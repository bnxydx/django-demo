from bz_edu_project.celery import celery_app
import time


# 定义任务函数
@celery_app.task  # 任务装饰器,将函数注册为celery任务
def send_email(name):
    print(f'准备发送{name}的邮件')
    time.sleep(5)
    print(f'{name}的邮件发送成功')

    return 'OK1'


@celery_app.task
def send_sms(name):
    print(f'准备发送{name}的短信')
    time.sleep(5)
    print(f'{name}的短信发送成功')
    return 'OK2'

if __name__ == '__main__':
    send_email('12')
    send_sms('12')