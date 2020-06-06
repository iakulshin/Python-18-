import requests
import re
from bs4 import BeautifulSoup

param_search = {'lr':'159', 'text': input("Введите запрос: ")}
url = 'https://yandex.ru/search/'

request = requests.get(url, params=param_search)
response = BeautifulSoup(request.text, 'html.parser')

with open('output.txt', 'w', encoding='utf-8') as file:
    for i in response.findAll('a', href=True):
        url = i.get('href')
        if url.startswith('https'):
            file.write(url + '\n')
