from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ex 
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == "__main__":
    options = Options()
    options.add_argument('-headless')
    try:
        driver = webdriver.Chrome(options=options)
        driver.get('http://www.baidu.com')
        input = driver.find_element_by_id('kw')
        input.send_keys('python')
        wait = WebDriverWait(driver, 10)
        wait.until(ex.presence_of_element_located((By.ID, 'content_left')))
        print(driver.current_url)
        print(driver.get_cookies())
        print(driver.page_source)
    finally:
        driver.close()



