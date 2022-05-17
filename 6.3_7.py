"""
                                        6.3 Поиск элементов Selenium
Суть задачи проста( у вас будет всего 5 секунд для того чтобы получить результат, поэтому подумайте над кодом)

Открыть сайт (http://parsinger.ru/selenium/1/1.html) с помощью selenium;
Заполнить все существующие поля;
Нажмите на кнопку кнопку;
Скопируйте результат который появится рядом с кнопкой в случае если вы уложились в 5 секунд;
Вставьте результат в поле ниже.
Для заполнения полей вам потребуется метод .send_keys("Текст"), который мы применяем к каждому полю input, помните про универсальный метод .find_elements(), который возвращает список найденных элементов. Используйте этот метод для поиска всех полей.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://stepik-parsing.ru/selenium/1/1.html')
    input_form = browser.find_element(By.CLASS_NAME, 'form').send_keys('Text')
    time.sleep(5)
Для решения задачи используйте цикл,
чтобы обойти найденные элементы, методом .find_elements(),
и на каждой итерации к каждому полю применяйте метод .send_keys("text") для его заполнения,
а метод .click() используйте чтобы нажать на кнопку. Не забудьте про модуль time чтобы установить задержки.

"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/1/1.html')
    for field in browser.find_elements(By.CLASS_NAME, 'form'):
        field.send_keys('beer')
    time.sleep(2)
    browser.find_element(By.ID, "btn").click()
    time.sleep(10)
