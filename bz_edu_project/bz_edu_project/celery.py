import pymysql
pymysql.install_as_MySQLdb()
#
# import eventlet
# eventlet.monkey_patch()


import os
import django
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# 设置系统环境变量，安装django，必须设置，否则在启动celery时会报错
# celery_study 是当前项目名
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bz_edu_project.settings')
django.setup()
# 实例化一个celery类
celery_app = Celery('celery_study')
# 指定配置文件的位置
celery_app.config_from_object('django.conf:settings')
# 自动从settings的配置INSTALLED_APPS中的应用目录下加载 tasks.py
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# bz_edu_project/celery.py

import os
from celery import Celery
from celery.schedules import crontab  # ⬅️ 导入 crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bz_edu_project.settings')

app = Celery('bz_edu_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现任务
app.autodiscover_tasks()

# ========== ⬇️ 添加定时任务配置 ==========
app.conf.beat_schedule = {
    'send-weather-every-morning-7am': {
        'task': 'WeatherApp.tasks.se_batch',  # ⬅️ 我们稍后创建这个“批量任务”
        'schedule': crontab(hour=6, minute=55),
        # 'schedule': crontab(minute='*/1'),  # 测试用：每分钟执行一次
    },
}
app.conf.timezone = 'Asia/Shanghai'