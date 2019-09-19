from django.http import JsonResponse
from user import logics
from common import stat
from django.core.cache import  cache
from common import keys
from user.models import User

# Create your views here.
def get_vcode(request):
    '''用户获取验证码'''
    phonenum = request.GET.get('phonenum')
    if logics.send_vcode(phonenum):
        return JsonResponse({'code': stat.OK, 'data': None})
    else:
        return JsonResponse({'code': stat.SMSErr})

def check_vcode(request):
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    cached_vcode = cache.get(keys.VCODE_KEY%phonenum)

    # 检查验证码是否过期
    if cached_vcode == None:
        return JsonResponse({'code': stat.VcodeExpired, 'data': 'VcodeExpired'})

    # 检查验证码是否正确
    if cached_vcode == vcode:
        # 获取或创建用户
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum, nickname=phonenum)

        # 使用session记录用户登陆信息
        request.session['uid']  = user.id

        return JsonResponse({'code': stat.OK, 'data': user.to_dict()})
    else:
        return JsonResponse({'code': stat.VcodeErr, 'data': 'VcodeErr'})
