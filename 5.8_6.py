"""
                                    5.8 Ожидания явные и неявные 6
В этой задаче используйте метод presence_of_element_located(locator) который проверяет наличие элемента в DOM.

Откройте сайт (http://parsinger.ru/expectations/5/index.html) при помощи Selenium;
На сайте есть кнопка, поведение которой вам знакомо;
После нажатие на кнопку, на странице начнётся создание элементов class с рандомными значениями;
Ваша задача применить метод, чтобы он вернул содержимое элемента с классом "BMH21YY", когда он появится на странице;
Полученное значение вставить в поле для ответа.
ps. Вы конечно можете и в ручную найти элемент с этим классом, но кого вы обманите?


"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/5/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    print(WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "BMH21YY"))).text)

