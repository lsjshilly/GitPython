from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException,StaleElementReferenceException
from pyquery import PyQuery  as pq
import pymongo


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


client = pymongo.MongoClient(host='47.106.109.80', port=27017)
db = client['jingdong']
db.products.drop()
collection = db['products']

def search():
    browser.get('https://www.jd.com/')
    try:
        time.sleep(2)
        input = wait.until(ES.presence_of_element_located(
            (By.CSS_SELECTOR, '#key')))
        submit = wait.until(ES.element_to_be_clickable(
            (By.CSS_SELECTOR, '#search > div > div.form > button')))
        input.send_keys('ipad')
        submit.click()
    except TimeoutException:
        search()


def next_page(page):
    try:
        next_input = wait.until(ES.presence_of_element_located(
            (By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input')))
        next_submit = wait.until(ES.element_to_be_clickable(
            (By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > a')))
        try:
            next_input.clear()
            next_input.send_keys(page)
            next_submit.click()
        except StaleElementReferenceException:
            next_input = wait.until(ES.presence_of_element_located(
            (By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input')))
            next_submit = wait.until(ES.element_to_be_clickable(
            (By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > a')))
            next_input.clear()
            next_input.send_keys(page)
            next_submit.click()


        wait.until(ES.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'), str(page)))
        wait.until(ES.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList > ul > li')))
        get_procudts()
    except TimeoutException:
        next_page(page)

def get_procudts():
    time.sleep(3)
    html = browser.page_source
    doc = pq(html)
    items_list = doc('#J_goodsList > ul > li').items()
    k=0
    for item in items_list:
        k+=1
        products = {
            'price': item.find('div > div.p-price > strong > i').text(),
            'detail': item.find('div > div.p-name.p-name-type-2 > a > em').text(),
            'shop': item.find('div > div.p-shop > span > a').text()
        }
        print(products)
        save_mongodb(products)
    print('找到的总数是：{}'.format(k))

def save_mongodb(products):
    try:
        collection.insert_one(products)
        print('保存成功')
    except Exception:
        print('保存失败')




if __name__ == "__main__":
    search()
    for i in range(1, 10):
        print('*'*100)
        print('page'+str(i))
        print('*'*100)
        next_page(i)
        
    browser.close()


