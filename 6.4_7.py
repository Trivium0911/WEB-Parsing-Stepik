"""
                                        6.4 Скроллинг страниц 7
Откройте сайт с помощью Selenium;
На сайте есть 100 чекбоксов, 25 из них вернут число;
Ваша задача суммировать все появившиеся числа;
Отправить получившийся результат в поля ответа.

"""


import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/2/index.html')
    browser.find_element(By.ID, "details-button").click()      # "Подключение не защищено"
    browser.find_element(By.ID, "proceed-link").click()
    time.sleep(1)
    res = []
    for input_tag in browser.find_elements(By.TAG_NAME, 'input'):
        input_tag.send_keys(Keys.DOWN)
        input_tag.click()
        elem_id = input_tag.get_attribute("id")
        ans = browser.find_element(By.ID, f"result{elem_id}")
        if ans.text != '':
                res.append(int(ans.text))
print(sum(res))
