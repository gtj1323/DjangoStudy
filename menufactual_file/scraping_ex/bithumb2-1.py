# 코인명 /각겨 정보로 txt 저장하기
import requests
from bs4 import BeautifulSoup

# 1. names와 prices 리스트를 받아 옴.
req = requests.get('https://www.bithumb.com/').text
soup = BeautifulSoup(req, 'html.parser')

names = soup.select('#tableAsset > tbody > tr > td:nth-child(1) > p > a > strong')
prices = soup.select('#tableAsset > tbody > tr > td:nth-child(2) > strong')

# 2. zip으로 묶어서 NEW를 분리하여 제거 한 후, 텍스트파일bitbit.txt에 씀.
with open('bitbit.txt', 'w', encoding='utf-8') as f :
    for name, price in zip(names, prices):
        n = name.text.split()
        # if ' NEW' in name.text:
        #     name.text.replace(' NEW', '')
        #     print(name.text, 'new!')
        f.write(f'{n[0]} / {price.text}\n')