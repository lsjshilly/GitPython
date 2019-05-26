from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

url ='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

try:
    option = Options()
    option.add_argument('-headless')
    browser = webdriver.Chrome(options=option)
    browser.get(url)
    browser.switch_to_frame('iframeResult')
    try:
        logo = browser.find_element_by_class_name('logo')
        print(logo)
    except:
        print('NO LOGO')
        browser.switch_to.parent_frame()
        try:
            logo = browser.find_element_by_class_name('logo')
            print(logo)
            print(logo.text)
        except:
            print('NO LOGO')
except:
    print('false')

browser.close()
print('done')


    