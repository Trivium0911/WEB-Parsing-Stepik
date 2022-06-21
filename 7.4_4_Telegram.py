"""
                                7.4 Парсим данные участников группы 4

Скачайте полноразмерные аватарки всех участников группы включая все сохранённые аварки;
Встроенными методами windows узнайте общий размер всех аватарок(74шт);
Полученное число в байтах вставьте в поля для ответа.

"""


from telethon import TelegramClient, events, sync, connection
import os

r_api = int(os.getenv("api_id"))
r_hash = os.getenv("api_hash")
folder_address = os.getenv("folder_address")
with TelegramClient('my', r_api, r_hash) as client:
    all_user_group = client.get_participants('t.me/Parsinger_Telethon_Test')
    for user in all_user_group:
        for iter_photo in client.iter_profile_photos(user):
            client.download_media(iter_photo, file=folder_address)


