"""
                                4.7 Парсинг табличных данных 3
На  сайте (https://parsinger.ru/table/2/index.html) расположена таблица;
Цель: Собрать числа с 1го столбца и суммировать их;
Полученный результат вставить в поле ответа.

"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/2/index.html')
soup = BeautifulSoup(response.text, 'lxml')
lines = soup.find_all('tr')
res = []
for line in lines[1:]:
    res.append(float(line.contents[1].next))
print(sum(res))