"""
                                    6.3 Поиск элементов Selenium 13
Открываем сайт с помощью selenium (http://parsinger.ru/selenium/7/7.html);
Получаем значения всех элементов выпадающего списка;
Суммируем(плюсуем) все значения;
Вставляем получившийся результат в поле на сайте;
Нажимаем кнопку и копируем длинное число;
Вставляем конечный результат в поле ответа.

"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/7/7.html')
    res = sum([int(elem.text) for elem in browser.find_elements(By.TAG_NAME, "option")])
    browser.find_element(By.ID, "input_result").send_keys(res)
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(2)
    print(browser.find_element(By.ID, "result").text)
