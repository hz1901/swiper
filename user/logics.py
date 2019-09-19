import random

import requests

from swiper import cfg


def random_code(length=6):
    '''产生一个指定长度的随机码'''
    return  ''.join([str(random.randrange(10) for i in range(length))])

def send_vcode(phonenum):
    '''发送验证码'''
    vcode = random_code()
    parmas = cfg.YZX_PARAMS.copy()
    parmas['param'] = vcode
    parmas['mobile'] = phonenum
    resp = requests.post(cfg.YZX_API,json=parmas)
    if resp.status_code == 200:
        return True
    else:
        return False

