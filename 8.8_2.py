"""
                            8.8 Приготовление асинхронного супа 2

Откройте сайт (https://parsinger.ru/asyncio/create_soup/1/index.html), там есть 500 ссылок, секретный код лежит только
на четырёх из них;
Напишите асинхронный код, который найдёт все четыре кода и суммирует их;
Суммируйте все полученный цифры и вставьте результат в поле для ответа:
"""
import sys
import time
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import requests

result = []
all_link = []


def find_good_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    shema = 'https://parsinger.ru/asyncio/create_soup/1/'
    [all_link.append(shema + x['href']) for x in soup.find_all('a')]



async def main(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            if response.ok:
                soup = BeautifulSoup(await response.text(), 'lxml')
                result.append(int(soup.find('p', class_='text').text))


if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    policy = asyncio.WindowsSelectorEventLoopPolicy()
    asyncio.set_event_loop_policy(policy)
url = 'https://parsinger.ru/asyncio/create_soup/1/index.html'
find_good_url(url)
start = time.perf_counter()
task = [main(url) for url in all_link]
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(asyncio.wait(task))
print(sum(result))
