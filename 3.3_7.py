"""
                                            3.3 Метод requests.get() 7
Задача:

Перейдите на сайт (http://parsinger.ru/video_downloads/)
Скачайте видео с сайта  при помощи requests
Определите его размер в ручную
Напишите размер файла в поле для ответа. Написать нужно только цифру в мб.


"""


import os
import requests


resp = requests.get('http://parsinger.ru/video_downloads/videoplayback.mp4', stream=True)
with open('file.mp4', 'wb') as file:
    file.write(resp.content)
print(os.path.getsize("file.mp4") // 10**6)