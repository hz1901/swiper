import time
from django.utils.deprecation import MiddlewareMixin

from user.models import User
from libs.http import render_json
from common import stat

def timer_pass(func):
    '''时间检查装饰器'''
    stip_time = lambda :time.time()
    def warp(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        used = (t2 - t1) * 1000
        print('接口耗时：%0.2f ms' %used)
        return res
    return warp

class AuthMiddleware(MiddlewareMixin):
    PATH_WHITE_LIST = [
        '/api/user/get_vcode',
        '/api/user/check_vcode'
    ]
    def process_request(self,request):
        if request.path in self.PATH_WHITE_LIST:
            return
        uid = request.session.get('uid')
        # print(uid)
        # 检查session是否有uid
        if not uid:
            return render_json(code=stat.LoginRequired)
        request.user = User.objects.get(id=uid)
