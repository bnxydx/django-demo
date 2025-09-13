# WeatherApp/tasks.py

from celery import shared_task
from .utils.SendWeatherData import send_email
from django.core.management import call_command  # 可选：如果你有 manage.py 命令
from django.db import connection
from WeatherApp.models import WeatherModels  # 替换为你的实际模型路径
from WeatherApp.serializer import WeatherSerializers  # 替换为你的实际序列化器
from .views import weather_query  # 确保你能导入这个函数

@shared_task
def se(Qnum, text, City):
    """发送单个用户的天气邮件"""
    send_email(Qnum, text, City)
    return 'OK1'

@shared_task
def se_batch():
    """每天早上7点执行：批量发送天气邮件"""
    from django.db import connection
    connection.close()  # 防止多进程数据库连接问题（可选）

    # 获取所有订阅用户
    users = WeatherModels.objects.all()
    serializer = WeatherSerializers(users, many=True)

    for item in serializer.data:
        Qnum = item['Qnum']
        City = item['City']
        text = weather_query(City)
        # 异步发送每个用户邮件（避免阻塞）
        se.delay(Qnum, str(text), City)

    return f"Triggered {len(serializer.data)} weather emails."