"""
                                    8.8 Приготовление асинхронного супа 1
Откройте сайт тренажёр https://parsinger.ru/html/index1_page_1.htm;
Напишите асинхронный код, который обработает все карточки(160шт);
Необходимо вычислить общий размер скидки для всех товаров в рублях;
https://ucarecdn.com/03fcb9a4-5a2d-4481-b46a-5c8a862759fa/
Вставьте полученное значение в поле для ответа:
"""


import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup

category_lst = []
pagen_lst = []
domain = 'https://parsinger.ru/html/'
res = []


def get_soup(url):
    resp = requests.get(url=url)
    return BeautifulSoup(resp.text, 'lxml')


def get_urls_categories(soup):
    all_link = soup.find('div', class_='nav_menu').find_all('a')

    for cat in all_link:
        category_lst.append(domain + cat['href'])


def get_urls_pages(category_lst):
    for cat in category_lst:
        resp = requests.get(url=cat)
        soup = BeautifulSoup(resp.text, 'lxml')
        for pagen in soup.find('div', class_='pagen').find_all('a'):
            pagen_lst.append(domain + pagen['href'])


async def get_data(session, link):

    async with session.get(url=link) as response:
        resp = await response.text()
        soup = BeautifulSoup(resp, 'lxml')
        item_card = [x['href'] for x in soup.find_all('a',
                                                      class_='name_item')]
        for x in item_card:
            url2 = domain + x
            async with session.get(url=url2) as response2:
                resp2 = await response2.text()
                soup2 = BeautifulSoup(resp2, 'lxml')
                count = int(soup2.find('span', id='in_stock').text.split()[2])
                old_price = int(soup2.find('span', id='old_price').text.
                                split()[0])
                price = int(soup2.find('span', id='price').text.split()[0])
                res.append((old_price - price) * count)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in pagen_lst:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


url = 'https://parsinger.ru/html/index1_page_1.html'
soup = get_soup(url)
get_urls_categories(soup)
get_urls_pages(category_lst)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

print(sum(res))
