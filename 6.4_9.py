"""
                                6.4 Скроллинг страниц 9
Откройте сайт (http://parsinger.ru/infiniti_scroll_1/) с помощью Selenium;
На сайте есть список из 100 элементов, которые генерируются при скроллинге;
В списке есть интерактивные элементы, по которым можно осуществить скроллинг вниз;
Используйте Keys.DOWN или .move_to_element();
Цель: получить все значение в элементах, сложить их;
Получившийся результат вставить в поле ответа.
Подсказка:

Элементы могут грузится медленнее чем работает ваш код, установите задержки.

Подумайте над условием прерывания цикла, последний элемент в списке имеет class="last-of-list"

"""


import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/infiniti_scroll_1/')
    time.sleep(0.5)
    count = 0
    res = []
    check_lst = []
    while True:
        inps = [i for i in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'input')]
        for inp in inps:
            if inp not in check_lst:
                time.sleep(2)
                inp.click()
                inp.send_keys(Keys.DOWN)
                time.sleep(2)
                count += 1
                check_lst.append(inp)

        spans = [res.append(int(i.text)) for i in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')
                 if int(i.text) not in res]
        breaker = [x for x in browser.find_elements(By.TAG_NAME, 'span') if x.get_attribute('class')]
        if breaker:
            break

print(res)


