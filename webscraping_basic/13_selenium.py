from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")    # 현재 같은경로에 크롬 드라이버가 있어서 () 안에 경로가 필요없어
browser.get("http://naver.com")

