from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.chrome.options import Options


option = Options()
option.add_argument('-headless')
browser = webdriver.Chrome(options=option)
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time out')

try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()

