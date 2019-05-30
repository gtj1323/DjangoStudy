import random
import requests
import json
from pprint import pprint
# 강사님 코드
"""
0. random 으로 로또번호를 생성합니다.
1. api 를 통해 우승 번호 번호를 가져옵니다.
2. 0 번과 1번을 비교하여 나의 등수를 알려준다.
--------
1. url 요청 보내서 정보를 가져옵니다.
    - json 으로 받는다. (딕셔너리로 접근 가능)
2. api 의 당첨번호와 보너스 번호를 저장하고.
3. 뽑은게 몇등인지, 몇번만에 당첨된건지 하는거 뽑으세요.
"""

url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=860'
res = requests.get(url)
lotto = res.json()

winner = []
for i in range(1, 7):
    winner.append(lotto[f'drwtNo{i}'])

bonus = lotto['bnusNo']

count = 0
rank = 0
while True:
    count += 1
    my_numbers = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(my_numbers))

    if matched == 6:
        rank = 1
    elif matched == 5 and bonus in my_numbers:
        rank = 2
    elif matched == 5:
        rank = 3
        break
    elif matched == 4:
        rank = 4
    elif matched == 3:
        rank = 5
    else:
        print('응 안돼')

money = count * 1000
print("이번 주 당첨번호: " + str(winner))
print("보너스 번호: " + str(bonus))
print("내 번호: " + str(my_numbers))
print(rank, ' 등 입니다.')
print(count, '번만에 당첨되셨습니다.')
print('쓴 돈은', format(money, ','))

# or
print('이번 주 당첨번호: ' + ', '.join(map(str, winner)) + ' + ' + str(bonus))
print('내 번호:  ' + ', '.join(map(str, my_numbers)))