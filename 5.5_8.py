"""
                                    5.5 Методы Selenium 8
Откройте сайт (https://parsinger.ru/methods/5/index.html) с помощью Selenium;
На сайте есть 42 ссылки, у каждого сайта по ссылки есть cookie с определёнными сроком жизни;
Цель: написать скрипт, который сможет найти среди всех ссылок страницу с самым длинным сроком жизни cookie и получить с этой странице число;
Вставить число в поле для ответа.

"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

res = ''
dct = {}
with webdriver.Chrome() as browser:
    main_url = 'https://parsinger.ru/methods/5/'
    browser.get(f'{main_url}index.html')
    time.sleep(.2)
    for i in range(1, 43):
        browser.get(f"{main_url}{i}.html")
        time.sleep(.2)
        cookies = browser.get_cookies()
        expiry = int(cookies[0]['expiry'])
        dct[f"{main_url}{i}.html"] = expiry
        browser.back()

    for k, v in dct.items():
        if v == max(dct.values()):
            browser.get(k)
            print(browser.find_element(By.ID, "result").text)

