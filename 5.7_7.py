"""
                                    5.6 Окна и вкладки 7
Откройте сайт (http://parsinger.ru/window_size/2/index.html) с помощи selenium;
У вас есть 2 списка с размерами  size_x и size_y;
При сочетании размеров из этих списков, появится число;
Результат появится в id="result";
Скопируйте результат в поле для ответа.
ps. При написании кода, учитывайте размер рамок браузера.

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

sizes_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
sizes_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/2/index.html')
    for x in sizes_x:
        for y in sizes_y:
            browser.set_window_size(x, y)
            real_x = browser.find_element(By.ID, "width").text.split(": ")[1]
            real_y = browser.find_element(By.ID, "height").text.split(": ")[1]
            res_x, res_y = abs(x + (x - int(real_x))), abs(y + (y - int(real_y)))
            browser.set_window_size(res_x, res_y)
            res = browser.find_element(By.ID, 'result')
            time.sleep(.1)
            print(res.text) if res else None
