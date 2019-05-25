# 获取节点信息
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('-headless')
browser = webdriver.Chrome(options=options)
browser.get('https://www.zhihu.com/explore')
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
print(logo.text)
print(logo.id)
print(logo.location)
print(logo.tag_name)
print(logo.size)