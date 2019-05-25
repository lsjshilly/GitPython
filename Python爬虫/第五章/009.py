import time
import requests
import urllib
import json

url = 'https://www.toutiao.com/api/search/content/?'
# url = 'https://www.toutiao.com/api/search/content/?keyword=%E8%A1%97%E6%8B%8D'

headers = {
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

def get_page(page):
    parameters = {
        'keyword': '街拍',
        'aid': 24,
        'app_name': 'web_search',
        'offset': page,
        'format': 'json',
        
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        # 'timestamp': times
    }


    total_url = url + urllib.parse.urlencode(parameters)
    print(total_url)
    try:
        response = requests.get(url=total_url, headers=headers)
        print(response)
        if response.status_code == 200:
            print(response.text)
            return response.text
    except requests.ConnectionError as e:
        print(e.args)

def parse_page(json):
    if json.get('data'):
        print(json.get('data'))
        items = json.get('data')

        for i in range(1, len(items)):
            title = items[i].get('title')
            print(title)
            image_urls = items[i].get('image_list')
            for image_url in image_urls:
                img_url = image_url.get('url')
                save_pictures(img_url)



def save_pictures(url):
    name = './images/'+url[-7:]+'jpg'
    response = requests.get(url)
    with open(name,'wb') as f:
        f.write(response.content())


if __name__ == "__main__":
    for page in range(0, 10):
        times = round(time.time()*1000)
        json = get_page(page*20)
        # parse_page(json)