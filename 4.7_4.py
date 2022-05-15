"""
                                    4.7 Сохраняем результат в JSON 4

Выберите 1 любую категорию на сайте тренажере (http://parsinger.ru/html/index1_page_1.html)
и соберите все данные с карточек.


"""


import requests
from bs4 import BeautifulSoup
import json


def get_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8-sig'
    return BeautifulSoup(response.text, 'lxml')


def get_list_with_links(shema, linktext, elem, classname):
    return [f"{shema}{link['href']}" for link in linktext.find(elem, class_=classname).find_all('a')]


link = 'http://parsinger.ru/html/index3_page_1.html'
shem = 'http://parsinger.ru/html/'
result_json = []
soup = get_soup(link)
page_links = get_list_with_links(shem, soup, 'div', 'pagen')
for page in page_links:
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]
    for list_item, price_item, name in zip(description, price, name):
        result_json.append({
             'name': name,
             'brand': [x.split(':')[1] for x in list_item][0].strip(),
             'type': [x.split(':')[1] for x in list_item][1].strip(),
             'connect': [x.split(':')[1] for x in list_item][2].strip(),
             'game': [x.split(':')[1] for x in list_item][3].strip(),
             'price': price_item

        })


with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
