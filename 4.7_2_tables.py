"""
                                4.7 Парсинг табличных данных 2
На  сайте (https://parsinger.ru/table/1/index.html) расположена таблица;
Цель: Собрать все уникальные числа из таблицы и суммировать их;
Полученный результат вставить в поле ответа.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/table/1/index.html'
    browser.get(url)
    res = []
    for i in browser.find_elements(By.TAG_NAME, "td"):
        if float(i.text) not in res:
            res.append(float(i.text))
    print(sum(res))
