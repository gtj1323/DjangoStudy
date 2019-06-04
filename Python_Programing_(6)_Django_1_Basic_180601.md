[TOC]

# 6. Django Framework
Django - MTV(model, template, view)
M - 데이터 관리
T - 사용자가 보는 화면
V - 중간 관리자



1. Django 설치 (pip 명령어로 설치)
	`pip install django`
2. 새로운 앱 만들기
	`django-admin startproject intro .`      (만약 '.'' 이 없으면 폴더가 하나 더 생성됨. intro 폴더 생성.)
	`python manage.py startapp [앱이름]`     ((앱이름) 라는 app 생성 앱이름은 복수형 권장.)
	- Ex) `python manage.py startapp pages `    (pages 라는 app 생성)
3. 서버 기동
	`python manage.py runserver` 서버를 기동함. 수정시 자동으로 디버깅하여 적용됨.
4. .git ignore 설정
	프로젝트에 .gitignore 추가, 내용에 .idea/ 추가



## 6.1 Django  프로젝트 파일 설명 및 설정.
1. **intro\ **
**\_\_init\_\_.py** : 프로젝트 초기화 시켜주는 파일.
**setting.py** : 프로젝트 모든 세팅.
**urls.py** : 어떤 뷰를 사용할지 방향을 설정. 요청이 가장 먼저 오는 곳. 관리자페이지가 먼저 만들어져 있음. url을 쌓아 올라가야함. 순서의 영향을 받음.
**wsgi.py** : 장고와 웹서버 연결해주는 통신 프로토콜
2. **pages\ **     (정확히는 application 이름을 가진 dir.)
**\_\_init\_\_.py**
**migration.py** : 모델 설계도
**admin.py** : 관리자용 페이지
**app.py** : 앱 정보
**models.py** : 데이터베이스 조작
**test.py** : 테스트 코드
**views.py** : 컨트롤러 역할을 하고 view들을 조작.
**urls.py** : 만들어 줘야함. applicatino 내에서 url을 관리하는 파일.

> Django는 작성순서를 일반적으로 아래에서 위로 작성.
> list, tuple, dict 상관없이 마지막 항목 마지막에 ','를 붙이는 것이 관례
> pages/urls 는 위에서 아래로 작성.
> 모든 파일의 마지막에 빈 라인이 추가되면 에러 비슷한 내용이 나오지 않음.



-  inro\setting.py : Django 설정값이 저장되어 있음.

```python
"""
... 윗부분 생략 ...
"""
INSTALLED_APPS = [
    # local apps
    # 'pages'# 어플리케이션 이름을 써도 되지만, 정확하게는 아랫부분으로 쓰는 것을 권장. 경로를 따가가보면 해당 클래스가 존재함.
    'pages.apps.PagesConfig',
    # thrid party apps

    #django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',#장고는 항상 마지막에 콤마를 쓰도록 권장함.
]

"""
... 중간부분 생략 ...
"""

# Internationalization # 국제화 설정
LANGUAGE_CODE = 'ko-kr'# 언어 설정, en-us -> ko-kr

TIME_ZONE = 'Asia/Seoul' # 시간 설정. UTC -> Asia/Seoul 데이타베이스 타임존.Time Zone Abbreviations – Worldwide List

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
```

**INSTALLED_APPS**

> 사용할 앱에 대한 정보를 나타내는 list

**TIME_ZONE**

>  template forms 에서 출력되는 시간.
>  만약 모델에서도 사용자가 지정한 TIME_ZONE 값을 적용시기기 위해 False로 설정.

**LANGUAGE_CODE**

> 기본 언어 설정.



- intro\urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 요청이 가장 먼저 오는 곳. 관리자페이지가 먼저 만들어져 있음.
    # path('url', ) url을 쌓아 올라가야햠. 순서가 중요함. 위쪽부터 동작함.
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
```

**path('pages/', include('pages.urls'))**
> 어플리케이션을 작동시킬 url과 사용할 파일을 지정해줌.
> 해당 경로를 사용하기 위해서는 pages/가 반드시 앞에 포함되어야함.

**path('admin/',admin.site.urls)**

> 관리자 페이지로 가기 위한 url
> Django의 경우 관리자 페이지가 만들어져 있어 별도로 만들어줄 필요가 없음.



- pages\urls.py

```python
from django.urls import path, include
from . import views

