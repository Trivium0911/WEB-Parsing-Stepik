"""
                                    5.6 Окна и вкладки 4
Откройте сайт (http://parsinger.ru/blank/modal/4/index.html) при помощи Selenium;
На сайте есть список пин-кодов и только один правильный;
Для проверки пин-кода используйте кнопку "Проверить"
Ваша задача, найти правильный пин-код и получить секретный код;
Вставьте секретный код в поле для ответа.

"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/4/index.html')
    check_btn = browser.find_element(By.ID, "check")
    pins = [i.text for i in browser.find_element(By.CLASS_NAME, 'main').find_elements(By.CLASS_NAME, "pin")]
    for pin in pins:
        check_btn.click()
        promt = browser.switch_to.alert
        time.sleep(.1)
        promt.send_keys(pin)
        promt.accept()
        res = browser.find_element(By.ID, "result").text
        if res.isdigit():
            print(res)
            break
