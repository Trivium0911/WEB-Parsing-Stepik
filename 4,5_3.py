"""    4.5 Пагинация 3

1. Откройте сайт http://parsinger.ru/html/index3_page_1.html
2. Извлеките названия товара с каждой страницы (всего 4х страниц)
3. Данные с каждой страницы должны хранится в списке.
4. По итогу работы должны получится 4 списка которые хранятся в списке(список списков)
5. Отправьте получившийся список список в поле ответа.
6. Метод strip()использовать не нужно

Пример ожидаемого списка:

[[' name1 ', 'name2', ' ... ', ' name_N'], [' name1 ', 'name2', ' ... ', ' name_N'], [' name1 ', 'name2', ' ... ', ' name_N'], [' name1 ', 'name2', ' ... ', ' name_N']]
"""


import requests
from bs4 import BeautifulSoup

url = 'http://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'
pagen = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
res = []
for link in pagen:
    resp = requests.get(url=link)
    resp.encoding = 'utf-8'
    sp = BeautifulSoup(resp.text,'lxml')
    res.append([i.text for i in sp.find_all('a', class_='name_item')])

print(res)