urlpatterns = [ # 유일하게 위에서 아래로 내려가면서 작성함.
    path('', views.index),
    # 끝에 urls 에 항상 '/'를 써야함.
    path('dinner/', views.dinner),
    path('hello/<name>/', views.hello),
    path('introduce/<name>/<age>/', views.introduce),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:radius>/', views.area),
    path('dtl_example/', views.dtl_example),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('artii/', views.artii),
    path('result/', views.result),
    path('user-new/', views.user_new),
    path('user-create/', views.user_create),
    path('static-example', views.static_example), #마지막에 ','를 붙이는 것이 관례
]

```

**path('사용할 url/', 사용할 기능.)**

> 사용할 url에는 반드시 끝에 '/'를 넣어야함.
> views.py에서 사용할 기능이 정의 되있는 것을끌어와야함.
> 경로에는 <string:>, <int:> 받아올 값의 종류 설정가능
>
> - ex) intro\urls.py 에 path('pages/', include('pages.urls')), 가 추가되어 있다고 하면.
> **path('dinner/', views.index)**
>
>     > /pages/ url로 접속하면 views.py의 dinner함수를 실행.
>
>   **path('hello/\<name>')**
>   
>   > /pages/hello/이름/ 이라는 url로 접속하면 views.py의 introduce함수 실행.



## 6.2 Django Template Language(DTL).

Django는 Template에서 다양한 방법으로 활용이가능하다.
활용하기 위해서는 application명을 가진 폴더 안의 templates라는 폴더에 있어야 함.
[DTL 사용법](https://docs.djangoproject.com/en/1.7/topics/templates/)

1. Template 상속관계 만들기.
- base.html  :  base가 될 템플릿. 부트스트랩, 폰트어썸 을 포함함. 자식은 바디, css파일만 작성하면 됨.
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<!-- 폰트 어썸 --><script defer src="https://use.fontawesome.com/releases/v5.8.2/js/all.js" integrity="sha384-DJ25uNYET2XCl5ZF++U8eNxPWqcKohUUBUpKGlNLMchM7q4Wjg2CUpjHLaL8yYPH" crossorigin="anonymous"></script>
	<!-- daneden Animate.css 가져오기. 사용법은 Github에 나옴. --><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css">
    <!-- 부트스트랩 --><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	{% block css %}{% endblock %}
	<title>title</title>
</head>

<body>
    <div class="container">
        <h1>장고 연습</h1>
        {% block content %}
        {% endblock %}
    </div>
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>

</html>
```

**{% block css %}{% endblock %}**
**{% block content %}{% endblock %}**
> 자식이 작성해야 하는 부분.
> content, css는 작성자가 지정하는 변수로 바꾸어 사용해도됨. 
> 하나의 부모에 여러개의 block을 만들 수 있음.(title, css 등)

2. Django Template Language 사용법.

- dtl_example.html

