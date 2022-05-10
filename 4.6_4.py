"""
                            4.6 Сохраняем результат в Excel 4

Напишите код который собирает данные в категории HDD (http://parsinger.ru/html/index4_page_1.html) со всех 4х страниц и сохраняет всё в таблицу, по примеру предыдущего степа.

Заголовки :  Наименование, Бренд, Форм-фактор, Ёмкость, Объём буф. памяти, Цена


"""


import csv
import requests
from bs4 import BeautifulSoup

with open('res.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объём буф. памяти', 'Цена'
    ])

url = 'http://parsinger.ru/html/index4_page_1.html'

response = requests.get(url=url)
response.encoding = 'UTF-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'
links = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]

for link in links:
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]

    for item, descr, price in zip(name, description, price):
        result = []
        flatten = item, [x.split(':')[1].strip() for x in descr if x], price
        for x in flatten:
            if isinstance(x, list):
                for i in x:
                    result.append(i)
            else:
                result.append(x)
        print(result)
        with open('res.csv', 'a', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(result)
    print('Done')


