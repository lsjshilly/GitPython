from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://www.jd.com/')
    input = browser.find_element_by_id('key')
    input.send_keys('固态硬盘')
    time.sleep(2)
    input.clear()
    time.sleep(2)
    input = browser.find_element_by_id('key')
    input.send_keys('固态硬盘')
    time.sleep(2)
    button = browser.find_element_by_class_name('button')
    button.click()
    time.sleep(2)
finally:
    browser.close()
