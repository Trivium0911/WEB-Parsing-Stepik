"""
                                5.5 Методы Selenium 7
Откройте сайт (https://parsinger.ru/methods/3/index.html) с помощью Selenium;
Ваша задача получить все значения с чётным числом после "_" и суммировать их;
Полученный результат вставить в поле для ответа.
"""


from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    res = []
    for cookie in cookies:
        if int(cookie['name'].replace('sercet_cookie_', '')) % 2 == 0:
            res.append(int(cookie['value']))
print(sum(res))

