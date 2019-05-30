import smtplib
from email.message import EmailMessage
from getpass import getpass

password = getpass('Password : ')
msg = EmailMessage()
msg['Subject'] = '제목을 지어 줍니다. 지금은 Untitled'
msg['From'] = 'gtj1323@naver.com'

# 한명에게 보낼 경우
# msg['To'] = 'oops0429@naver.com'
# 여러명에게 보낼 경우
email_list=['gtj1323@naver.com', 'oops0429@naver.com', 'jbt95955142@gmil.com']
msg['To'] = ','.join(list)

msg.set_content('햄 메일한번 보내 봅니다.')

s = smtplib.SMTP_SSL('smtp.naver.com', '995') # '메일', '포트'
s.login('gtj1323', password)
s.send_message(msg)

print('이메일 전송 완료 !!')
