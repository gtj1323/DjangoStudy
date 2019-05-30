import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bithumb.com/').text
#print(req)
soup = BeautifulSoup(req, 'html.parser')
# print(soup)
tags = soup.select('#tableAsset > tbody > tr > td:nth-child(1) > p > a > strong')

for tag in tags:
    print(tag.text)