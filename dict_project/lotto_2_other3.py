import random
import requests
import json
from pprint import pprint
# 정원이 코드
url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=860'
res = requests.get(url)
lottery = res.json()

winner = set([])
for i in range(1, 7) :
    winner.add(lottery[f'drwtNo{i}'])

bonus = set([lottery['bnusNo']])

count = 0
first = 0
second = 0
third = 0
forth = 0
fifth = 0

while True :
    numbers = set(random.sample(range(1, 46), 6))

    jackpot = winner & numbers
    lucky = bonus & numbers

    if len(jackpot) == 6 :
        first += 1
        first_num = numbers
        break
    elif len(jackpot) == 5 and len(lucky) == 1 :
        second += 1
    elif len(jackpot) == 5 :
        third += 1
    elif len(jackpot) == 4 :
        forth += 1
    elif len(jackpot) == 3 :
        fifth += 1

    count += 1

reward_all = count * 1000
reward_5 = 5000 * fifth
reward_4 = 50000 * forth
reward_3 = int(( reward_all - ( reward_4 + reward_5 )) * 0.125 / third)
reward_2 = int(( reward_all - ( reward_4 + reward_5 )) * 0.125 / second)
reward_1 = int(( reward_all - ( reward_4 + reward_5 )) * 0.75 / first)

print('로또 제 860회')
print(f'총 구매자 수 : {count}')
print(f'총 당첨금 : {reward_all}')
print(f'당첨번호 {winner} + {bonus}')
print('------------------------------------')
print(f'1등 당첨자 수 : {first}')
print(f'1등 당첨금 : {reward_1}')
print('------------------------------------')
print(f'2등 당첨자 수 : {second}')
print(f'2등 당첨금 : {reward_2}')
print('------------------------------------')
print(f'3등 당첨자 수 : {third}')
print(f'3등 당첨금 : {reward_3}')
print('------------------------------------')
print(f'4등 당첨자 수 : {forth}')
print(f'4등 당첨금 : {50000}')
print('------------------------------------')
print(f'5등 당첨자 수 : {fifth}')
print(f'5등 당첨금 : {5000}')
print('------------------------------------')
print(f'기부자 수 : {count - first - second - third - forth - fifth}')