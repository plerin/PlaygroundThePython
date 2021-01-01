import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage() # 객체생성
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "zborisz@naver.com" # 받는 사람

# 여러 명에게 메일을 보낼 때
# to_list = ["zborisz@naver.com, plerin153@qbicware.com"]
# msg["To"] =  ", ".join(to_list)

# 참조
# msg["Cc"] = "zborisz@naver.com"

# 비밀참조
# msg["BCc"] = "zborisz@naver.com"

msg.set_content("테스트 본문입니다. 아아 다이노스오~") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)