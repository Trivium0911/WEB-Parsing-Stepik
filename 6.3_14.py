"""
                                    6.3 Поиск элементов Selenium 14
Откройте сайт при помощи selenium (http://parsinger.ru/selenium/6/6.html);
Решите уравнение на странице;
Найдите и выберите в  выпадающем списке элемент с числом, которое у вас получилось после решения уравнения;
Нажмите на кнопку;
Скопируйте число и вставьте в поле ответа.

"""



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/7/7.html')
    res = 12434107696 * 3 * 2 + 1
    if str(res) in [i.text for i in browser.find_elements(By.TAG_NAME, "option")]:
        browser.find_element(By.PARTIAL_LINK_TEXT, str(res)).click()
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(20)
    print(browser.find_element(By.ID, "result").text)
