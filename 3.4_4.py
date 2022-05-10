"""
                                           3.4 Статус коды  4
1. Откройте сайт http://parsinger.ru/task/1/
2. На нём есть 500 ссылок  и только 1 вернёт статус код 200
3. Напишите код который поможет найти правильную ссылку
4. По этой ссылке лежит секретный код, который необходимо вставить в поле ответа.

"""



import requests
from bs4 import BeautifulSoup

for x in range(1,501):
    url = f'http://parsinger.ru/task/1/{x}.html'
    resp = requests.get(url=url)
    if resp.status_code == 200:
        print(url)
        soup = BeautifulSoup(resp.text, 'lxml')
        print(soup.find("body"))