"""
                                7.5 Парсим сообщения группы 3
В группе (https://t.me/Parsinger_Telethon_Test) пользователь с user_id=5339026159 оставил несколько цифровых
сообщений;
Цель: Определить участника с указанным user_id и получить его сообщения и суммировать их;
Полученное число вставьте в поле для ответа.
"""


from telethon import TelegramClient, events, sync, connection
import os

r_api = int(os.getenv("api_id"))
r_hash = os.getenv("api_hash")
res = []
chk_id = 5339026159
with TelegramClient('my', r_api, r_hash) as client:
    all_messages = client.iter_messages('t.me/Parsinger_Telethon_Test', from_user=chk_id)
    for message in all_messages:
        if message.message:
            res.append(int(message.message))

print(sum(res))