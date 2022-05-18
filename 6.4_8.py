"""
                                    6.4 Скроллинг страниц 8
Откройте сайт сайт (https://parsinger.ru/scroll/3/) с помощью Selenium;
Ваша задача, получить числовое значение  id="число" с каждого тега <input> который при нажатии вернул число;
Суммируйте все значения и отправьте результат в поле ниже.


На целевом сайте 300 тегов. Чтобы сэкономить вам время, мы позаботились о мини версии
сайта (https://parsinger.ru/scroll/training_task_3/), на нём всего 10 тегов.
При правильном решении задачи, на тестовом сайте получившийся результат  будет равен 18

"""

import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/3/')
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
            res.append(int(elem_id))
print(sum(res))
