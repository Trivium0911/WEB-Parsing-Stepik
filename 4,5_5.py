"""
                                      4.5 Пагинация 5


1. Открываем сайт http://parsinger.ru/html/index1_page_1.html
2. Проходимся по всем категориям, страницам и карточкам с товарами(всего 160шт)
3. Собираем с каждой карточки стоимость товара умножая на количество товара в наличии
4. Складываем получившийся результат
5. Получившуюся цифру с общей стоимостью всех товаров вставляем в поле ответа.

"""

import requests
from bs4 import BeautifulSoup

url = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'
goods_navigation = [f"{shema}{link['href']}" for link in soup.find('div', class_='nav_menu').find_all('a')]
res = []
for good in goods_navigation:
    resp_navi = requests.get(url=good)
    resp_navi.encoding = 'utf-8'
    soup_goods = BeautifulSoup(resp_navi.text, 'lxml')
    pagen = [f"{shema}{link['href']}" for link in soup_goods.find('div', class_='pagen').find_all('a')]
    for link in pagen:
        resp = requests.get(url=link)
        resp.encoding = 'utf-8'
        soup_link = BeautifulSoup(resp.text, 'lxml')
        pagen_product = [f"{shema}{i['href']}" for i in soup_link.find_all("a", class_='name_item')]
        for link_product in pagen_product:
            resp_product = requests.get(url=link_product)
            resp_product.encoding = 'utf-8'
            sp_product = BeautifulSoup(resp_product.text, 'lxml')
            count = int(sp_product.find('span', id='in_stock').text.replace("В наличии: ", ''))
            price = int(sp_product.find('span', id='price').text.replace(" руб", ''))
            res.append(price * count)
print(sum(res))