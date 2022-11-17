import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = " 테스트 메일"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
msg.set_content("첨부파일 있음")

with open("../2_desktop/img/file_menu.png", "rb") as f:
    print(f.name)
    # main/sub type = MIME type , 영상 오디오 등은 검색해서 찾자
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)
    
# mime type example
# with open("xxx.pdf", "rb") as f:
#     msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 수립되었는지 확인
    smtp.starttls() # 내용을 암호화하여 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    smtp.send_message(msg)