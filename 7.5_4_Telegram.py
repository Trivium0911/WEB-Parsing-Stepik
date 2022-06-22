"""
                                7.5 Парсим сообщения группы 4

Цель: собрать username всех пользователей которые отправили числовое сообщение в
группу (https://t.me/Parsinger_Telethon_Test);
Создать список из этих username;
Вставить полученный список в поле для ответа


Ожидаемый список (символ @ добавлять к username не нужно), в списке может быть только 1 username пользователя.
Если у пользователя отсутствует username, исключить его из списка:

[username, username, ..., username]

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
            user = client.get_entity(message.from_id.user_id)
            if user.username and user.username not in res:
                res.append(user.username)
print(res)
