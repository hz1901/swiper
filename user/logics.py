import random

import requests
from django.core.cache import cache
from swiper import cfg
from common import keys

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

