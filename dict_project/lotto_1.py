import random
import requests
from bs4 import BeautifulSoup
from pprint import pprint

numbers = random.sample(range(800,861), 5) # 800~860까지 5개를 리스트로 뽑음.
for num in numbers:
    url = f'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}'
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    lottery = soup.select('.ball_645')
    print(f'{num} 회차 당첨 번호')
    count=0
    for lotto in lottery:
        if count!=6:
            print(lotto.text, end = ' ')
        elif count==6:
            print('+', lotto.text, end = ' ')
        count+=1
    print('\n')