import os

from celery import Celery
from worker import config
# 加载Django 的 setting
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")

celery_app = Celery('worker')            # 实例话一个celery
celery_app.config_from_object(config)      # 加载相关配置
celery_app.autodiscover_tasks()          #自动监听任务