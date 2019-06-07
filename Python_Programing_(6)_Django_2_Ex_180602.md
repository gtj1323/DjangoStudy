[TOC]

## 6.4. Django Framework예제 모음. books application

- 강의에서 2번째로 만들었던 `books` app 을 이용해 다양한 실습을 진행해보자.

`pip install django
django-admin startproject intor .`
두개는 했다고 보고 실행.

`python manage.py startapp books`
`python manage.py runserver`
intro\settings.py에 `'books.apps.BooksConfig',` 등록
intro\urls.py 에 urlpatterns에 `path('books/', include('books.urls')),` 등록

### - url 정보

|        url        |                           기능                            |
| :---------------: | :-------------------------------------------------------: |
|      books/       |                     종합 메인 페이지                      |
| books/graduation/ |       우리의 수료날(190627)까지 남은 날짜 출력하기        |
| books/imagepick/  |        Lorem Picsum 활용하여 랜덤 이미지 출력하기         |
|   books/today/    | 오늘 시간 및 날씨 정보 알려주기 (지금 살고 위치 기준으로) |
| books/ascii_new/  |       ascii art 를 변환을 위한 text, font 입력받기        |
| books/ascii_make/ |       artii 를 활용하여 art 로 만들어서 출력해주기        |
|  books/original/  |             영어 번역을 위한 한국어 입력받기              |
| books/translated/ |             papago 활용하여 한-영 번역 해주기             |


### - 활용 정보

> 필요한 모듈 : requests / os / datetime
>
> - `index.html`
>
> 	```django
> 	{% extends "base.html" %}
> 	{% block content %}
>	 	   	<h1>유틸리티</h1>
>	    	<a href="/books/graduation/">수료까지 남은 시간</a><br>
>	    	<a href="/books/imagepick/">랜덤이미지</a><br>
>	    	<a href="/books/today/">오늘 날씨</a><br>
>	    	<a href="/books/ascii_new/">아스키 코드 변환기</a><br>
>	    	<a href="/books/original/">파파고 번역기</a>
> 	{% endblock %}
> 	```

#### 답

- books/views.py 에 추가될 내용.
	```python
	# Create your views here.
	def index(request):
	    return render(request, 'books\index.html')
	```

- books/urls.py
	```python
	path('', views.index),
	```

- templates/books/index.html

	```django
	{% extends "base.html" %}
	{% block content %}
	   <h1>유틸리티</h1>
	   <a href="/books/graduation/">수료까지 남은 시간</a><br>
	   <a href="/books/imagepick/">랜덤이미지</a><br>
	   <a href="/books/today/">오늘 날씨</a><br>
	   <a href="/books/ascii-new/">아스키 코드 변환기</a><br>
	   <a href="/books/original/">파파고 번역기</a>
	{% endblock %}
	```

---

### 6.4.1. 수료날

- datetime 연산을 사용해 오늘 시점부터 수료날 까지의 남은 시간을 출력하라

#### 답

- books/views.py 에 추가될 내용.

	```python
	#우리의 수료날(190627)까지 남은 날짜 출력하기
	def graduation(request):
	    now = datetime.now()
	    end = datetime(2019, 6, 27, 1, 26, 55, 731039)
	    date= end - now
	    context={
	        'now':now,
	        'date': (date.days+1),
	        'end': end,
	    }
	    return render(request, 'books\graduation.html', context)
	```

- books/urls.py
	```python
	path('graduation/', views.graduation),
	```

- templates/books/.html
	```django
	{% extends "base.html" %}
	{% block content %}
	   <h1>오늘{{now}}부터 졸업{{둥}}까지 남은 날짜.</h1>
	   <p>{{date}}</p>
	   {{end|timeuntil:now}}
	{% endblock %}
	```

---

### 6.4.2. 랜덤 이미지

> https://picsum.photos/500/500/?random

- lorem picsum 을 사용

- 다음의 url 설정을 통해 이미지를 만들어주기.

  ```
  https://picsum.photos/500/500/?random
  ```

#### 답

- books/views.py 에 추가될 내용.

	```python
	# Lorem Picsum 활용하여 랜덤 이미지 출력하기
	def imagepick(request):
	    return render(request, 'books\imagepick.html')
	```

