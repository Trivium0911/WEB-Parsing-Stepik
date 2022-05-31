"""
                                    5.6 Окна и вкладки 2

Откройте сайт (http://parsinger.ru/blank/modal/2/index.html) при помощи Selenium;
На сайте есть 100 buttons;
При нажатии на одну из кнопок в  теге <p id="result">Code</p> появится код;
Вставьте секретный код в поле для ответа.

"""


from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/2/index.html')
    res_elem = browser.find_element(By.ID, "result")
    res = 0
    for button in browser.find_elements(By.CLASS_NAME, "buttons"):
        button.click()
        alert = browser.switch_to.alert
        alert.accept()
        if browser.find_element(By.ID, "result").text:
            res = int(res_elem.text)
print(res)
