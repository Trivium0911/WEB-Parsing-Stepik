"""
                                        7.5 Парсим сообщения группы 2

В группе есть закреплённое сообщение;
Цель: получить user_id пользователя чьё сообщение закреплено;
Вставить полученный user_id в поле для ответа.

"""


from telethon import TelegramClient, events, sync, connection
import os

r_api = int(os.getenv("api_id"))
r_hash = os.getenv("api_hash")

with TelegramClient('my', r_api, r_hash) as client:
    all_messages = client.iter_messages('t.me/Parsinger_Telethon_Test')
    for message in all_messages:
        if message.pinned:
            print(message.from_id.user_id)

