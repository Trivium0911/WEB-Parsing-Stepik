"""
                                            5.8 Ожидания явные и неявные 7
А это задача для тех кто всё таки решил перехитрить прошлую задачу и решил её вручную. А для всех остальных, задача максимально проста, запустить тот же самый код из прошлой задачи, но на другом url и с другим class.

Откройте сайт (http://parsinger.ru/expectations/6/index.html) при помощи Selenium;
На сайте есть кнопка, поведение которой вам знакомо;
После нажатие на кнопку, на странице начнётся создание элементов class с рандомными значениями;
Ваша задача применить метод, чтобы он вернул содержимое элемента с классом "Y1DM2GR" , когда он появится на странице;
Полученное значение вставить в поле для ответа.

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/6/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    print(WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "Y1DM2GR"))).text)
