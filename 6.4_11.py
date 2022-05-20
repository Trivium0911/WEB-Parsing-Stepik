"""
                                    6.4 Скроллинг страниц 11
Откройте сайт (http://parsinger.ru/infiniti_scroll_3/) с помощью Selenium
На сайте есть 5 окошек с подгружаемыми элементами, в каждом по 100 элементов;
Необходимо прокрутить все окна в самый низ;
Цель: получить все значение в каждом из окошек и сложить их;
Получившийся результат вставить в поле ответа.
Оптимальное время выполнения скрипта 11 сек

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    url = 'http://parsinger.ru/infiniti_scroll_3/'
    browser.get(url)
    browser.set_window_size(1024, 720)
    action = ActionChains(browser)
    last_elem = browser.find_element(By.ID, 'scroll-container_5')
    res = []
    while True:
        action.scroll(85, 275, 85, 275).perform()
        action.scroll(280, 300, 280, 300).perform()
        action.scroll(480, 300, 480, 300).perform()
        action.scroll(680, 320, 680, 320).perform()
        action.scroll(900, 300, 900, 300).perform()
        break_list = [i.get_attribute('class') for i in last_elem.find_elements(By.TAG_NAME, 'span')]
        if 'last-of-list' in break_list:
            [res.append(int(x.text)) for x in
             browser.find_element(By.CLASS_NAME, 'main').find_elements(By.TAG_NAME, 'span')]
            break

print(sum(res))
