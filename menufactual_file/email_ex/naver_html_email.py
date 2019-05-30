import smtplib
#from email.message import EmailMessage
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

password = getpass('Password : ')

msg = MIMEMultipart()
msg['Subject'] = '제목을 지어 줍니다. 지금은 Untitled'
msg['From'] = 'gtj1323@naver.com'

# 한명에게 보낼 경우
# msg['To'] = 'oops0429@naver.com'
# 여러명에게 보낼 경우
email_list=['gtj1323@naver.com', 'oops0429@naver.com', 'jbt95955142@gmil.com']
msg['To'] = ','.join(list)

html = """
<html>
    <body>
        <img src="http://sampleimg.com/asdasd.png">
        <p>HI,</p>
        <a href = "https://www.google.com">GO TO GOGGLE</a>
    </body>
</html>
"""
part = MIMEText(html, 'html')
msg.attach(part)

s = smtplib.SMTP_SSL('smtp.naver.com', '995') # '메일', '포트'
s.login('gtj1323', password)
s.send_message(msg)

print('이메일 전송 완료 !!')
