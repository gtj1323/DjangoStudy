mulcam = {
    "location": ["서울", "경기", "강원", "부산"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "서울":  {
            "lecturer": "junho",
            "manager": "유신애",
            "class president": "강태훈",
            "groups": {
                "1조": ["강태훈", "궁정원", "백상우"],
                "2조": ["손민호", "안창균", "이지원"],
                "3조": ["이현호", "장주혁", "정민교"],
                "4조": ["정병태", "조남수", "최재진"],
            }
        },
        "부산": {
            "lecturer": "홍길동",
            "manager": "변사또"
        }
    }
}

"""
난이도* 1. 지역(location)은 몇개 있나요? : list length
출력예시) 4
"""
print('==== Q1 ====')
print(len(mulcam["location"]))
"""
난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
출력예시) False
"""
print('==== Q2 ====')
print('requests'in mulcam['language']['python']['python standard library'])
"""
난이도** 3. 서울반의 반장의 이름을 출력하세요. : depth 있는 접근
출력예시) 강태훈
"""
print('==== Q3 ====')
print(mulcam['classes']['서울']['class president'])
"""
난이도*** 4. mulcam 에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
출력 예시)
python
web
"""
print('==== Q4 ====')
for lang in mulcam['language'].keys():
    print(lang)
"""
난이도*** 5 mulcam 부산반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
출력 예시)
홍길동
변사또
"""
print('==== Q5 ====')
for info in mulcam['classes']['부산'].values():
    print(info)
"""
난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
"""
print('==== Q6 ====')
for name, exp in mulcam['language']['python']['frameworks'].items():
    print(f'{name}는 {exp}이다.')
"""
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
출력예시)
오늘의 당번은 강태훈
"""
print('==== Q7 ====')
from random import randrange
a = mulcam['classes']['서울']['groups']['4조'][randrange(0,3)]
print(f'오늘의 당번은 {a}')
# 다른 답
import random
d = mulcam['classes']['서울']['groups']['4조']
name = random.choice(d)
print(f'오늘의 당번은 {name}')