from django.http import JsonResponse
from user import logics
from common import err

# Create your views here.
def get_vcode(request):
    '''用户获取验证码'''
    phonenum = request.GET.get('phonenum')
    if logics.send_vcode(phonenum):
        return JsonResponse({'code': err.OK, 'data': None})
    else:
        return JsonResponse({'code': err.VcodeErr})

def check_vcode(request):

    return JsonResponse({})