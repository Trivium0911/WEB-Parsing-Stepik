"""
                Напишите код который собирает данные в каждой категории c каждой карточки
                (http://parsinger.ru/html/index1_page_1.html), всего их 160.

Обязательные Заголовки :  Наименование, Артикул, Бренд, Модель, Наличие, Цена, Старая цена, Ссылка на карточку с товаром,

Перечисленные заголовки являются общими для всех карточек.


"""


# import csv
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_soup(url):
#     response = requests.get(url)
#     response.encoding = 'utf-8-sig'
#     return BeautifulSoup(response.text, 'lxml')
#
#
# def get_list_with_links(linktext, elem, classname):
#     shema = 'http://parsinger.ru/html/'
#     return [f"{shema}{link['href']}" for link in linktext.find(elem, class_=classname).find_all('a')]
#
#
# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     lst = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие',
#            'Цена', 'Старая цена', 'Ссылка на карточку с товаром']
#     writer.writerow(lst)
#     start_url = 'http://parsinger.ru/html/index1_page_1.html'
#     soup = get_soup(start_url)
#     navi_links = get_list_with_links(soup,  'div', 'nav_menu')
#     for navi_link in navi_links:
#         soup_link = get_soup(navi_link)
#         pagen = get_list_with_links(soup_link, 'div', 'pagen')
#         for page in pagen:
#             soup_page = get_soup(page)
#             goods_links = [f"http://parsinger.ru/html/{link['href']}"
#                            for link in soup_page.find_all('a', class_="name_item")]
#             for product_link in goods_links:
#                 product_page = get_soup(product_link)
#                 description = [x.text.strip().split("\n") for x in product_page.find_all('div', class_='description')]
#                 res = []
#                 for i in description:
#                     for j in i:
#                         if ": " in j and j.split(": ")[0] in lst or "В наличии" in j:
#                             res.append(j.split(": ")[1])
#                         elif j == '' or j == 'Купить' or (": " in j and j.split(": ")[0] not in lst):
#                             continue
#                         else:
#                             res.append(j)
#                 res.append(product_link)
#                 writer.writerow(res)

# ------ 1. Импортируем необходимые бибилотеки ------
import requests
import csv
from bs4 import BeautifulSoup

# ------ 2. Получаем количество категорий и страниц из пагинации ------
URL = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=URL)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pages = int(soup.find('div', class_='pagen').find_all('a')[-1].text)
categories = len(soup.find('div', class_='nav_menu').find_all('a'))

# ------ 3. Собираем список всех ссылок на все товары ------
link_items = []
for category in range(1, categories + 1):
    for page in range(1,pages + 1):
        url = f'http://parsinger.ru/html/index{category}_page_{page}.html'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'lxml')
        shema = 'http://parsinger.ru/html/'
        items_on_page = soup.find_all('div', class_='sale_button')
        link_items.extend([shema + link.find('a').get('href') for link in items_on_page])

# ------ 4. Собираем список с вложенными словарями с информацией по всем товарам ------
all_items_info = []
for link in link_items:
    response = requests.get(url=link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    all_items_info.append({
        'Наименование': soup.find('p', id='p_header').text.strip(),
        'Артикул': "".join(soup.find('p', class_='article').text.strip().split(": ")[-1]),
        'Бренд': "".join(soup.find('li', id='brand').text.strip().split(": ")[1:]),
        'Модель': "".join(soup.find('li', id='model').text.strip().split(": ")[1:]),
        'Наличие': "".join(soup.find('span', id='in_stock').text.strip().split(": ")[-1]),
        'Цена': soup.find('span', id='price').text.strip(),
        'Старая цена': soup.find('span', id='old_price').text.strip(),
        'Ссылка на карточку с товаром': link
    })

# ------ 5. Все записываем в файл, обращаясь по индексу в словаре ------
columns_name = ['Наименование', 'Артикул', 'Бренд', 'Модель',
                'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром']
with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(columns_name)
    for item in all_items_info:
        writer.writerow([
            item['Наименование'], item['Артикул'], item['Бренд'], item['Модель'],
            item['Наличие'], item['Цена'], item['Старая цена'], item['Ссылка на карточку с товаром']
        ])