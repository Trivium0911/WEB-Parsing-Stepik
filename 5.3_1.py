import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('C:\\Users\\Lenovo\\AppData\\Local\\Google\\Chrome\\User Data\\'
                             'Default\\Extensions\\bpflbjmbfccblbhlcmlgkajdpoiepmkd\\1.4.1_0.crx ')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(50)