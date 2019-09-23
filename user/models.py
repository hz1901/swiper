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

    @property
    def profile(self):
        # 用户的交友资料
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile

    def to_dict(self):
        return {
            'id': self.id,
            'phonenum': self.phonenum,
            'sex': self.sex,
            'birthday': str(self.birthday),
            'avatar': self.avatar,
            'location': self.location
        }

class Profile(models.Model):
    dating_sex = models.CharField(max_length=8, choices=User.SEX, verbose_name='匹配的性别')
    dating_location = models.CharField(max_length=16, choices=User.LOCATION, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1,verbose_name='最小查询范围')
    max_distance = models.IntegerField(default=50,verbose_name='最大查询范围')

    min_dating_age = models.IntegerField(default=18,verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50,verbose_name='最大交友年龄')

    vibration = models.BooleanField(verbose_name='开启震动', default=True)
    only_matche = models.BooleanField(verbose_name='不让为匹配的人看我的相册', default=True)
    auto_play = models.BooleanField(verbose_name='自动播放视频', default=False)