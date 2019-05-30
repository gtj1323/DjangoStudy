from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    lotto_num = request.args.get('lotto_num')
    if lotto_num=='':
        lotto_num = get_random()
    else:
        lotto_num = sorted([int(lotto_num.split()[i]) for i in range(0, 6)])
        print(type(lotto_num[0]))

    response = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    lotto = response.json()
    '''
    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])
    '''
    #list comprehension
    winner = [lotto[f'drwtNo{i}'] for i in range(1,7)]
    bonus = lotto["bnusNo"]
    res = check_luck(lotto_num, winner, bonus)
    return render_template('lotto_result.html',
                           lotto_round=lotto_round,
                           winner =f'{winner} + {bonus}',
                           my_num = f'{lotto_num}',
                           res=res)
    # 1. 내 번호 리스트 만들기
    # 2. 내 번호를 lotto_check 에서 입력받는 6개 번호로 만들기
    # 3. 당첨번호와의 교집합
    # 4. 조건에 따라 1등부터 꽝까지 결과값을 lotto_result로 출력.

def get_random():
    lucky = sorted(random.sample(range(1,46),5))
    return lucky

def check_luck(lucky_list, winner_list, winner_bonus_int):
    length = len(lucky_list)
    if length==6:
        lucky_set = set(lucky_list)
        winner_set = set(winner_list)
        diff_set = lucky_set - winner_set
        len_diff = len(diff_set)
        if len_diff == 0:
            return '1등'
        elif len_diff == 1:
            if winner_bonus_int in diff_set:
                return '2등'
            else:
                return '3등'
        elif len_diff == 2:
            return '4등'
        elif len_diff == 3:
            return '5등'
        else:
            return '꽝'
    elif length !=6:
        return '다시 입력해주세요.'

if __name__ == '__main__':
    app.run(debug=True)