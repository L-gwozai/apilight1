import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_wechat_message(webhook_url, message_content):
    # 构建消息内容
    message = {
        "msgtype": "text",
        "text": {
            "content": message_content
        }
    }

    # 发送POST请求，使用json参数而不是data
    response = requests.post(webhook_url, json=message)

    # 检查响应
    if response.status_code == 200:
        print("消息发送成功")
    else:
        print(f"消息发送失败，HTTP响应码: {response.status_code}")






def send_markdown_email(receiver_email, markdown_text, choice=1, subject=None):
    # 邮箱配置信息
    email_configs = {
        1: {
            'smtp_server': 'smtp.qq.com',
            'smtp_port': 587,
            'sender_email': '3281941735@qq.com',
            'sender_password': 'buuxpowmjnngcjif',
        },
        2: {
            'smtp_server': 'smtp.163.com',
            'smtp_port': 25,
            'sender_email': 'your_netease_email@163.com',
            'sender_password': 'your_netease_password',
        }
    }

    if choice not in email_configs:
        print("无效的选项")
        return

    # 获取选定的邮箱配置
    email_config = email_configs[choice]

    # 创建电子邮件
    if subject is None:
        subject = 'nocodb每日监督'
    body = markdown_text
    message = MIMEMultipart()
    message['From'] = email_config['sender_email']
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # 连接到SMTP服务器
        server = smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port'])
        server.starttls()  # 使用TLS加密连接
        server.login(email_config['sender_email'], email_config['sender_password'])

        # 发送电子邮件
        server.sendmail(email_config['sender_email'], receiver_email, message.as_string())
        print('电子邮件发送成功')
    except Exception as e:
        print(f'电子邮件发送失败: {e}')
    finally:
        server.quit()

# # 替换为你的企业微信机器人URL
# webhook_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=81834e10-3e84-404c-8880-32ff2e242777'

# # 要发送的消息内容
# message_content = "hello world"

# # 调用函数发送消息
# send_wechat_message(webhook_url, message_content)


# # 使用示例
# receiver_email = "584257191@qq.com"
# markdown_text = "这是一封包含Markdown文本的示例邮件。"
# subject = "哦吼吼"  # 自定义标题
# send_markdown_email(receiver_email, markdown_text, choice=1, subject=subject)