- books/urls.py
	```python
	path('imagepick/', views.imagepick),
	```

- templates/books/.html
	```django
	{% extends "base.html" %}
	{% block content %}
	   <h1>랜덤 그림 가져오기.</h1>
	   <img src="https://picsum.photos/500/500/?random">
	{% endblock %}
	```

---

### 6.4.3. 날씨 API

> API 정보 - https://openweathermap.org/current
>
> - 동시에 여러 명이 API 발급을 할 경우 일부 인원은 API 인증에 시간이 소요될 수 있습니다.
> - key 를 받은 뒤에도 어느정도 시간이 필요한 경우도 있습니다.
>
> - 요청 url
>
> ```python
> url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID=" + key
> ```

- API 정보를 바탕으로 날씨상태 / 현재온도 / 최고온도 / 최저온도를 출력하시오

#### 답

- books/views.py 에 추가될 내용.

	```python
	# 오늘 시간 및 날씨 정보 알려주기 (지금 살고 위치 기준으로)
	def today(request):
	    key = '6f2daf96185ad766c18830219fd6b641'
	    url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID=" + key
	    req = requests.get(url).json()
	    print("req['main']['temp_min']", req['main']['temp_min'])
	    context={
	        "status": req['weather'][0]['description'],
	        "temp_min": round(req['main']['temp_min']-273.15, 1),
	        "temp_max": round(req['main']['temp_max']-273.15,1),
	        "temp": round(req['main']['temp']-273.15,1),
	    }
	    return render(request, 'books\\today.html', context)
	```

- books/urls.py
	```django
	path('today/', views.today),
	```

- templates/books/today.html
	```django
	{% extends "base.html" %}
	{% block content %}
	   <h1>날씨.</h1>
	   "temp_min": {{temp_min}},
	   <br>
	   "temp_max": {{temp_max}},
	   <br>
	   "temp": {{temp}},
	   <br>
	{% endblock %}
	```

---

### 6.4.4. ASCII art

- 사용자로부터 입력 받을 때, font는 아래 중에서 선택할 수 있게 하기 (dropdown 형식)

  ```python
  fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
  ```

- 해당 url 이용하기

  ```
  http://artii.herokuapp.com/make?text=ASCII&font=short
  ```

#### 답

- books/views.py 에 추가될 내용.
	```python
	# ascii art 를 변환을 위한 text, font 입력받기
	def ascii_new(request):
	    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
	    context = {
	        'fonts':fonts,
	    }
	    return render(request, 'books\\ascii_new.html', context)
	
	# artii 를 활용하여 art 로 만들어서 출력해주기
	def ascii_make(request):
	    text = request.GET.get('text')
	    font = request.GET.get('font')
	    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
	    result = requests.get(url).text
	    context={
	        'result': result
	    }
		return render(request, 'books\\ascii_make.html', context)
	```

- books/urls.py
	```python
	path('ascii-new/', views.ascii_new),
	path('ascii-make/', views.ascii_make),
	```

- templates/books/ascii_new.html
	```django
	{% extends "base.html" %}
	{% block content %}
	   <h1>아스키 코드로 변환시켜 봅시다. Ascii_new.</h1>
	   <form action="/books/ascii-make/">
	      <input type="text" name="text">
	      <select name="font">
	         {% for font in fonts %}
	            <option vlaue="{{font}}">{{font}}</option>
	         {% endfor %}
	      </select>
	      <input type="submit" value="만들기">
	   </form>
	<a href="/books">back</a>
	{% endblock %}
	
	```
	
- templates/books/ascii_make.html
	```django
	{% extends "base.html" %}
	{% block content %}
	   <h1>아스키 코드로 변환시켜 봅시다. Ascii_make.</h1>
	   <pre>{{result}}</pre>
	{% endblock %}
	```

---

### 6.4.5. 파파고 번역

> 네이버 파파고(NMT) 활용하기
>
> https://developers.naver.com/docs/nmt/reference/
>
> api 등록 시 웹 서비스 URL 설정 - http://127.0.0.1:8000
>
> **api key 는 환경변수를 통해 가리기**
>
> - `~/.bash_profile`
>
> ```bash
> export NAVER_CLIENT_ID="04_JhV7aah3EvgAa8HL4"
> export NAVER_CLIENT_SECRET="3WGL522B80"
> ```
>
> ```bash
> $ source ~/.bash_profile
> ```

