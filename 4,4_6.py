from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = [int(i.text.replace(' руб', '')) for i in soup.find_all('div', class_='price_box') ]
print(sum(div))
