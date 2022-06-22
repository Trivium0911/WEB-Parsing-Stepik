"""
                            7.4 Парсим данные участников группы 6

Есть список lst=[] в котором хранятся username участников группы (https://t.me/Parsinger_Telethon_Test);
Цель собрать числа из поля "О Себе" или "About" пользователя из списка lst=[], затем суммировать все добытые числа;
Полученное число вставить в поле для ответа.
lst = ['daxton_13246', 'Anthony_Alexander534', 'William_Price34', 'Roger_Parks4',
       'Nancy_Montgomery54', 'Melissa_Simmons4', 'Shane_Morris34', 'Gloria_Thompson4',
       'Linda_Hernandez4', 'James_Morton34', 'Constance_Jones4', 'Joshua_Andrews34',
       'Erica_Moore34', 'Timothy_Green3', 'Lisa_Hawkins', 'Nancy_Johnson3', 'Mary_Davis1',
        'Brian_Johnson2', 'Peter_Barnes', 'James_Washington3']

"""

from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest
import os

r_api = int(os.getenv("api_id"))
r_hash = os.getenv("api_hash")

res = []
lst = ['daxton_13246', 'Anthony_Alexander534', 'William_Price34', 'Roger_Parks4',
       'Nancy_Montgomery54', 'Melissa_Simmons4', 'Shane_Morris34', 'Gloria_Thompson4',
       'Linda_Hernandez4', 'James_Morton34', 'Constance_Jones4', 'Joshua_Andrews34',
       'Erica_Moore34', 'Timothy_Green3', 'Lisa_Hawkins', 'Nancy_Johnson3', 'Mary_Davis1',
       'Brian_Johnson2', 'Peter_Barnes', 'James_Washington3']

with TelegramClient('my', r_api, r_hash) as client:
    users = client.iter_participants('t.me/Parsinger_Telethon_Test')
    lst_users = [client(GetFullUserRequest(x)) for x in users if x.username in lst]
    for user in lst_users:
        res.append(int(user.about))
print(sum(res))
