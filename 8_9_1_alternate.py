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


import time
import aiofiles
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os



async def write_file(session, url, name_img):
    async with aiofiles.open(f'img/{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for file in response.content.iter_chunked(2048):
                await f.write(file)
        print(f'Изображение сохранено {name_img}')


async def main(url):
    schema = 'https://parsinger.ru/asyncio/aiofile/2/'

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
            all_page = [schema + x['href'] for x in soup.find_all('a')]
            all_url_image = []
            for x in all_page:
                async with session.get(x) as response2:
                    soup2 = BeautifulSoup(await response2.text(), 'lxml')
                    all_url_image.extend([x['src'] for x in soup2.find_all('img')])
            tasks = []
            for link in all_url_image:
                name_img = link.split('/')[6]
                task = asyncio.create_task(write_file(session, link, name_img))
                tasks.append(task)
            await asyncio.gather(*tasks)


path = 'img/'
start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
url = 'https://parsinger.ru/asyncio/aiofile/2/index.html'
try:
    asyncio.run(main(url))
except:
    asyncio.run(main(url))


print(f'Cохранено {len(os.listdir(path))} изображений за {round(time.perf_counter() - start, 3)} сек')


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


print(f'Размер всех изображений {get_folder_size(path)} byte')
