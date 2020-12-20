""" 
headless 옵션을 설정하면 실제로 브라우저를 띄우지 않고 실행할 수 있다.
그런데 그럴경우 user-agent를 확인해보면 HeadlessChrome 이라는 정보가 있어 사이트에 막을 수 있어 따로 지정해줘야함 
-> options.add_argument("user-agent=")
 """
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")   # 내부적으로 이 크기로 띄운다.
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url ="https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()