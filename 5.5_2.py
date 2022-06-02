"""
                                5.5 Методы Selenium 2
Откройте сайт (https://parsinger.ru/methods/1/index.html) с помощью Selenium;
При обновлении сайта, в id="result" появится число;
Обновить страницу возможно придется много раз, т.к. число появляется не часто;
Вставьте полученный результат в поле для овтета:

"""

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    while True:
        browser.refresh()
        res = browser.find_element(By.ID, "result").text
        if res.isdigit():
            break
print(res)
