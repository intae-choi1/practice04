import smtplib
from account import *


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 수립되었는지 확인
    smtp.starttls() # 내용을 암호화하여 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    
    subject = "test mail" # 메일 제목
    body = "mail body" # 메일 본문
    
    msg = f"Subject: {subject}\n{body}" # 이 형태로 msg를 작성해야 메일을 보낼 수 있음
    
    smtp.sendmail(EMAIL_ADDRESS, "matalsidra@naver.com", msg)