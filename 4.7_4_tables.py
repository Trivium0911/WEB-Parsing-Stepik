"""
                                    4.7 Парсинг табличных данных 4

На  сайте (https://parsinger.ru/table/3/index.html) расположена таблица;
Цель: Собрать числа с 1го столбца и суммировать их;
Полученный результат вставить в поле ответа.

"""

# with bs4
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://parsinger.ru/table/3/index.html').text, 'lxml')
res = [float(i.text) for i in soup.find_all('td') if i.find('b')]
print(sum(res))


# with Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/table/3/index.html')
    res = [float(i.text) for i in browser.find_elements(By.TAG_NAME, "b")]
print(sum(res))
