from random import choice
import requests
import os

url = 'http://httpbin.org/ip'
project_dir = os.getenv("PROJECT_DIR")
with open(project_dir + 'proxy.txt') as file:
    proxy_file = file.read().split('\n')
    for _ in range(1000):
        try:
            ip = choice(proxy_file).strip()
            proxy = {
                'http': f'http://{ip}',
                'https': f'http://{ip}'
            }
            response = requests.get(url=url, proxies=proxy)
            print(response.json(), 'Success connection')
        except Exception as _ex:
            continue
