import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bithumb.com/').text

soup = BeautifulSoup(req, 'html.parser')
tags = soup.select('.coin_list tr')

with open('bitbit.txt', 'w', encoding='utf-8') as f:
    for tag in tags:
        name = tag.select_one('td:nth-of-type(1) a strong').text.replace(' NEW', '').strip()
        price = tag.select_one('td:nth-of-type(2) strong').text
        f.write(f'{name} / {price}\n')