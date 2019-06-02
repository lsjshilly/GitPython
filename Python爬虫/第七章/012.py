from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 5)


def search():
    browser.get('https://www.jd.com/')
    try:
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
        next_input.clear()
        next_input.send_keys(page)
        next_submit.click()
        wait.until(ES.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'), str(page)))
        time.sleep(1)
        # time.sleep(3)
        # return browser.page_source
    except TimeoutException:
        next_page(page)


if __name__ == "__main__":
    search()
    for i in range(1, 20):
        next_page(i)
