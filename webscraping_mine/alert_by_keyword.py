import re
import requests
from bs4 import BeautifulSoup

# 이메일 보내기 위함
import smtplib
from account import *
from email.message import EmailMessage

def create_soup(url):
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language":"ko-KR,ko" # 만약 페이지가 등록된 header, 국가에 따라 다른 페이지를 제공한다면 한국 페이지 접근하기 위해 필요한 설정
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def web_test():
    url = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page={}&hotlist_flag=999&divpage=64".format(1)
    soup = create_soup(url)
    with open("web_test.html", "w", encoding="utf8") as f:
        f.write(soup.prettify())

def send_email(content):
    
    msg = EmailMessage() # 객체생성
    msg["Subject"] = "alert_by_keyworkd_뽐뿌_마스크." # 제목
    msg["From"] = EMAIL_ADDRESS # 보내는 사람
    msg["To"] = "zborisz@naver.com" # 받는 사람

    msg.set_content(content) # 본문

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def scrape_ppomppu(max_page, list_keyword):
    dic_content = {}
    total_contents = ''

    for keyword in list_keyword:
        dic_content[keyword] = ''

    for i in range(1, max_page):
        url = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page={}&hotlist_flag=999&divpage=64".format(i)
        soup = create_soup(url)
        data_rows = soup.find("table", attrs={"id":"revolution_main_table"}).find_all("tr", {"class": ["list0","list1"]})
        for row in data_rows:
            close = row.find("img", attrs={"src":"/zboard/skin/DQ_Revolution_BBS_New1/end_icon.PNG"})
            if close:
                continue
            row_title = row.find("font", attrs={"class":"list_title"}).get_text().replace(" ","").upper()
            row_link = "http://www.ppomppu.co.kr/zboard/" + row.find("a", attrs={"href":re.compile("^view.php")})["href"]
            for keyword in list_keyword:
                if keyword in row_title:
                    dic_content[keyword] += row_title + '|'
                    dic_content[keyword] += row_link + '|'
    for keyword in list_keyword:
        total_contents += "="*20 + " " + keyword + " " + "="*20 + "\r\n"
        
        if dic_content[keyword] == '':
            total_contents += '{}, no search result'.format(keyword) + '\r\n'
        # '\r\n'.join하면 문자열이 개행되면서 합쳐진다.
        total_contents += "\r\n".join(dic_content[keyword].split("|"))

    return total_contents

# 프로그램 직접 호출할 때만 사용되도록
if __name__ == "__main__":
    # web_test()
    
    brand = 'apple,Samsung,LG'
    print(brand.upper())

    try:
        print("[alert by keyword | site : ppomppu]")
        max_page = int(input("검색할 최대 페이지를 입력하세요 : " ))
        keyword = input("키워드를 입력하세요(구분자 : ,) :")

    except ValueError:
        print("에러! 잘못된 값을 입력했습니다.")

    list_keyword = keyword.replace(" ","").upper().split(",")
    content = scrape_ppomppu(max_page, list_keyword)
    send_email(content)