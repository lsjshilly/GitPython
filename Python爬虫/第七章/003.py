from selenium import webdriver
from selenium.webdriver import ActionChains
import time

try:
    # browser = webdriver.Chrome()
    # browser.get('https://www.jd.com/')
    # time.sleep(3)
    # souce = browser.find_element_by_class_name('focus_item_img')
    # target = browser.find_element_by_id('key')
    # actions = ActionChains(browser)
    # actions.drag_and_drop(souce, target)
    # actions.perform()
    # time.sleep(2)
    # browser.close()
# ************************************************************
    browser = webdriver.Chrome()
    browser.get('https://weibo.com/')
    time.sleep(10)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    browser.execute_script('alert("To Botton")')
    browser.close()
finally:
    browser.close()