- 파파고 API 를 통해 한-영 번역하기

  ```python
  naver_client_id = os.getenv("NAVER_CLIENT_ID")
  naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
  
  papago_url = "https://openapi.naver.com/v1/papago/n2mt"
  
  # 네이버에 Post 요청을 위해서 필요한 내용들
  headers = {
    "X-Naver-Client-Id": naver_client_id,
    "X-Naver-Client-Secret": naver_client_secret
  }
  
  data = {
    "source": "ko",
    "target": "en",
    "text": korean
  }
  
  papago_response = requests.post(papago_url, headers=headers, data=data).json()
  english = papago_response["message"]["result"]["translatedText"]
  ```
  
- books 파일구조

  ```
  .
  ├── books
  │   ├── __init__.py
  │   ├── admin.py
  │   ├── apps.py
  │   ├── migrations
  │   ├── models.py
  │   ├── templates
  │   │   └── books
  │   │       ├── ascii_make.html
  │   │       ├── ascii_new.html
  │   │       ├── graduation.html
  │   │       ├── imagepick.html
  │   │       ├── index.html
  │   │       ├── original.html
  │   │       ├── today.html
  │   │       └── translated.html
  │   ├── tests.py
  │   ├── urls.py
  │   └── views.py
  └── manage.py
  ```

#### 답

- books/views.py 에 추가될 내용.
	```python
	# 영어 번역을 위한 한국어 입력받기
	def original(request):
	    return render(request, 'books\original.html')
	
	# papago 활용하여 한-영 번역 해주기
	def translated(request):
	    korean = request.GET.get('text')
	    naver_client_id = os.getenv("NAVER_CLIENT_ID")
	    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
	
	    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
	
	    # 네이버에 Post 요청을 위해서 필요한 내용들
	    headers = {
	        "X-Naver-Client-Id": naver_client_id,
	        "X-Naver-Client-Secret": naver_client_secret
	    }
	
	    data = {
	        "source": "ko",
	        "target": "en",
	        "text": korean
	    }
	    papago_response = requests.post(papago_url, headers=headers, data=data).json()
	    english = papago_response["message"]["result"]["translatedText"]
	
	    context = {
	        'korean': korean,
	        'english': english,
	    }
	    return render(request, 'books/translated.html', context)
	```

- books/urls.py
	```python
	path('original/', views.original),
	path('translated/', views.translated),
	```

- templates/books/original.html
	```django
	{% extends "base.html" %}
	{% block content %}
	   <h1>한글을 작성하여 번역하여 봅시다. original.</h1>
	   <form action="/books/translated/">
	      <input type="text" name="text">
	      <input type="submit" value="만들기">
	   </form>
	<a href="/books">back</a>
	{% endblock %}
	```
	
- templates/books/translated.html
	```django
	{% extends "base.html" %}
	{% block content %}
	   <h1>한글을 작성하여 번역하여 봅시다. translated.</h1>
	   <p>원문 : {{korean}}</p>
	   <p>번역 : {{english}}</p>
	{% endblock %}
	```

---

## Postman 사용법

1. 설치
2. 전송방법 선택(GET, POST 등)
3. URL 입력
4. GET 방식 : 전송방법에 따라 KEY, VALUE입력 자동으로 입력됨.
	POST방식 : HEADERS에 요구되는 BODY와 KEY와 VALUE를 입력
5. SEND하면 결과값을 돌려받아줌.



**EX) 네이버 파파고 API를 Postman에서 사용하는 방법.**

- 네이버 API 파파고 : HEADERS

	| KEY                   | VALUE                                        |
	| --------------------- | -------------------------------------------- |
	| X-Naver-Client-Id     | '네이버에서 어플리케이션을 등록하고 받은 ID'       |
	| X-Naver-Client-Secret | '네이버에서 어플리케이션을 등록하고 받은 Password' |

- 네이버 API 파파고 : BODY (x-www-form-urlencoded 선택)

	| KEY     | VALUE            |
	| ------- | ---------------- |
	| source  | ko               |
	| target  | en               |
	| text    | '번역하고 싶은 말' |