# 1. dict를 만드는 방법
# 1-1. 직접 입력
lunch1={
    '중국집': '02'
}

# 1-2. 함수 이용.
lunch2 = dict(중국집='02')

print(lunch1)
print(lunch2)

# 2. 값 추가
lunch2['분식집']='031'

print(lunch1)
print(lunch2)

# 3. 구조에 따라 찾아오기.
idol={
    'bts':{
      '지민':25,
      'RM':24
    }
}
print(idol['bts']['지민'])

# 딕셔ㅓ리 + 반복문
for key in lunch2:
    print(key)
    print(lunch2[key])

# .items()
for key, value in lunch2.items():
    print(key, value)

# values()
for value in lunch2.values():
    print(value)

# keys()
for key in lunch2.keys():
    print(key)














