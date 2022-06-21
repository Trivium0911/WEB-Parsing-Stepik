"""
                            7.4 Парсим данные участников группы 1

Получить список всех участников группы;
Извлечь у каждого подписчика first_name и last_name;
Вставьте полученный список в поле для ответа.
Ожидаемый список:

['first_name last_name', 'first_name last_name', ..... first_name last_name']

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
    res.append(f"{i.first_name} {i.last_name}")

print(res)
