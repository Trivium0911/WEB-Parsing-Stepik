"""
                                    7.5 Парсим сообщения группы 5

Скачайте все изображения из группы;
Определите общий размер всех фотографий(40шт);
Вставьте полученное число в поле для ответа(число должно быть в байтах, в числе должны отсутствовать пробелы).

"""


from telethon import TelegramClient, events, sync, connection
import os

from telethon.tl.types import InputMessagesFilterPhotos

r_api = int(os.getenv("api_id"))
r_hash = os.getenv("api_hash")
folder_address = os.getenv("folder_address")
with TelegramClient('my', r_api, r_hash) as client:
    all_messages = client.get_messages('t.me/Parsinger_Telethon_Test', filter=InputMessagesFilterPhotos, limit=40)
    for message in all_messages:
        client.download_media(message, file=folder_address)

