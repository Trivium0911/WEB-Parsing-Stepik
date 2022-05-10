"""
                                    3.5 Получаем содержимое response объекта 4


1. Перейдите на сайт http://parsinger.ru/img_download/index.html
2. На 1 из 160 картинок написан секретный код
3. Напишите код, который поможет вам скачать все картинки и найти cекретный код
4. Вставьте код в поле для ответа


"""


import requests

for i in range(1, 161):
    response = requests.get(f'http://parsinger.ru/img_download/img/ready/{i}.png')
    with open(f'image{i}.jpeg', 'wb') as file:
        file.write(response.content)