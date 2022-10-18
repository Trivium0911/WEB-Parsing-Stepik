"""
                                        8.9 aiofile  2

Глубина парсинга уровень 2
Откройте сайт (https://parsinger.ru/asyncio/aiofile/3/index.html), на нём есть 100 ссылок, в каждой из них есть ещё
10 ссылок, в каждой из 10 ссылок есть 8-10 изображений, структура как на картинке ниже;
https://ucarecdn.com/1efc13c5-fc22-4725-b5e7-245bbb71d133/
Ваша задача: Написать асинхронный код который скачает все уникальные изображения которые там есть (они повторяются, в
это задании вам придётся скачать 2615 изображений) ;
Вставьте размер всех скачанных изображений в поле для ответа;
Асинхронный код должен обработать все ссылки и скачать все изображения примерно за 180-200 сек, скорость зависит от
скорости вашего интернет соединения.

Воспользуйтесь функцией ниже, для получения размера всех файлов в папке. Функция на вход принимает путь к папке с
изображениями filepath="/img/"

def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size
"""

import time
import aiofiles
import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
import os


all_links = []
shema2 = 'https://parsinger.ru/asyncio/aiofile/3/depth2/'
shema = 'https://parsinger.ru/asyncio/aiofile/3/'


async def write_file(session, url, name_img):
    async with aiofiles.open(f'sync_save_files/{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for file in response.content.iter_chunked(2048):
                await f.write(file)
        print(f'Изображение сохранено {name_img}')


def find_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = [shema + x['href'] for x in soup.find_all('a')]
    for i in links:
        resp = requests.get(i)
        soup2 = BeautifulSoup(resp.text, 'lxml')
        all_links.extend([shema2 + x['href'] for x in soup2.find_all('a')])


async def main(url):

    async def eternity():
        await asyncio.sleep(60)
        print('yay!')

    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

    async with aiohttp.ClientSession() as session:

            async with session.get(url) as response:
                all_url_image = []
                soup = BeautifulSoup(await response.text(), 'lxml')
                all_url_image.extend(
                [x['src'] for x in
                    soup.find_all(class_='picture')])
            tasks = []
            for link in all_url_image:
                name_img = link.split('/')[6]
                if not os.path.exists(f'sync_save_files/{name_img}'):
                    task = asyncio.create_task(write_file(session,
                                                          link, name_img))
                    tasks.append(task)
            await asyncio.gather(*tasks)


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


path = 'sync_save_files/'
start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
url = 'https://parsinger.ru/asyncio/aiofile/3/index.html'
find_urls(url)
for link in reversed(all_links):
    asyncio.run(main(link))

print(f'Размер всех изображений {get_folder_size(path)} byte')

