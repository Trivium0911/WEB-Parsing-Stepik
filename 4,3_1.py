import requests
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as file:
    soup2 = BeautifulSoup(file, 'lxml')
    print(soup2)

# print("/-------------/")
#
# response = requests.get(url='http://parsinger.ru/html/watch/1/1_1.html')
# soup = BeautifulSoup(response.text, 'lxml')
#
# print(soup)