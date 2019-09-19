import datetime

from django.db import models

# Create your models here.

class User(models.Model):
    SEX = (
        ('mail', '男性'),
        ('femail', '女性')
    )
    LOCATION = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('广州', '广州'),
        ('深圳', '深圳'),
        ('杭州', '杭州'),
        ('武汉', '武汉'),
        ('成都', '成都'),
        ('重庆', '重庆'),
        ('西安', '西安'),
        ('沈阳', '沈阳'),
    )
    phonenum = models.CharField(max_length=16, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=32, verbose_name='昵称')
    sex = models.CharField(max_length=8, choices=SEX, verbose_name='性别')
    birthday = models.DateField(default=datetime.date(1999,1,1),verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='头像')
    location = models.CharField(max_length=15, choices=LOCATION, verbose_name='城市')