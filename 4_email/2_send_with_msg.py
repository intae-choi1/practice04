import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = " 테스트 메일"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "matalsidra@naver.com"
msg.set_content("테스트 본문")

# 여러명에게 보낼 때
# msg["To"] = "matalsidra@naver.com, abcd@abcd.abc, abcd2@abcd.abc"
# 참조
# msg["Cc"] = "메일 주소"
# 비밀 참조
# msg["Bcc"] = "메일 주소"


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 수립되었는지 확인
    smtp.starttls() # 내용을 암호화하여 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    smtp.send_message(msg)