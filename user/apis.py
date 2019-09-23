from django.forms import model_to_dict
from django.http import JsonResponse
from user import logics
from common import stat
from django.core.cache import  cache
from common import keys
from user.models import User
from libs.http import render_json
from libs.orm import model_to_dict

# Create your views here.
def get_vcode(request):
    '''用户获取验证码'''
    phonenum = request.GET.get('phonenum')
    if logics.send_vcode(phonenum):
        return render_json()
    else:
        return JsonResponse(code=stat.SMSErr)

def check_vcode(request):
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    cached_vcode = cache.get(keys.VCODE_KEY%phonenum)
    # 检查验证码是否过期
    if cached_vcode == None:
        return render_json(code=stat.VcodeExpired, data='VcodeExpired')

    # 检查验证码是否正确
    if cached_vcode == vcode:
        # 获取或创建用户
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum, nickname=phonenum)

        # 使用session记录用户登陆信息
        request.session['uid']  = user.id
        return render_json(code=stat.OK, data=model_to_dict(user))
    else:
        return render_json(code=stat.VcodeErr, data='VcodeErr')

def get_profile(request):
    '''获取个人信息及交友资料'''
    user = request.user
    # use = User.objects.get(id=uid)
    # print(request.path)
    # print(dir(request.session))
    # print(request.session.items)
    return render_json(data=model_to_dict(user.profile))

def set_profile(request):
    '''修改个人资料，及交友资料'''
    return render_json()

def upload_avatar(request):
    '''上传头像'''
    return render_json()