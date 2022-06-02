"""

Для этой задачи потребуется код с прошлого степа.

Откройте сайт (http://parsinger.ru/window_size/2/index.html) с помощи selenium;
У вас есть 2 списка с размера окон size_x и size_y;
Цель: определить размер окна, при котором,  в id="result" появляется число;
Результат должен быть в виде словаря {'width': size_x, 'height': size_y}
ps. При написании кода, учитывайте размер рамок браузера.

Размеры рамок могут зависеть от вашего разрешения и масштабирования экрана. Задача составлена при 100% масштабировании, масштабирование можно проверить в настройках дисплея.

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
            if res. text:
                print(browser.get_window_size())
                print(res.text)
                break

