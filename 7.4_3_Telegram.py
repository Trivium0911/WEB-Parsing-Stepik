"""
                            7.4 Парсим данные участников группы 3

Скачайте полноразмерные аватарки всех участников группы (https://t.me/Parsinger_Telethon_Test);
Встроенными методами windows узнайте общий размер всех аватарок(50шт);
Полученное число в байтах вставьте в поля для ответа.

"""


from telethon import TelegramClient, events, sync, connection
import os

r_api = int(os.getenv("api_id"))
r_hash = os.getenv("api_hash")
folder_address = os.getenv("folder_address")
with TelegramClient('my', r_api, r_hash) as client:
    participants = client.get_participants('t.me/Parsinger_Telethon_Test')
    for i, user in enumerate(participants):
        client.download_profile_photo(user, f'{folder_address}{i}', download_big=True)
