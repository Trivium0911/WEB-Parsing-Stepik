"""
                            5.6 Окна и вкладки 3
Откройте сайт (http://parsinger.ru/blank/modal/3/index.html) при помощи Selenium;
На сайте есть 100 buttons;
При нажатии на любую кнопку появляется confirm с пин-кодом;
Текстовое поле под кнопками проверяет правильность пин-кода;
Ваша задача, найти правильный пин-код и получить секретный код;
Вставьте секретный код в поле для ответа.

"""


from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/3/index.html')
    check_btn = browser.find_element(By.ID, "check")
    check_pole = browser.find_element(By.ID, "input")
    res = browser.find_element(By.ID, "result")
    for button in browser.find_elements(By.CLASS_NAME, "buttons"):
        button.click()
        alert = browser.switch_to.alert
        pin = alert.text
        alert.accept()
        check_pole.send_keys(pin)
        check_btn.click()
        if res.text != 'Неверный пин-код':
            print(res.text)
            break

