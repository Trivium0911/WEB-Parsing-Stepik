"""
                                    5.6 Окна и вкладки 6
Откройте сайт (http://parsinger.ru/window_size/1/) с помощью selenium;
Необходимо открыть окно таким размером, чтобы рабочая область страницы составляла 555px на 555px;
Учитывайте размеры границ браузера;
Результат появится в id="result";
Вставьте полученный результат в поле для ответа.

"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/1/')
    browser.set_window_size(555 + 13, 555 + 131)
    res = browser.find_element(By.ID, 'result')
    time.sleep(5)
    print(res.text) if res else None
