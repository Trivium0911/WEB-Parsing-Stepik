"""
                            4.7 Парсинг табличных данных 5
На  сайте (https://parsinger.ru/table/4/index.html) расположена таблица;
Цель: Собрать числа в зелёных ячейках и суммировать их;
Полученный результат вставить в поле ответа.
"""

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://parsinger.ru/table/4/index.html').text, 'lxml')
res = [float(i.text) for i in soup.find_all('td', class_='green')]
print(sum(res))
