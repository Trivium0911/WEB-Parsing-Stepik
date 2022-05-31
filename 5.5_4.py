"""
                                     5.5 Скроллинг страниц 4
Когда вы хотите взаимодействовать с элементом который визуально перекрыт другим элементом, вы получите ошибку.

selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element
<button class="btn" onclick="clicks()">...</button> is not clickable at point (135, 179).
Other element would receive the click: <div class="block2"></div>
Это ошибка нам сообщает, что другой элемент получит клик. Для того чтобы исключить такие ситуации нам неходимо получить
фокус этого элемента. webdriver перед кликом проверяет ширину и высоту элемента, если они больше 0, то клик будет
произведён по центру элемента. Для того чтобы получить фокус элемента,
можно использовать .execute_script("return arguments[0].scrollIntoView(true);", element) где
element это объект webdriver'a.

Задача:

1. Откройте сайт (http://parsinger.ru/scroll/4/index.html) с помощью Selenium;
2. На сайте есть 50 кнопок, которые визуально перекрыты блоками;
3. После нажатия на кнопку в id="result" появляется уникальное для каждой кнопки число;
4. Цель: написать скрипт который нажимает поочерёдно все кнопки и собирает уникальные числа;
5. Все полученные числа суммировать, и вставить результат в поле для ответа.

"""


from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/4/index.html')
    res_elem = browser.find_element(By.ID, "result")
    res = []
    for button in browser.find_elements(By.CLASS_NAME, "btn"):
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        browser.execute_script("return arguments[0].scrollIntoView(true);", res_elem)
        res.append(int(res_elem.text))
print(sum(res))
