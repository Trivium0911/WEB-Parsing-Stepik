"""
                                        4.7 Парсинг табличных данных 7
На  сайте (https://parsinger.ru/table/5/index.html) расположена таблица;
Цель: Написать скрипт который формирует словарь, где ключ будет автоматически формироваться из заголовка таблицы, а значения это сумма всех чисел в столбце;
Полученный словарь вставить в поле ответа.

"""


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://parsinger.ru/table/5/index.html').text, 'lxml')
lines = soup.find_all('tr')
dct = {}
for key in lines[0]:
    if key != '\n':
        dct[key.text] = 0
for line in lines[1:]:
    line_strip = line.text.split('\n')
    for column, elem in zip(dct, line_strip[1:-1]):
        dct[column] += float(elem)
for k, v in dct.items():
    dct[k] = round(v, 3)
print(dct)
