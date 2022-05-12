"""
                                4.6 Сохраняем результат в Excel 6

Напишите код который собирает данные в категории watch (http://parsinger.ru/html/index1_page_1.html)
c каждой карточки, всего их 32.

Обязательные Заголовки :  Наименование, Артикул, Бренд, Модель, Тип, Технология экрана, Материал корпуса, Материал браслета, Размер, Сайт производителя, Наличие, Цена, Старая цена,  Ссылка на карточку с товаром.

Всего должно быть 14 заголовков
"""

import csv
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8-sig'
    return BeautifulSoup(response.text, 'lxml')


def get_list_with_links(linktext, elem, classname):
    shema = 'http://parsinger.ru/html/'
    return [f"{shema}{link['href']}" for link in linktext.find(elem, class_=classname).find_all('a')]


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель',
                     'Тип', 'Технология экрана', 'Материал корпуса',
                     'Материал браслета', 'Размер', 'Сайт производителя',
                     'Наличие', 'Цена', 'Старая цена',  'Ссылка на карточку с товаром'])

    url = 'http://parsinger.ru/html/index1_page_4.html'
    soup_link = get_soup(url)
    pagen = get_list_with_links(soup_link, 'div', 'pagen')
    for page in pagen:
        soup_page = get_soup(page)
        watches = [f"http://parsinger.ru/html/{link['href']}" for link in soup_page.find_all('a', class_="name_item")]
        for watch in watches:
            watch_page = get_soup(watch)
            description = [x.text.strip().split("\n") for x in watch_page.find_all('div', class_='description')]
            res = []
            for i in description:
                for j in i:
                    if j == '' or j == 'Купить':
                        continue
                    elif ": " in j:
                        res.append(j.split(": ")[1])
                    else:
                        res.append(j)
            res.append(watch)
            writer.writerow(res)


