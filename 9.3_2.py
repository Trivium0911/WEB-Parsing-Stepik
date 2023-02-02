"""                     9.3 Обход обычной капчи 2


Напишите скрипт который соберёт артикулы со всех страниц и карточек в разделе
https://captcha-parsinger.ru/;
Суммируйте все артикулы и вставьте полученное число в поле для ответа;"""


from python_anticaptcha import AnticaptchaClient, ImageToTextTask
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os


def solve_captcha() -> str:
    api_key = os.getenv('api_key')
    captcha_fp = open('captcha_ms.jpeg', 'rb')
    client = AnticaptchaClient(api_key)
    task = ImageToTextTask(captcha_fp)
    job = client.createTask(task)
    job.join()
    result = job.get_captcha_text()
    return result if (len(result) != 0 or result is None) \
        else job.report_incorrect()


res = []
with webdriver.Chrome() as browser:
    url = 'https://captcha-parsinger.ru/?page='
    for i in range(1, 7):
        browser.get(url + str(i))
        time.sleep(5)
        if 'Подтвердите, что вы не робот' in browser.page_source:
            time.sleep(10)
            browser.find_element(By.CSS_SELECTOR,
                                 'div[class="chakra-form-control '
                                 'css-1sx6owr"]').find_element(
                    By.TAG_NAME, 'img').screenshot('captcha_ms.jpeg')
            time.sleep(10)
            browser.find_element(By.ID, 'field-:r0:').send_keys(
                solve_captcha())
            time.sleep(5)
            browser.find_element(By.CSS_SELECTOR,
                                 'button[class="chakra-button '
                                 'css-1wq39mj"]').click()

        article_sum = sum([int(x.text.split()[1]) for x in browser.
                          find_elements(By.CLASS_NAME, 'css-1ecvsm5')])
        match article_sum:
            case 0:
                time.sleep(5)
                article_sum = sum([int(x.text.split()[1]) for x in browser.
                                  find_elements(By.CLASS_NAME,
                                                'css-1ecvsm5')])
        res.append(article_sum)

print(sum(res))
