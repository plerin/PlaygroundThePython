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


# # selenium이 필요한지 확인하려고 일단 request로 받아온 html 문서로 우리가 갖고올 수 있는지 확인
# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

# 3.
url ="https://www.daum.net/"
browser.get(url)

# 4.
browser.find_element_by_id("q").send_keys("송파 헬리오시티")  

# 5.
browser.find_element_by_class_name("btn_search").click()

soup = BeautifulSoup(browser.page_source, "lxml")

# 6. 내 풀이
# col1s = soup.find_all("td", attrs={"class":"col1"})
# col2s = soup.find_all("td", attrs={"class":"col2"})
# col3s = soup.find_all("td", attrs={"class":"col3"})
# col4s = soup.find_all("td", attrs={"class":"col4"})
# col5s = soup.find_all("td", attrs={"class":"col5"})

# for idx in range(0,5):
#     print("="*15,"매물",(idx+1),"="*15)
#     print("거래 : ", col1s[idx].get_text())
#     print("면적 : ", col2s[idx].get_text())
#     print("가격 : ", col3s[idx].get_text())
#     print("동 : ", col4s[idx].get_text())
#     print("층 : ", col5s[idx].get_text())


# 문제 풀이 
'''

'''
# url = "https://search.daum.net/search?w=tot&DA=JU5&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
# class가 tbl인 table 찾고 그 안에서 첫번째 tbody 그리고 그 안의 모든 tr 을 갖고오는 코드 
data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
print(data_rows)
# list인데 index를 사용해야 할 경우 해당 list를 enumerate()로 감싸주기
for idx, row in enumerate(data_rows):
    columns = row.find_all("td")
    print("="*15,"매물",idx,"="*15)
    print("거래 : ", columns[0].get_text().strip())
    print("면적 : ", columns[1].get_text().strip(), "(공급/전용)")
    print("가격 : ", columns[2].get_text().strip(), "(만원)")
    print("동 : ", columns[3].get_text().strip())
    print("층 : ",columns[4].get_text().strip() )
