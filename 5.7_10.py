"""
                                5.7 Окна и вкладки 10
Откройте сайт (http://parsinger.ru/blank/3/index.html) с помощью Selenium;
На сайте есть 10 buttons, каждый button откроет сайт в новой вкладке;
Каждая вкладки имеет в title уникальное число;
Цель - собрать числа с каждой вкладки и суммировать их;
Полученный результат вставить в поле для ответа.
"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    res = []
    browser.get('http://parsinger.ru/blank/3/index.html')
    time.sleep(1)
    for btn in browser.find_elements(By.CLASS_NAME, "buttons"):
        btn.click()
    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(.2)
        title = browser.execute_script("return document.title;")
        if title.isdigit():
            res.append(int(title))
print(sum(res))


