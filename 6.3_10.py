"""
                                        6.3 Поиск элементов Selenium
Откройте сайт (http://parsinger.ru/selenium/3/3.html);
Извлеките данные из каждого  второго тега <p>;
Сложите все значения, их всего 100 шт;
Напишите получившийся результат в поле ответа.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    elems = browser.find_elements(By.XPATH, "/html/body/div/div/p[2]")
    print(sum([int(i.text) for i in elems]))