```html
{% extends "base.html" %}
<!-- extends는 항상 최상단에 있어야 인식 됨. 상대경로로 작성.-->
{% block css %}
	<link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
{% endblock css %}

{% block content %}
	<h1>'menus': {{menus}},
        'my_sentence': {{my_sentence}},
        'messages': {{messaes}},
        'datetimenow': {{datetimenow}},
        'empty_list': {{empty_list}}</h1>
	<h3>1. 반복문</h3>
	{% for menu in menus%}
		<p>{{menu}}</p>
	{% endfor %}
	<hr>
	{% for menu in menus%}
		<p>{{ forloop.counter}} : {{menu}}</p>
	{% endfor %}
	<hr>
	{% for user in empty_list%}
		<p>{{user}}</p>
	{% empty %}
		<p>지금 가입한 유저가 없습니다.</p>
	{% endfor %}
	<hr>
	<h3>조건문</h3>
	{% for menu in menus %}
		{% if forloop.first %}
			<p>짜장면 + 고춧가루</p>
		{% else %}
			<p>{{menu}}</p>
		{% endif %}
	{% endfor %}
	<hr>
	<h3>3. length filter</h3>
	{% for message in messages %}
		{% if message|length > 5 %}
			<p>글이 너무 길어요.</p>
		{% else %}
			<p>{{message}}, {{message|length}}</p>
		{% endif %}
	{% endfor %}\
	<!-- 모두 가능하다 >=, <=, ==, !=, in, not, in ,is -->
	<hr>
	<h3>4. lorem ipsum</h3>
	{% lorem %}
	<hr>
	{% lorem 3 w %}
	<hr>
	{% lorem 3 w random %}
	<hr>
	{% lorem 3 p%}

	<h3>5. 글자 수 제한</h3>
	<!-- 단어 단위로 잘라서 나타내기.-->
	<p>{{my_sentence|truncatewords:3}}</p>
	<p>{{my_sentence|truncatewords:4}}</p>
	<!-- 공백, ... 도 하나의 글자로 봄.-->
	<p>{{my_sentence|truncatechars:3}}</p>
	<p>{{my_sentence|truncatechars:4}}</p>

	<hr>
	<h3>6. 글자 관련 필터</h3>
	<p>{{'abc'|length}}</p>
	<p>{{'ABC'|lower}}</p>
	<p>{{my_sentence|title}}</p>
	<p>{{'abc def'|capfirst}}</p>
	<p>{{'Abc Def'|capfirst}}</p>
	<p>{{'abc Def'|capfirst}}</p>
	<p>{{menus|random}}</p>

	<hr>
	<h3>7. 연산</h3>
	<p>{{ 4|add:6 }}</p>

	<hr>
	<h3>8. 날짜 표현</h3>
	<!-- dtl의 주석처리는 %->#으로 둘 다 변경.	-->
	{{datetimenow}}
	{% now 'DATETIME_FORMAT' %}<br>
	{% now 'SHORT_DATETIME_FORMAT %}<br>
	{% now 'DATE_FORMAT' %}<br>
	{% now 'SHORT_DATE_FORMAT' %}<br>
	{% now "Y" as current_year %}<br>
	Copyright {{ current_year }}

	<hr>
	<h3>9. 기타</h3>
	<!--url을 만들어 줌.-->
	{{'google.com'|urlize}}
{% endblock %}
```

**{% extends "상속받을 html 파일" %}**
>  상대경로로 작성해야함.  최상단에 위치해야 됨.

**{% block css %}사용할 CSS파일{% endblock css %}**
>  CSS파일을 선택하여 사용할 수 있게 함. ednblock의 css는 안써도됨.(2중으로 한 경우 작성)

**{% for menu in menus%} 반복 내용 {% endfor %}**

> for문을 사용함. menus라는 list에서 하나씩 뽑아서 사용. endfor 앞까지의 내용을 반복함.

**{% for user in empty_list%}**
		**\<p>{{user}}\</p>**
	**{% empty %}**
		**\<p>지금 가입한 유저가 없습니다.\</p>**
**{% endfor %}**

> 조건 for문 사용. 만약 list가 empty인 경우 작성될 내용을 명시함.

**{% for menu in menus %}**
	**{% if forloop.first %}**
		**\<p>짜장면 + 고춧가루\</p>**
	**{% else %}**
		**\<p>{{menu}}\</p>**
	**{% endif %}**
**{% endfor %}**

> if forloop.first : 조건문의 첫번째 루프인 경우.

**{% for message in messages %}**
	**{% if message|length > 5 %}**
		**\<p>글이 너무 길어요.\</p>**
​	**{% else %}**
		**\<p>{{message}}, {{message|length}}\</p>**
​	**{% endif %}**
**{% endfor %}**

> message|length : message라는 변수의 length를 나타냄.

**{% lorem %}
{% lorem 3 w %}
{% lorem 3 w random %}
{% lorem 3 p%}**

