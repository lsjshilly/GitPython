import requests
# from urllib.parse import urlencode
# from requests import codes
# import os
# from hashlib import md5
# from multiprocessing.pool import Pool
# import re


# def get_page(offset):
#     params = {
#         'aid': 24,
#         'offset': offset,
#         'format': 'json',
#         #'keyword': '街拍',
#         'autoload': 'true',
#         'count': '20',
#         'cur_tab': '1',
#         'from': 'search_tab',
#         'pd': 'synthesis'
#     }
#     base_url = 'https://www.toutiao.com/api/search/content/?keyword=%E8%A1%97%E6%8B%8D'
#     url = base_url + urlencode(params)
#     print(url)
#     try:
#         resp = requests.get(url)
#         print(url)
#         if 200  == resp.status_code:
#             print(resp.json())
#             return resp.json()
#     except requests.ConnectionError:
#         return None


# def get_images(json):
#     if json.get('data'):
#         data = json.get('data')
#         for item in data:
#             if item.get('cell_type') is not None:
#                 continue
#             title = item.get('title')
#             images = item.get('image_list')
#             for image in images:
#                 origin_image = re.sub("list", "origin", image.get('url'))
#                 yield {
#                     'image':  origin_image,
#                     # 'iamge': image.get('url'),
#                     'title': title
#                 }
#                 print(origin_image)

#     print('succ')

# if __name__ == '__main__':

#     groups = [x * 20 for x in range(0, 10)]
#     for group in groups:
#         json = get_page(group)
#         get_images(json)



url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1558664109144'
headers = {
    
    # 'cookie': 'tt_webid=6694085347226043907; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6694085347226043907; UM_distinctid=16ae318c3609-047934d5bbbeb5-f353163-1fa400-16ae318c361c8e; csrftoken=f22eb4c96702ca46717d9c0f0f651684; uuid="w:d2ca1d90a32d4fcd97bf12ab03e33cf9"; s_v_web_id=ef0f84baf2354c9639e80a3d298edb99; __tasessionId=bs1ua8xw31558662765358; CNZZDATA1259612802=1664152150-1558584290-%7C1558659890',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

response = requests.get(url, headers=headers)
print(response.text)



   
   
   