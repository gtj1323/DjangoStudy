import random
import requests
import json
# 주혁이 코드
def my_lotto():
    my_list = set()
    while True:
        number = random.randrange(1, 46)
        my_list.add(number)
        if len(my_list) == 6:
            return my_list

def get_lotto(num = 860):
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    res = requests.get(url)
    lotto = res.json()
    winner = set()
    for i in range(1, 7):
        winner.add(lotto[f'drwtNo{i}'])
    bonus = lotto['bnusNo']
    return winner, bonus

def check(my_n, com_n, com_b):
    print(f'나의 번호 : {sorted(my_n)}')
    print(f'당첨 번호 : {sorted(com_n)} + {com_b}')
    grade = len(my_n & com_n)
    if grade == 6:
        return 1
    elif grade == 5:
        my_b = (my_n - com_n).pop()
        if my_b == com_b:
            return 2
        return 3
    elif grade == 4:
        return 4
    elif grade == 3:
        return 5
    else:
        return 0

com_number, com_bonus = get_lotto()
result = 0
cnt = 0
prize = 2
while True:
    my_number = my_lotto()
    result = check(my_number, com_number, com_bonus)
    cnt += 1
    print(f'{cnt}번 도전결과 : {result}등')
    if (result != 0) & (result <= prize):
        break