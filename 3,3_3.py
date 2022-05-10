from fake_useragent import UserAgent
import requests
import os

ua = UserAgent()
project_dir = os.getenv('PROJECT_DIR')
user_agent = 'user_agent.txt'
url = 'http://httpbin.org/user-agent'

for _ in range(10):
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    print(response.text)