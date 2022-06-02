"""
                                        5.7 Окна и вкладки 11
У вас есть список сайтов, 6 шт;
На каждом сайте есть chekbox, нажав на этот chekbox появится код;
Ваша задача написать скрипт, который открывает при помощи Selenium все сайты во вкладках;
Проходит в цикле по каждой вкладке, нажимает на chekbox и сохранет код;
Из каждого числа, необходимо извлечь корень, функцией sqrt();
Суммировать получившиеся корни и вставить результат в поле для ответа.
ps. Верный ответ содержит  9 знаков после запятой, т.е имеет вид 000000.000000000

psps. Рекомендую не пытаться обманывать, и извлекать числа другими способами. Работа с вкладками это одна из важных тем,
которую необходимо освоить.



sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html','http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    res = []
    sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
             'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html',
             'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html', ]
    browser.get(sites[0])
    blank = 1
    for site in sites[1:]:
        browser.execute_script(f'window.open("{site}", "_blank{blank}");')
        blank += 1
    tabs = browser.window_handles
    for x in range(len(tabs)):
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(.2)
        browser.find_element(By.CLASS_NAME, "check_box").click()
        res.append(browser.find_element(By.ID, "result").text)
        time.sleep(1)
print(sum([pow(int(i), 0.5) for i in res]))
