[TOC]

# 5. 190530 Flask

**Web?**

> 클라이언트(웹브라우저)가 서버에 정보를 주고 받는 것.

Get : 데이터를 노출된 상태로 그대로 보냄.
Post : 데이터를 숨겨서 보냄.



## 5.0. 미리 알아둘 것. -데코레이터

- 데코레이터 사용 예시

```python
def hello(func):
    def wrapper(): #감싸주는 함수.
        print('HIHIHI')
        func()
        print('HIHI')
    return wrapper

#기존함수를 수정하지 않고, 다른 함수의 개념을 가져와서 사용함.
@hello # 함수이름을 써줌.
def bye():
    print('BYEBYE')

if __name__ == '__main__':
    bye()
```

- 결과

```
HIHIHI
BYEBYE
HIHI
```

**데코레이터 @함수**

> 기존의 함수를 수정하지 않고, 다른 함수의 개념을 가져올 수 있음.



## 5.1. Flask 기초 예제

Flask 설치 : `pip install flask`


- hello.py

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

**실행 명령 : cmd 혹은 git bash에서`FLASK_APP=hello.py flask run`**

> 플라스크는 app.py를 기본적으로 인식
> flask라는 이름의 파일은 인식 불가.
> `export FLASK_APP=hello.py` (FLASK_APP=hello.py 환경변수에 등록)하면 flask run만 하면 flask run으롯 실행 가능.

**app=Flask(\_\_name\_\_)**

>app말고 다른 이름을 쓰면 별도의 설정이 필요함.
>인스턴스를 생성시켜 줌.



## 5.2. Flask 사용.

- app.py   ***이하  app=Flask(\_\_name\_\_) , debug 는 호출되어 있다고 보고) 함수만 표시함.***

```python
@app.route('/') # app.route 함수가 요청을 받고, 처리하도록 도와주는 함수.
def index(): # 뷰 함수
    return 'Hellow World !'

@app.route('/hello')
def hello():
    return '반갑습니다 ! !2'

@app.route('/user/<int:username>') # 변화되는 값이면 < >사용. 숫자면 int: 사용.
def show_user_profile(username):
    # show the user profile for that user
    return f'User : {username}'

@app.route('/projects/') # 마지막에 /를 붙이는 경우 상관 없이 접속가능. 주로 메인페이지.
def projects():
    return 'The project page'

@app.route('/about') # 마지막에 /를 붙이는 경우 접속 불가.
def about():
    return 'The about page'

@app.route('/greeting/<string:name>') # default는 string
def greeting(name):
    return f'반갑습니다! {name}님!'

@app.route('/cube/<int:num>') # default는 string
def cube(num):
    result = num ** 3
    return str(result)

@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요!!</h1>' \
           '<ul>' \
           '    <li>1 li</li>' \
           '    <li>2 li</li>' \
           '</ul>'
        # 태그를 직접 보낼 수 있음.


if __name__ =='__main__': #이 파이썬 파일이 직접 실행된 코드라면 if문 코드를 동작함.
    app.run(debug=True) #서버를 껏다 킬 필요가 없도록 함. 서버가 실행중에도 디버깅을 함.
```

**app.route('/"url"',methods=['POST'])**

> url 주소를 주워줌.
> url에 '/'를 넣으면 주소에 '/'를 넣은 것과 안넣은 것에 상관 없이 접속가능.
> methods=['POST']를 입력하면 POST방식을 사용. 생략하면 get방식 사용.

**바뀔 수 있는 값 사용 : <변수 이름>**

> **url 주소에서 값이 바뀔 수 있는 경우에 사용함.**
> default는 string:
> 만약 타입을 지정해주려면 int: 등의 옵션을 주어야함.

**return 알 것 : 반드시 str 형식으로 바꾸어서 리턴하여야 함.**

> str형식이 아닌 것을 리턴하면 오류가 발생함.

**@app.run(debug=True)**

> 코드변경을 디버그로 쫓음.
> 파일 수정 시 자동으로 디버그하여 수정된 내용이 적용됨. 

**\_\_name\_\_**

> 현재 스크립트 파일이 시작점인지, 모듈인지 판단함.
> 만약 import하여 파일을 (모듈로) 시작하면 \_\_name\_\_ 는 '모듈 이름'이 됨.
> 만약 직접 실행하면 \_\_name\_\_ 는 '\_\_main\_\_' 이 됨.



### 5.2.1 실습 - 점심메뉴 정하기

