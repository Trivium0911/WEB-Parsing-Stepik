"""
                        6.3 Поиск элементов Selenium 9
Откройте сайт (http://parsinger.ru/selenium/3/3.html);
Извлеките данные из каждого тега <p>;
Сложите все значения, их всего 300 шт;
Напишите получившийся результат в поле ниже.
"""


from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    elems = browser.find_elements(By.TAG_NAME, 'p')
    print(sum([int(i.text) for i in elems]))
