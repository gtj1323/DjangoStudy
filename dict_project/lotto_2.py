import random
import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=860'
res = requests.get(url)
lottery = res.json()
# pprint(lottery)

winner=[]
for i in range(1,7):
    winner.append(lottery[f'drwtNo{i}'])
bonus = lottery['bnusNo']
print(f'당첨 번호 : {winner} + {bonus}')
# 1. 내가 자동으로 산 복권 번호 번호와 당첨번호winner) 교집합 개수 비교
# 2. 특정 등수가 당첨 되면 멈추기
# 3. [도전] 몇번만에 당첨인지 /당첨까지 얼마를 썼는지
winner_set = set(winner)
bonus_set = set([bonus])
count=1
count2=0
count3=0
count4=0
count5=0
while True:
    my_num = random.sample(range(1,46), 6)
    my_num_set = set(my_num)
    #my_num_set = set([4, 8, 18, 25, 27, 43])
    diff_set = my_num_set - winner_set
    len_diff=len(diff_set)
    if len_diff == 0:
        break
    elif len_diff == 1:
        diff_bo_set = diff_set - bonus_set
        len_diff_bo = len(diff_bo_set)
        if len_diff_bo == 0:
            count2+=1
            #break
        elif len_diff_bo == 1:
            count3+=1
            #break
    elif len_diff == 2:
        count4+=1
        #break
    elif len_diff == 3:
        count5+=1
        #break
    count+=1
    if count%100000 == 0:
        print(f'{count}회 시도')
print(f'내 번호{my_num_set}, 횟수:{count}\n\t2등{count2}, 3등{count3}, 4등{count4}, 5등{count5}')
print(f'{count*1000}원 사용')
print("끝")
"""
1등 : 6개 번호 모두 일치
2등 : 5개 번호 일치 + 나머지 1개가 보너스 번호 일치
3등 : 5개 번호 일치
4등 : 4개 번호 일치
5등 : 3개 번호 일치
"""