'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
total=0;
for value in score.values():
    total+=value
avg = total/len(score)
print(avg)

# 다른 답
total = sum(score.values())
count = len(score)
print(total/count)

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
total=0;
count=0;
for score in scores.values():
    for value in score.values():
        total+=value
        count+=1
avg = total/count
print(avg)

# 다른 답
avg=0;
for student in scores.values():
    total=sum(student.values())
    avg+=total/len(student)
avg = avg/len(scores)
print(avg)

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
for CityN, temps in city.items():
    total = 0
    count = 0
    for temp in temps:
        total+=temp
        count+=1
    avgTemp=total/count
    print(CityN, ':', avgTemp)

# 다른 답
for name, temp in city.items():
    average_temp= sum(temp)/len(temp)
    print(f'{name} : {average_temp}')
'''
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
'''

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
lowTemp=0
hotTemp=0
for cityN, temps in city.items():
    for temp in temps:
        if lowTemp>temp :
            lowTemp=temp
            coldCity=cityN
        if hotTemp<temp :
            hotTemp=temp
            hotCity=cityN
print('hotCity', hotCity)
print('coldCity', coldCity)

# 다른 답
count = 0
cold = 0
hot =0
for name, temp in city.items():
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        minTemp = min(temp)
        maxTemp = max(temp)
        if cold > minTemp:
            cold = minTemp
            cold_city = name
        if hot < maxTemp:
            hot = maxTemp
            hot_city = name
    count+=1
print('hotCity', hot_city)
print('coldCity', cold_city)

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
for temp in city['서울']:
    if (temp==2):
        print('Yes')
        break

# 다른 답
if 2 in city['서울']:
    print('Yes')
else:
    print('No')