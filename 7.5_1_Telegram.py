"""
                                7.5 Парсим сообщения группы 1

Спарсить числовые значения из сообщений в группе (https://t.me/Parsinger_Telethon_Test);
Суммировать полученные числа и вставить результат в поле для ответа.

"""


from telethon import TelegramClient, events, sync, connection
import os

r_api = int(os.getenv("api_id"))
r_hash = os.getenv("api_hash")
res = []
with TelegramClient('my', r_api, r_hash) as client:
    all_messages = client.iter_messages('t.me/Parsinger_Telethon_Test')
    for message in all_messages:
        if message.message and int(message.message):
            res.append(int(message.text))
print(sum(res))
