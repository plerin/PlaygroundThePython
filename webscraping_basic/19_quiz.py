"""
browser에 접속하고 검색창에 입력(송파 헬리오시티) 후 검색 버튼 눌러야해 -> selenium 필요 
부동산 부분에 나오는 결과 정보 갖고와야해 browser.find_element_by_xx

어떻게 만들거야?
1. selenium 사용
2. headless Chrome 사용
3. url 변수 만들고 get으로 사용해 
4. 검색창 경로를 알아서 송파 헬리오시티 입력
5. 검색 xpath찾아서 click()
6. find_elements로 부동산 정보 갖고와 
7. for문 돌며 찍어줘
8. browser 닫아줘 quit()사용 
"""

# 1. 
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# 2.
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")   # 내부적으로 이 크기로 띄운다.
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 3.
url ="https://www.daum.net/"
browser.get(url)

# 4.
browser.find_element_by_id("q").send_keys("송파 헬리오시티")  

# 5.
browser.find_element_by_class_name("btn_search").click()

soup = BeautifulSoup(browser.page_source, "lxml")

# 6.
print(soup.find_all("td", attrs={"class":"col1"}))