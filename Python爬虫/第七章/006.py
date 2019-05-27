from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.by import By



option = Options()
option.add_argument('-headless')
browser = webdriver.Chrome(options=option)
browser.get('http://www.baidu.com')
wait = WebDriverWait(browser, 10)
input = wait.until(ES.presence_of_element_located((By.ID, 'kw')))
button = wait.until(ES.presence_of_element_located((By.ID, 'su')))
print(input)
print(button)