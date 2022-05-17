"""
                                            4.8 Парсим JSON 2


"""


import requests as requests

url = 'http://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()
for item in response:
    print(item["description"]['brand'], item["description"]['model'])
