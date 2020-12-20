import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")    # 현재 같은경로에 크롬 드라이버가 있어서 () 안에 경로가 필요없어

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("zborisz")   
browser.find_element_by_id("pw").send_keys("Nav6105er2@")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("zborisz22")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.quit() # 전체 브라우저 종료


