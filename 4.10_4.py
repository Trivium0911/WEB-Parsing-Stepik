"""
                                    4.10 Парсим JSON 4

Используйте полученный по ссылке JSON (http://parsinger.ru/downloads/get_json/res.json)
чтоб посчитать стоимость товаров в каждой отдельной категории.

На вход ожидается словарь. {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N} где N это общая стоимость товаров в категории.

"""


import requests

url = 'http://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()
res_dct = {'watch': 0, 'mobile': 0, 'mouse': 0, 'hdd': 0, 'headphones': 0}
for item in response:
    for key in res_dct.keys():
        if item['categories'] == key:
            res_dct[key] += int(item['price'].replace(" руб", '')) * int(item['count'])
print(res_dct)