import random
import os
import requests
from django.core.cache import cache
from swiper import cfg
from common import keys
from django.conf import settings
from libs.qncloud import upload_to_qn
from worker import celery_app

def random_code(length=6):
    '''产生一个指定长度的随机码'''
    return  ''.join([str(random.randrange(10)) for i in range(length)])

def send_vcode(phonenum):
    '''发送验证码'''
    vcode = random_code()
    cache.set(keys.VCODE_KEY%phonenum, vcode, 180)  # 使用缓存验证码记录，180秒后过期
    print('vcode:', vcode)
    parmas = cfg.YZX_PARAMS.copy()
    parmas['param'] = vcode
    parmas['mobile'] = phonenum
    return True
    resp = requests.post(cfg.YZX_API,json=parmas)
    # print(resp.json())
    if resp.status_code == 200:
        return True
    else:
        return False

def save_avatar(upload_file, uid):
    filename = 'Avatar-%s' % uid
    print(filename)
    fullpath = os.path.join(settings.MEDIA_ROOT, filename)
    with open(fullpath, 'wb') as fp:
        for chunk in upload_file.chunks():   #  跟readlines有点像，单比readlines好，readlines如果数据就是一行读取就不好了。
            fp.write(chunk)
    return fullpath, filename

@celery_app.task
def upload_avatar(user, avatar_file):
    # 将文件保存到服务器
    fullpath, filename = save_avatar(avatar_file, user.id)
    # 上传到七牛云
    avatar_url = upload_to_qn(localfile=fullpath, filename=filename)
    # print(dir(avatar_file), type(avatar_file))
    # 删除本地文件
    # os.remove(fullpath)
    # 将链接保存到数据库
    user.avatar = avatar_url
    user.save()
    return avatar_url