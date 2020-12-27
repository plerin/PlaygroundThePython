import requests
from bs4 import BeautifulSoup

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


def scrape_ppomppu():
    print("[ppomppu]")

    for i in range(1, 11):
        url = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page={}&hotlist_flag=999&divpage=64".format(i)
        soup = create_soup(url)
        # print(soup)
        data_rows = soup.find("table", attrs={"id":"revolution_main_table"}).find_all("tr", {"class": ["list0","list1"]})
        # print(data_rows)
        for row in data_rows:
            close = row.find("img", attrs={"src":"/zboard/skin/DQ_Revolution_BBS_New1/end_icon.PNG"})
            if close:
                continue
            contents = row.find("font", attrs={"class":"list_title"}).get_text()
            print(contents)

# 프로그램 직접 호출할 때만 사용되도록
if __name__ == "__main__":
    # web_test()
    scrape_ppomppu()