"""
                                4.9 Сохраняем результат в JSON 6

Выберите 1 любую категорию на сайте тренажёре, и соберите все данные с карточек товаров + ссылка на карточку.
По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.
Ключи в блоке description, должны быть получены автоматически из атрибутов HTML элементов.




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
res_json = []
soup = get_soup(link)
page_links = get_list_with_links(shem, soup, 'div', 'pagen')
count = 2
for page in page_links:
    product_soup = get_soup(page)
    product_links = [f"{shem}{link['href']}" for link in product_soup.find_all('a', class_="name_item")]
    categories = [f"{name['id']}" for name in soup.find('div', class_="nav_menu").find_all('div')]
    for p_link in product_links:
        p_soup = get_soup(p_link)
        name = [x.text.strip() for x in p_soup.find_all('a', class_='name_item')]
        description = [x.text.strip().split("\n") for x in p_soup.find_all('div', class_='description')]
        descr_positions = p_soup.find('ul', id='description').find_all('li')
        for x in description:
            desc = {li['id']: li.text.split(':')[-1].strip() for li in descr_positions}
            res_json.append({
                    'categories': categories[count],
                    'name': x[0].strip(),
                    'article': x[1].split(": ")[1],
                    'description': desc,
                    'count': x[12].split(": ")[1].strip(),
                    'price': x[14].strip(),
                    'old_price': x[15].strip(),
                    'site': p_link
                })

            with open('res.json', 'w', encoding='utf-8') as file:
                json.dump(res_json, file, indent=4, ensure_ascii=False)
