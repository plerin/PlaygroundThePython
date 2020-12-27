import re
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

def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("  (링크 : {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?ie=UTF-8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&sm=chr_hty"
    soup = create_soup(url)
    # 날씨 정보
    cast = soup.find("p", attrs={"class": "cast_txt"}).get_text()
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text() # 최저온도
    max_temp = soup.find("span", attrs={"class":"max"}).get_text() # 최저온도

    #강수확률
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    # 미세먼지
    # dust = soup.find("dl", attrs={"class":"indicator", "id":"id인 값"}, texet=["미세먼지","초미세먼지"])
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text() # 미세먼지
    pm25 = dust.find_all("dd")[1].get_text() # 초미세먼지


    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp,min_temp,max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()

def scrape_headline_news():
    print("[스포츠 뉴스]")
    url = "https://sports.news.naver.com"
    soup = create_soup(url)
    # limit 붙이면 x개까지만 찾아라
    news_list = soup.find("ul", attrs={"class":"today_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        # title = news.div.a.get_text().strip()
        title = news.find("strong", attrs={"class":"title"}).get_text().strip()
        link = url + news.find("a")["href"]   
        print_news(index, title, link)
    print()     

def scrape_it_news():
    print("[it 뉴스]")   
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)  # 3개까지만 가져오자
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번재 a 태그의 정보를 상ㅇ

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)

    print()

def scrape_english():
    print("[오늘의 영어 회화]")   
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    # attrs 안에 re.compile("^conv_kor_t") 이면 , id가 'conv_kor_t'로 시작하는 모든 div 태그를 모두 가져올 수 있어
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    # // 인 이유는 나머지가 떨어지지 않았을 때 버리기위해
    for sentence in sentences[len(sentences)//2:]: # 8 문장이 있다고 가정할 때, 5~8까지 잘라서 가져옴
        print(sentence.get_text().strip())

    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())

# 이 프로그램을 직접 실행할 때는 호출, 다른 파일을 통해 실행할 때는 실행안됨
if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # sport 뉴스 가져오기
    scrape_it_news() # it 뉴스 가져오기
    scrape_english() # 오늘의 영어 회화 가져오기
