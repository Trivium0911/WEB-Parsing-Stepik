"""
                                6.4 Скроллинг страниц 10
Для скроллинга окна используйте .scroll(0,0,0,0) , где координаты это позиция курсора, который должен быть поверх окна.
Откройте сайт (http://parsinger.ru/infiniti_scroll_2/) с помощью Selenium;
На сайте есть список из 100 элементов, которые генерируются при скроллинге;
Необходимо прокрутить окно в самый низ;
Цель: получить все значение в элементах, сложить их;
Получившийся результат вставить в поле ответа.


"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    url = 'http://parsinger.ru/infiniti_scroll_2/'
    browser.get(url)
    browser.set_window_size(1920, 1080)
    action = ActionChains(browser)
    while True:
        action.scroll(800, 400, 800, 400).perform()
        time.sleep(1)
        break_list = [x.get_attribute('class') for x in browser.find_elements(By.TAG_NAME, 'p')]
        if 'last-of-list' in break_list:
            break
    res = [int(x.text) for x in browser.find_elements(By.TAG_NAME, 'p') if x.text]
    print(sum(res))