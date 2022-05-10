"""
                                             4.5 Пагинация 4
1. Открываем сайт http://parsinger.ru/html/index3_page_4.html
2. Проходимся по всем страницам в категории мыши (всего  4 страницы)
3. На каждой странице посещаем каждую карточку с товаром (всего 32 товаров)
4. В каждой карточке извлекаем при помощи bs4 артикул <p class="article"> Артикул: 80244813 </p>
5. Складываем(плюсуем) все собранные значения
6. Вставляем получившийся результат в поле ответа
"""

import requests
from bs4 import BeautifulSoup

url = 'http://parsinger.ru/html/index3_page_4.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'
pagen = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
res = []
for link in pagen:
    resp = requests.get(url=link)
    resp.encoding = 'utf-8'
    soup_link = BeautifulSoup(resp.text, 'lxml')
    pagen_product = [f"{shema}{i['href']}" for i in soup_link.find_all("a", class_='name_item')]
    for link_product in pagen_product:
        resp_product = requests.get(url=link_product)
        resp_product.encoding = 'utf-8'
        sp_product = BeautifulSoup(resp_product.text, 'lxml')
        res.append(int(sp_product.find('p', class_='article').text.replace("Артикул: ", '')))

print(sum(res))