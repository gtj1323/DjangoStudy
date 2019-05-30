import  requests
from bs4 import BeautifulSoup

# 일반적인 크롤링이 불가능 한 경우 헤더를 함께 보내야 응답하는 경우가 있음. 반드시 헤더는 dirc 형태로 보내야 함.
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
req = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text

soup = BeautifulSoup(req, 'html.parser')
tags = soup.select('#lst50')

with open('MelonCart.txt', 'w', encoding='utf-8') as f:
    for tag in tags:
        rank = tag.select_one('td:nth-child(2) .rank').text
        artist = tag.select_one('td:nth-child(6) .ellipsis.rank01 a').text
        title = tag.select_one('td:nth-child(6) .ellipsis.rank02 a').text
        print(f'{rank}위 / {artist} / {title}')
        f.write(f'{rank}위 / {artist} / {title}\n')