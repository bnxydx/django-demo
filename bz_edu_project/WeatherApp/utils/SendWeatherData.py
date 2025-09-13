import ast
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr  # 用于格式化发件人

def send_email(Qnum,test,city):
    sender = '1123520338@qq.com'
    password = 'tbacvuoclcmqigfe'  # 你的授权码
    recipient = f'{Qnum}@qq.com'
    test = ast.literal_eval(test)
    # 创建邮件内容
    mail_text = f"""
        {city}
        今日天气:{test['text']},
        今日温度:{test['temp']},
        今日风向:{test['windDir']},
        今日风速:{test['windSpeed']},
    """
    msg_body = MIMEText(mail_text, 'plain', 'utf-8')

    # ✅ 正确设置 From（包含名称 + 邮箱）
    msg_body['From'] = formataddr(('305死鸡检测系统', sender), charset='utf-8')

    # To 和 Subject 也可以用 formataddr（可选）
    msg_body['To'] = formataddr(('监控接收人', recipient), charset='utf-8')
    msg_body['Subject'] = Header('天气预报', 'utf-8')

    try:
        # 使用 SSL 连接 QQ 邮箱
        smtp_obj = smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtp_obj.login(sender, password)
        smtp_obj.sendmail(sender, [recipient], msg_body.as_string())
        smtp_obj.quit()
        print("✅ 邮件发送成功")

    except smtplib.SMTPAuthenticationError:
        print("❌ 认证失败：检查授权码是否正确")
    except smtplib.SMTPServerDisconnected:
        print("❌ 连接已断开：网络或服务器问题")
    except Exception as e:
        print("❌ 其他错误：", str(e))

if __name__ == '__main__':
    # send_email('0.9')
    ...