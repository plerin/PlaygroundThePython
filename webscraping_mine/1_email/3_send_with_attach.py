import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage() # 객체생성
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "plerin152@gmail.com" # 받는 사람```
# msg["To"] = "zborisz@naver.com" # 받는 사람```
msg.set_content("다운로드 하세요")



# msg.add_attachment()    # 첨부파일 등록
# rb readbinary
# MIME_TYPE 참조 _ https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types 
with open("google_movie.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)

with open("테스트.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("엑셀.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)