1. /lunch/3 으로 요청이 들어옴.(3, 4, 5 숫자는 다양하게 들어 올 수 있음.)
2. 메뉴 리스트에서 랜덤으로 인원 수 만큼 메뉴를 골라서 출력

```python
@app.route('/lunch/<int:people>') # default는 string
def lunch(people):
    menu = ['짬뽕', '짜장면', '볶음밥', '곰탕', '돼지국밥', '비빔밥', '삼선짜장', '중화비빔밥']
    result = random.sample(menu, people)
    return str(result)
```



## 5.3. templates 사용 (플라스크는 jinja html 문법 사용.)

**반드시 templates라는 폴더안에 html파일을 작성하여 사용.**

```python
from flask import Flask, render_template, request
#render_template을 하여야 사용가능함.
```

**render_template**

> templates 폴더에 있는 html 문서를 jinja html 문법을 이용하여 사용 할 수 있게 해줌.

**request**

> 해당 url로 들어갈 때 어떤 값을 받아 올 때 사용.
> request.args.get('html변수명') : get방식으로 받아옴.(URL에 나타남.)
> request.form.get('html변수명') : POST방식으로 받아옴.(URL에 보이지 않음.)



- app.py, templates/index.html : 간단한 template 예시

```python
@app.route('/html_render')
def html_render():
    return render_template('index.html')
```

```html
<h1>여기는 템플릿입니다.</h1>
```



- app.py, templates/hello.html : string 넘겨받아서 쓰기.

```python
#넘겨받아서 템플릿에 쓰기.
@app.route('/html_name/<name>')
def html_name(name):
    return render_template('hello.html', name=name)
            # 왼쪽은 변수명(템플릿에서 사용할 이름), 오른쪽은 받은 값.
```

```html
<h1>안녕하세요!, {{name}}</h1>
```

**render_template('html파일', 템플릿 변수명 = python 변수명)**

> 변수를 받아서 사용하는 방법.

**{{템플릿 변수명.}}**

> 변수를 받아서 템플릿에 띄우는 방식.



- app.py, templates/cube.html : 여러개의 변수 넘기기.

```python
@app.route('/html_cube/<int:num>')
def html_cube(num):
    result = num ** 3
    return render_template('cube.html', num=num, cube=result)
```

```html
<h1>한 변의 길이가 {{num}}인 정육면체의 부피는 {{cube}}이다.</h1>
```



- app.py, templates/index.html : 간단한 template 예시

```python
@app.route('/html_render')
def html_render():
    return render_template('index.html')
```

```html
<h1>여기는 템플릿입니다.</h1>
```



- app.py  ,  template/pong.html  ,  template/ping.html  :  보내고 링크따라 가서 받기 : get방식.

```python
# 보낸 요청 받기(ping-pong)
@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    user_name = request.args.get('name')
    return render_template('pong.html', user_name=user_name)
```

```html
<!--pong.html-->
<form action="/pong">
	<input type="text" name="name">
	<input type="submit" value="핑!!">
	<!--	핑!!이 name이라는 이름으로 /pong으로 넘어감.	-->
</form>
```

```html
<!--ping.html-->
<h1>{{user_name}}</h1>
```



- app.py  ,  template/pong_new.html  ,  template/ping_new.html  :  보내고 링크따라 가서 받기 : POST방식.

```python
# post 방식의 ping-pong
# 보낸 요청 받기(ping-pong)
@app.route('/ping_new')
def ping_new():
    return render_template('ping_new.html')

@app.route('/pong_new', methods=['POST'])
def pong_new():
    user_name = request.form.get('name') # 포스트 방식은 form에 있음.
    return render_template('pong_new.html', user_name=user_name)
```

```html
<!--pong_new.html-->
<form action="/pong_new" method="POST"> <!-- git 방식이 디폴트 -->
	new
	<input type="text" name="name">
	<input type="submit" value="핑!!">
	<!--	핑!!이 name이라는 이름으로 /pong으로 넘어감.	-->
</form>
```

```html
<!--ping_new.html-->
new
<h1>{{user_name}}</h1>
```



### 5.3.1. 실습 - 저녁메뉴 정하기

1. /dinner 로 요청이 들어왔을 때
2. 저녁 메뉴에서 랜덤으로 하나를 뽑아서 이미지와 메뉴 이름을 응답.
3. 출력 예시
   오늘 저녁은 ???입니다.
   [이미지]

