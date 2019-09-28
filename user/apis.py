# from django.forms import model_to_dict
from django.http import JsonResponse
from user import logics
from common import stat
from django.core.cache import  cache
from common import keys
from user.models import User
from libs.http import render_json
from libs.orm import model_to_dict
from user.forms import UserForm, ProfileForm


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
    # print(user.__dict__)
    # print(user.profile.__dict__)
    # print(model_to_dict(user.profile))
    return render_json(data=model_to_dict(user.profile))

def set_profile(request):
    '''修改个人资料，及交友资料'''
    user = request.user
    user_form = UserForm(request.POST)
    if user_form.is_valid():
        user.__dict__.update(user_form.cleaned_data) # 跟新对象数据
        user.save()
    else:
        return render_json(data=user_form.errors, code=stat.UserDataErr)

    profile_form = ProfileForm(request.POST)
    if profile_form.is_valid():
        '''通过本地保存，减少数据库的一次查询，user_form应该也可以用这种方法。'''
        profile = profile_form.save(commit=False)  # 先本地缓存过滤后的正确数据
        profile.id = user.id                   # 通过ID修改确保数据一直
        profile.save()              # 保存数据到数据库
    else:
        return render_json(data=profile_form.errors,code=stat.ProfileDataErr)

    return render_json()



def upload_avatar(request):
    '''上传头像'''
    avatar_file = request.FILES['avatar']
    logics.upload_avatar.delay(request.user, avatar_file)
    return render_json()