"""
                                                    8.9 aiofile  1

Глубина парсинга уровень 1
Откройте сайт (https://parsinger.ru/asyncio/aiofile/2/index.html), на нём есть 50 ссылок, в каждой ссылке лежит
по 10 изображений;
Ваша задача: Написать асинхронный код который скачает все уникальные изображения которые там есть (они повторяются,
а уникальных всего 454) ;
Вставьте размер всех скачанных изображений в поле для ответа;
Асинхронный код должен обработать все ссылки и скачать все изображения примерно за 20-30 сек, скорость зависит от
скорости вашего интернет соединения.

Воспользуйтесь функцией ниже, для получения размера всех файлов в папке. Функция на вход принимает путь к папке с
изображениями filepath="/img/"

def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size
"""
import asyncio
import os
import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup


all_links = []
shema = 'https://parsinger.ru/asyncio/aiofile/2/'


async def main(url):
    count = 0

    async def eternity():
        await asyncio.sleep(60)
        print('yay!')

    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            soup = BeautifulSoup(await response.text(), 'lxml')
            img_urls = [f'{x["src"]}' for x in soup.find_all('img')]
            tasks = []

            for link_img in img_urls:
                img_name = f"{link_img.split('/')[6]}"
                if not os.path.exists(f'images/path'):
                    task = asyncio.create_task(write_file(session,
                                                          link_img, img_name))
                    tasks.append(task)
            await asyncio.gather(*tasks)
            await asyncio.wait_for(eternity(), timeout=1.0)


async def write_file(session, url, name_img):
    async with aiofiles.open(f'images/{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await f.write(x)
        print(f'Изображение сохранено {name_img}')


def find_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    [all_links.append(shema + x['href']) for x in soup.find_all('a')]


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


url = 'https://parsinger.ru/asyncio/aiofile/2/index.html'
find_urls(url)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
for link in all_links:
    try:
        asyncio.run(main(link))
    except asyncio.TimeoutError:
        print('timeout!')
        continue

print(get_folder_size('/images/'))