```python
@app.route('/dinner')
def dinner():
    menu = {'짬뽕':'',
            '짜장면':'',
            '볶음밥':'',
            }
    pick = random.choice(list(menu.keys()))
    # url1=menu['짜장면'] # 없는 메뉴가 나오면 key err
    url2=menu.get('짜장면') # 없는 메뉴면 none 리턴
    return render_template('dinner.html', pick=pick, url=url2)
```

```html
<h1>오늘 저녁은 {{dinner}}입니다.</h1>
    <br>
    <img src="{{url}}" alt="{{pick}}사진">
```



### 5.3.2. 실습 - 저녁메뉴 정하기

1. /dinner 로 요청이 들어왔을 때
2. 저녁 메뉴에서 랜덤으로 하나를 뽑아서 이미지와 메뉴 이름을 응답.
3. 출력 예시
   오늘 저녁은 ???입니다.
   [이미지]

```python
@app.route('/lotto')
def lotto():
    number_list = list(range(1,46))
    lucky = random.sample(number_list, 6)
    # 진자 템플릿은 연산이 가능함.
    return render_template('lotto.html', lucky=lucky)
```

```html
<h1>{{lucky}}</h1>
	{% for num in lucky %}<!-- for문을 열어줌.	-->
		<h2>{{num}}</h2>
	{% endfor %}<!-- for문을 닫아줌..	-->
```

**{% 가려질 내용. %}**

> 작성 후 템플릿이 나갈 때는 가려져서 나가지 않을 수 있음.

**for num in [list]  ,  endfor**

>jinja 문법은 연산이 가능함.
>for 문을 사용한 후 종료를 해야함.



### 5.3.3. 실습 - FakeNaver

```python
#Fake naver
@app.route('/naver')
def naver():
    return render_template('naver.html')
```
```html
<h1>네이버 검색</h1>
<form action="https://search.naver.com/search.naver" target="_blank">
	<input type="text" name="query">
	<input type="submit" value="검색">
</form>
```



### 5.3.4. 실습 - FakeGoogle

```python
@app.route('/google')
def google():
    return render_template('google.html')
```

```html
<h1>구글 검색</h1>
	<form action="https://www.google.com/search" target="_blank">
	<input type="text" name="query">
	<input type="submit" value="검색">
</form>
```



### 5.3.5. 실습 - 신이 나를 만들 때.

- god_st.html  ,  god_re.html

```python
@app.route('/god_st')
def got_st():
    return render_template('/god_st.html')

@app.route('/god_re')
def got_re():
    name = request.args.get('name')
    material_list = ['기민함', '돈 복', '멍청함', '똑똑함', '시끄러움']
    reaction_list = ['조금만...', '적당히...', '으어어어...', '그냥 넣지 말고...']
    mat = random.sample(material_list, 3)
    print(mat)
    rea = random.sample(reaction_list, 3)
    print(rea)
    zziipp = zip(mat,rea)
    return render_template('/god_re.html', name=name,  zziipp=zziipp)
```

```html
<form action="/god_re"> <!-- git 방식이 디폴트 -->
	god
	<input type="text" name="name">
	<input type="submit" value="신의 응답">
	<!--	핑!!이 name이라는 이름으로 /pong으로 넘어감.	-->
</form>
```

```html
god
<h2>{{name}}님을 만들 때</h2>
{% for mat, rea in zziipp %}<!-- for문을 열어줌.	-->
		<h2>{{mat}}을 {{rea}}</h2>
	{% endfor %}<!-- for문을 닫아줌..	-->
```



### 5.3.6. 실습 - Lotto 당첨번호 확인

- lotto_check.html  ,  lotto_result.html

```python
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
```

```html
<form action="lotto_result">
    회&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp차 : <input type="text" name="lotto_round">
    <br>
    나의 번호 : <input type="text" name="lotto_num" value="빈칸이면 랜덤.">(띄어 쓰기로 구분)
    <br>
    <input type="submit" value="결과 확인!">
</form>
```

```html
<h1>회차 : {{lotto_round}}</h1>
<h2>당첨 번호 : {{winner}}</h2>
<h2>나의 번호 : {{my_num}}</h2>
<h2>결과 : {{res}}</h2>
```





***


# ※ 참고자료 190530
>  - 참고 - Flask 공식문서 : <http://flask.pocoo.org/>
>  - 참고 - Jinja 템플릿 문법 : <http://jinja.pocoo.org/>



