"""
                            7.4 Парсим данные участников группы 2

Получить данные участников группы;
id
first_name
last_name
phone
Вставьте полученный список в поле для ответа.
Ожидаемый список:

[id first_name last_name phone, id first_name last_name phone,.... id first_name last_name phone]

"""

from telethon import TelegramClient, events, sync, connection
import os

r_api = int(os.getenv("api_id"))
r_hash = os.getenv("api_hash")

client = TelegramClient('session_name2', r_api, r_hash)
client.start()
res = []
participants = client.get_participants('https://t.me/Parsinger_Telethon_Test')
for i in participants:
    res.append(f"{i.id} {i.first_name} {i.last_name} {i.phone}")

print(res)
