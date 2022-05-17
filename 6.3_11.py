"""
                                    6.3 Поиск элементов Selenium 11
Откройте сайт (http://parsinger.ru/selenium/4/4.html);
Установите все чек боксы в положение checked при помощи selenium и метода click();
Когда все чек боксы станут активны, нажмите на кнопку;
Скопируйте число которое появится на странице;
Результат появится в <p id="result">Result</p>;
Вставьте число в поле для ответа.
"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/4/4.html')
    for elem in browser.find_elements(By.CLASS_NAME, "check"):
        elem.click()
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(2)
    print(browser.find_element(By.ID,"result").text)