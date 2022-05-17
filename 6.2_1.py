import time

from selenium import webdriver

url = 'https://stepik.org/'
browser = webdriver.Chrome()

browser.get(url)
time.sleep(5)