> 아무것도 없으면 1개의 문단을 나타냄.
> 3 w : 앞의 3개 단어를 나타냄.
> 3 w : 랜덤으로 3개의 단어를 나타냄.
> 3 p : 3개의 문단을 나타냄.

**{{my_sentence|truncatewords:3}}
{{my_sentence|truncatewords:4}}
{{my_sentence|truncatechars:3}}
{{my_sentence|truncatechars:4}}**

> my_sentence의 일부를 잘라서 씀.
> truncatewords:3 앞 3개의 단어를 나타냄. 뒤에 ... 붙음
> truncatechars:3 앞 3개의 글자를 나타냄. 띄어쓰기와 ... 도 글자로 취급함.

**{{'abc'|length}}
{{'ABC'|lower}}
{{my_sentence|title}}
{{'abc def'|capfirst}}
{{'Abc Def'|capfirst}}
{{'abc Def'|capfirst}}
{{menus|random}}**

> length : 글자 갯수.
> lower : 전부 소문자.
> title : 타이틀(한 문장).
> capfirst : 첫글자 대문자로.
> random : list에서 랜덤으로 하나 뽑음.

**{{ 4|add:6 }}**

> 더하기 연산. 뺄셈이랑 더 있긴 함.

**{{datetimenow}}
{% now 'DATETIME_FORMAT' %}
{% now 'SHORT_DATETIME_FORMAT %}
{% now 'DATE_FORMAT' %}
{% now 'SHORT_DATE_FORMAT' %}
{% now "Y" as current_year %}
Copyright {{ current_year }}**

> 다양한 날짜 표현 방법.

**{{'google.com'|urlize}}**

> 링크.



## 6.3. Django 사용하기. [app : pages]

**아래의 파일은 모두 pages 앱, intro\urls.py에 pages/ 라는 url로 등록되어 있음.**
따라서 모든 url은 앞에 pages/가 붙음.

### 6.3.1. Django 기본 사용.


- pages\views.py 에 추가된 내용.
```python
def index(request): # request는 필수인자.
    return render(request, 'pages/index.html') # 반드시 templates 라는 폴더 안에 있어야함.
```
- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.
```python
path('', views.index),
```
- templates\\pages\\index.html

```html
{% extends "base.html" %}
{% block content %}
	<h1>Hellow Django</h1>
{% endblock %}
```

**path('',views.index)**

> pages/라는 url로 접근시 views.py의 index함수로 감.

**render(request, 'html파일')**

> request를 html파일에 랜더링하여 출력함.

### 6.3.2. Django, Template에 띄울 값 리턴.

- pages\views.py 에 추가된 내용.
```python
def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {'pick':pick}
    return render(request, 'pages/dinner.html', context)
```
- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.
```python
path('dinner/', views.dinner),
```
- templates\\pages\\dinner.html
```html
{% extends "base.html" %}
{% block content %}
	<h1>오늘 저녁은 {{pick}}</h1>
{% endblock %}
```
**path('dinner/',views.dinner)**

> pages/dinner/로 접근하면 pages/views.py의 dinner함수 사용.

**render(request, 'html파일', context)**

> context라는 dict를 넘겨주면 template에서 key를 이용하여 값을 사용가능.

### 6.3.3. Veriable Routing 방식1 : 1개의 값을 입력.

- pages\views.py 에 추가된 내용.
```python
def hello(request, name):
    context={
        'name':name,
    }
    return render(request, 'pages/hello.html', context)
```
- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.
```python
path('hello/<name>/', views.hello),
```
- templates\\pages\\hello.html
```html
{% extends "base.html" %}
{% block content %}
	<h1>Hellow {{name}}</h1>
{% endblock %}
```
**path('hello/\<name>/', views.hello)**

> <name>으로 작성된 부분에는 어떠한 형식으로든 string값을 입력받음.
> 입력받은 값을 사용하여 함수가 내부적으로 작동함.

**def hello(request, name):**
> 라우팅방식으로 값을 입력받으면 해당 값이 이 추가되어 정의해야함.


### 6.3.4. Veriable Routing 방식2 : 여러개의 값을 입력.

- pages\views.py 에 추가된 내용.
```python
# 자기소기 / 이름, 나이를 url로 받아서 출력.
def introduce(request, name, age):
    context={
        'name': name,
        'age': age,
    }
    return render(request, 'pages/introduce.html', context)
```
- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.
```python
path('introduce/<name>/<age>/', views.introduce),
```
- templates\\pages\\introduce.html
```html
{% extends "base.html" %}
{% block content %}
	<h1>이름 {{name}}, 나이 {{age}}</h1>
{% endblock %}
```

### 6.3.5. Veriable Routing 방식3 : 입력형식 지정.

- pages\views.py 에 추가된 내용.
```python
# 숫자 2개를 veriable reouting 방식으로 으로 받아 곱셈 결과 출력.
def times(request, num1, num2):
    res = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'res': res,
    }
    return render(request, 'pages/times.html', context)
```
- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.
```python
path('times/<int:num1>/<int:num2>/', views.times),
```
- templates\\pages\\times.html
```html
{% extends "base.html" %}
{% block content %}
	<h1>Times 'num1': {{num1}}, 'num2': {{num2}}, 'res': {{res}}</h1>
{% endblock %}
```
**path('times/\<int:num1>/\<int:num2>/', views.times)**

> 입력형식을 지정해줌.


### 6.3.6. Veriable Routing 방식4 : 입력받아 연산.

- pages\views.py 에 추가된 내용.
```python
# 원의 반지름 값을 variable routing 으로 받아 원의 넓이를 출력.
def area(request, radius):
    area = radius**2 * 3.141592653589793
    context = {
        'area': area,
    }
    return render(request, 'pages/area.html', context)
```
- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.
```python
path('area/<int:radius>/', views.area),
```
- templates\\pages\\area.html
```html
{% extends "base.html" %}
{% block content %}
	<h1>area : {{area}}</h1>
{% endblock %}
```

### 6.3.7. GET 방식 데이터 입력.

**_<u>GET 은 DB에서 데이터를 꺼내는 것! - > DB변화 X</u>_**

- pages\views.py 에 추가된 내용.
```python
# Throw Catch (variable louting을 하지 않음.)
def throw(requset):
    return render(requset, 'pages/throw.html')

def catch(requset):
    # print(requset.GET)
    message = requset.GET.get('message')
    context={'message': message}
    return render(requset, 'pages/catch.html', context)
```
- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.
```python
path('throw/', views.throw),
path('catch/', views.catch),
```
- templates\\pages\\throw.html
```html
{% extends "base.html" %}
{% block content %}
	<form action="/pages/catch">
		<input type="text" name="message">
		<input type="submit" value="제출">
	</form>
{% endblock %}
```
- template\pages\catch.html

```html
{% extends "base.html" %}
{% block content %}
	<h3>{{message}}</h3>
{% endblock %}
```

**\<form action="/pages/catch">**

> Default 방식이 GET방식. 데이터를 GET방식으로 하여 보낸 후 /pages/catch/ url로 보냄.
> 여기서는 name="message"로 지정 했기 때문에 받을 때 "message"로 해주어야햠.

**requset.GET.get('message')**

> GET방식으로 입력받은 데이터 중 'message'라는 name을 가진 것을 뽑아옴.

#### 6.3.7.1 GET방식 예제 : ASCII ART 받아오기.

- pages\views.py 에 추가된 내용.

```python
# requsets, random 필요.
#ASCII ART
def artii(requset):
    return render(requset, 'pages/artii.html')

def result(requset):
    # 1. form에서 날아온 데이터를 받음.
    message = requset.GET.get('message')
    print(f'message={message}')
    # 2. http://artii.herokuapp.com/fonts_list로 요청을 보내 응답을 결과로 .text로 변환후 저장.
    req = requests.get('http://artii.herokuapp.com/fonts_list').text
    # 3. 저장한 데이터를 list 로 바꾼다.
    fonts = req.split('\n')
    # 4. List 안에 들어있는 요소(font) 하나를 선택해서 저장.
    font = random.choice(fonts)
    # 5. 우리가 전달한 데이터와 저장한 font를 가지고 다시 요청을 보내 해당 응답 결과를 저장. (.text)
    url = f'http://artii.herokuapp.com/make?text={message}&font={font}'
    artii_res = requests.get(url).text
    # 5. 최종적으로 지정한 데이터를 template로 넘겨줌.
    context = {
        'artii': artii_res,
        'url': url
    }
    return render(requset, 'pages/result.html', context)
```

- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.

```python
path('artii/', views.artii),
path('result/', views.result),
```

- templates\\pages\\ascii.html

```html
{% extends "base.html" %}
{% block content %}
	<form action="/pages/result">
		<input type="text" name="message">
		<input type="submit" value="제출">
	</form>
{% endblock %}
```

- template\pages\result.html

```html
{% extends "base.html" %}
{% block content %}
    <pre>{{artii}}</pre>
    <!--html pr tag를 사용하여야 함.-->
    {{url}}
{% endblock %}
```

**pre 태그**

> 작성된 내용을 띄어쓰기, 텝 등을 그대로 표시하는 태그.

### 6.3.8. POST 방식으로 입력 받기.

**_<u>POST는 DB를 조작(생성/ 수정/ 삭제)! - > DB변화 O</u>_**

- pages\views.py 에 추가된 내용.

```python
# POST 방식
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'pwd': pwd,
    }
    return render(request, 'pages/user_create.html', context)
```

- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.

```python
path('user-new/', views.user_new),
path('user-create/', views.user_create),
```

- templates\\pages\\user_new.html

```html
{% extends "base.html" %}
{% block content %}
	<!--포스트 방식에서는 url에 '/'를 상항 붙여야 함.-->
	<form action="/pages/user-create/" method="POST">
	{% csrf_token %}
		이름 : <input type="text" name="name"><br>
		비밀번호 : <input type="password" name="pwd">
		<input type="submit" value="가입!!!">
	</form>
{% endblock %}
```

- template\pages\user_create.html

```html
{% extends "base.html" %}
{% block content %}
	<p>이름 : {{name}}</p>
	<p>비밀번호 : {{pwd}}</p>
{% endblock %}
```

**\<form action="/pages/user-create/" method="POST">**

> POST방식으로 값을 전달함.

**requset.POST.get('message')**

> POST방식으로 'message'라는 이름으로 전달된 값을 받아옴.

**{% csrf_token %}**

> 토큰을 자동으로 생성해줌. 보안문제와 관련 있음. POST방식에서 반드시 필요함.

### 6.3.9. static파일 사용하기.

static 파일
image css js 파일 등 별도의 처리없이 파일 내용을 그대로 보여줘도 되는 파일. (image, css 등)
Django는 app에 static 폴더에 위치가 지정되어 있음.

- pages\views.py 에 추가된 내용.

```python
def static_example(request):
    return render(request, 'pages/static_example.html')
```

- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.

```python
path('static-example', views.static_example),
```

- templates\\pages\static_example.html

```html
{% extends "pages/base.html" %}
<!-- extends는 항상 최상단에 있어야 인식 됨.-->

{% load static %}

{% block css %}
	<link rel="stylesheet" href="{% static 'pages/stylesheets/style.css' %}">
{% endblock css %}

{% block content %}
	<h1>static 파일 실습</h1>
	<img src="{% static 'images/123.gif' %}" alt="img">
{% endblock %}

```
```css
h1{
    color:red;
}
```
**{% load static %}**
> static 사용 선언.

**\<link rel="stylesheet" href="{% static 'pages/stylesheets/style.css' %}">**
> static 폴더의 style.css 를 불러옴.

**\<img src="{% static 'pages/images/123.gif' %}" alt="img">**

> static 폴더의 page/images/123.gif를 띄움.

### 6.3.10. dtl_example

- pages\views.py 에 추가된 내용.

```python
def dtl_example(requset):
    menus=['짜장명', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, You need python'
    messages = ['apple', 'banana', 'cucumbr', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(requset, 'pages/dtl_example.html', context)

```

- pages\urls.py 에 urlpatterns라는 list에 추가될 내용.

```python
path('dtl_example/', views.dtl_example),
```

- templates\\pages\\dtl_example.html

```html
{% extends "base.html" %}
<!-- extends는 항상 최상단에 있어야 인식 됨.-->
{% load static %}

{% block css %}
	<link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
{% endblock css %}

{% block content %}
	<h1>'menus': {{menus}},
        'my_sentence': {{my_sentence}},
        'messages': {{messaes}},
        'datetimenow': {{datetimenow}},
        'empty_list': {{empty_list}}</h1>
	<h3>1. 반복문</h3>
	{% for menu in menus%}
		<p>{{menu}}</p>
	{% endfor %}
	<hr>
	{% for menu in menus%}
		<p>{{ forloop.counter}} : {{menu}}</p>
	{% endfor %}
	<hr>
	{% for user in empty_list%}
		<p>{{user}}</p>
	{% empty %}
		<p>지금 가입한 유저가 없습니다.</p>
	{% endfor %}
	<hr>
	<h3>조건문</h3>
	{% for menu in menus %}
		{% if forloop.first %}
			<p>짜장면 + 고춧가루</p>
		{% else %}
			<p>{{menu}}</p>
		{% endif %}
	{% endfor %}
	<hr>
	<h3>3. length filter</h3>
	{% for message in messages %}
		{% if message|length > 5 %}
			<p>글이 너무 길어요.</p>
		{% else %}
			<p>{{message}}, {{message|length}}</p>
		{% endif %}
	{% endfor %}\
	<!-- 모두 가능하다 >=, <=, ==, !=, in, not, in ,is -->
	<hr>
	<h3>4. lorem ipsum</h3>
	{% lorem %}
	<hr>
	{% lorem 3 w %}
	<hr>
	{% lorem 3 w random %}
	<hr>
	{% lorem 3 p%}

	<h3>5. 글자 수 제한</h3>
	<!-- 단어 단위로 잘라서 나타내기.-->
	<p>{{my_sentence|truncatewords:3}}</p>
	<p>{{my_sentence|truncatewords:4}}</p>
	<!-- 공백, ... 도 하나의 글자로 봄.-->
	<p>{{my_sentence|truncatechars:3}}</p>
	<p>{{my_sentence|truncatechars:4}}</p>

	<hr>
	<h3>6. 글자 관련 필터</h3>
	<p>{{'abc'|length}}</p>
	<p>{{'ABC'|lower}}</p>
	<p>{{my_sentence|title}}</p>
	<p>{{'abc def'|capfirst}}</p>
	<p>{{'Abc Def'|capfirst}}</p>
	<p>{{'abc Def'|capfirst}}</p>
	<p>{{menus|random}}</p>

	<hr>
	<h3>7. 연산</h3>
	<p>{{ 4|add:6 }}</p>

	<hr>
	<h3>8. 날짜 표현</h3>
	<!-- dtl의 주석처리는 %->#으로 둘 다 변경.	-->
	{{datetimenow}}
	{% now 'DATETIME_FORMAT' %}<br>
	{% now 'SHORT_DATETIME_FORMAT %}<br>
	{% now 'DATE_FORMAT' %}<br>
	{% now 'SHORT_DATE_FORMAT' %}<br>
	{% now "Y" as current_year %}<br>
	Copyright {{ current_year }}

	<hr>
	<h3>9. 기타</h3>
	<!--url을 만들어 줌.-->
	{{'google.com'|urlize}}
{% endblock %}
```

파이참 설정 file - settings - editor - general - ensure - line -feed at file end of save 설정

# 참고자료 180601

> - 장고 템플릿 Language1 : <https://docs.djangoproject.com/en/1.7/topics/templates/>
>- 장고 템플릿 Language2 : https://docs.djangoproject.com/en/2.2/topics/i18n/
> - ascii art 1 : <http://artii.herokuapp.com/>
>- ascii art 2 : <http://artii.herokuapp.com/fonts_list>
> - 프레임워크 순위 : <https://hotframeworks.com/> 언급된 수에 따라 순위가 적용됨.
>- 검색해볼 것. : csrf (2008년 옥션 해킹 사건.)
