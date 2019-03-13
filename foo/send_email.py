#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time


def send_email():
    sender = '824024445@qq.com'
    receivers = ['824024445@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    f = open("files/record.json", "r", encoding="utf-8")
    content = f.read()
    mail_msg = """
    {}
      </tr>
    </table>
    </body>
    </html>
    """.format(content)
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = time.strftime("%Y-%m-%d")+ "中搜发帖"
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")