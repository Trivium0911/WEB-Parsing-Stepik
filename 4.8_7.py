"""
                            4.8 Сохраняем результат в Excel 7
Напишите код который собирает данные в каждой категории c каждой карточки
(http://parsinger.ru/html/index1_page_1.html), всего их 160.

Обязательные Заголовки :  Наименование, Артикул, Бренд, Модель, Наличие, Цена, Старая цена, Ссылка на карточку с товаром,

Перечисленные заголовки являются общими для всех карточек.


"""


import csv
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8-sig'
    return BeautifulSoup(response.text, 'lxml')


def get_list_with_links(shema, linktext, elem, classname):
    return [f"{shema}{link['href']}" for link in linktext.find(elem, class_=classname).find_all('a')]


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    shema = 'http://parsinger.ru/html/'
    lst = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие',
           'Цена', 'Старая цена', 'Ссылка на карточку с товаром']
    writer.writerow(lst)
    start_url = 'http://parsinger.ru/html/index1_page_1.html'
    soup = get_soup(start_url)
    navi_links = get_list_with_links(shema, soup, 'div', 'nav_menu')
    for navi_link in navi_links:
        soup_link = get_soup(navi_link)
        pagen = get_list_with_links(shema, soup_link, 'div', 'pagen')
        for page in pagen:
            soup_page = get_soup(page)
            goods_links = [f"{shema}{link['href']}" for link in soup_page.find_all('a', class_="name_item")]
            for product_link in goods_links:
                product_page = get_soup(product_link)
                description = [x.text.strip().split("\n") for x in product_page.find_all('div', class_='description')]
                res = []
                for i in description:
                    for j in i:
                        if ": " in j and j.split(": ")[0] in lst or "В наличии" in j:
                            res.append(j.split(": ")[1])
                        elif j == '' or j == 'Купить' or (": " in j and j.split(": ")[0] not in lst):
                            continue
                        else:
                            res.append(j)
                res.append(product_link)
                writer.writerow(res)

