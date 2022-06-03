"""
                            4.9 Сохраняем результат в JSON 7
Соберите данные со всех 5 категорий на сайте тренажере (http://parsinger.ru/html/index1_page_1.html)
и соберите все данные с карточек.
По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.
Ключи в блоке description должны быть получены автоматически из атрибутов HTML элементов.

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


link = 'http://parsinger.ru/html/index1_page_1.html'
shem = 'http://parsinger.ru/html/'
res_json = []
soup = get_soup(link)
navi_links = get_list_with_links(shem, soup, 'div', 'nav_menu')
for goods in navi_links:
    pagen_soup = get_soup(goods)
    page_links = get_list_with_links(shem, pagen_soup, 'div', 'pagen')
    for page in page_links:
        product_soup = get_soup(page)
        product_links = [f"{shem}{link['href']}" for link in product_soup.find_all('a', class_="name_item")]
        for p_link in product_links:
            p_soup = get_soup(p_link)
            descr_positions = p_soup.find('ul', id='description').find_all('li')
            desc = {li['id']: li.text.split(': ')[-1].strip() for li in descr_positions}
            res_json.append({
                    'categories': p_link.split("/")[4],
                    'name': p_soup.find('p', id='p_header').text.strip(),
                    'article': p_soup.find('p', 'article').text.split(':')[1].strip(),
                    'description': desc,
                    'count': p_soup.find('span', id='in_stock').text.split(':')[1].strip(),
                    'price': p_soup.find('span', id='price').text.strip(),
                    'old_price': p_soup.find('span', id='old_price').text.strip(),
                    'link': p_link
                    })

with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(res_json, file, indent=4, ensure_ascii=False)
