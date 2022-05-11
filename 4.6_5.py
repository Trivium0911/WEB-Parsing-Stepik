"""
                                4.6 Сохраняем результат в Excel 5

Напишите код который собирает данные со всех страниц и категорий на сайте тренажере
(http://parsinger.ru/html/index4_page_1.html) и сохраните всё в таблицу.


Заголовки :  Указывать не нужно
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
    url = 'http://parsinger.ru/html/index1_page_1.html'
    soup = get_soup(url)
    navigation = get_list_with_links(soup, 'div', 'nav_menu')
    for link in navigation:
        soup_link = get_soup(link)
        pagen = get_list_with_links(soup_link, 'div', 'pagen')
        for page in pagen:
            soup_page = get_soup(page)
            name = [x.text.strip() for x in soup_page.find_all('a', class_='name_item')]
            description = [x.text.strip() for x in soup_page.find_all('div', class_='description')]
            price = [x.text for x in soup_page.find_all('p', class_='price')]
            inf = zip(name, description, price)
            for item, descr, price in inf:
                flatten = item, descr.replace("\n", '. '), price
                res = []
                for x in flatten:
                    res.append(x)
                writer = csv.writer(file, delimiter=';')
                writer.writerow(res)

