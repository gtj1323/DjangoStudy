[TOC]

## 6.4. Django ORM, SQLite3 개념 및 설정. (게시판 만들기 준비)

`pip install django`
`django-admin startproject crud .`
`python manage.py startapp boards`
settings.py - TEMPLATES - 'DIRS' : [os.path.join(BASE_DIR, 'crud', 'templates')] 추가.

### 6.4.1. ORM?

**※ ORM 이란?**
 ORM(Object-Relational Mapping)이란 단순히 말하면 객체와 관계의 설정. 여기서 관계는 개발자들이 사용하는 관계형 데이터베이스를 의미.
 *객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에 __(Django - SQL)데이터를 변환__하는 프로그래밍 기술.*
 관계를 이용하여 해당 개발언어를 이용하여 자동으로 Query문을 자동으로 작성, 개발을 손쉽게 해주는 Tool. 개발 언어를 이용하여 DB의CRUD가 가능해짐. '가상 객체 데이터베이스'를 만들어 사용함.
 OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지않는 데이터를 변환하는 프로그래밍 기법이다. 객체 관계 매핑이라고도 부른다.
 Flask에서는 SQLAlchemy, Django는 내장 ORM, Node.js에서 Sequalize ORM을 사용.

**DB---ORM---Python Class(models.py)**

![151187385175F03A24](https://user-images.githubusercontent.com/43361320/58874442-c5852600-8703-11e9-9d3b-ca7c5c457c24.jpg)

**※ ORM 장점.**

- **SQL을 몰라도 DB 연동이 가능**하다. (SQL 문법을 몰라도 쿼리 조작 가능)
- SQL의 절차적인 접근이 아닌 **객체 지향적인 접근**으로 인해 **생산성이 증가**한다.
- 매핑 정보가 명확하여 ERD를 보는 것에 대한 의존도를 낮출 수 있다.
- **ORM은 독립적으로 작성되어 있고, 해당 객체들을 재활용**할 수 있다. 때문에 모델에서 가공된 데이터를 컨트롤러(view)에 의해 뷰(template)과 합쳐지는 형태로 디자인 패턴을 견고하게 다지는데 유리하다.

**※ ORM 단점.**

- ORM 만으로 완전한 서비스를 구현하기 어렵다.
- 사용은 어렵지만 설계는 신중해야 한다.
- 프로젝트의 복잡성이 커질 경우 난이도가 상승할 수 있다.

**※ Django ORM**

- Django 에서는 ORM을 제공함. 이때 default로 사용하는 DB가 SQLite이다. 다른 SQL도 사용가능하지만, 추가적인 설정이 요구됨.

**※ 추가** - 객체 지향 프로그래밍(OOP, Object-Oriented Programming). 
 프로그램설계 방법론이자 개념의 일종. 프로그램을 수많은 '객체'라는 기본 단위로 나누고 이 객체들의 상호작용으로 서술하는 방식.
**※ 추가** - 관계형 데이터베이스 관리 시스템(RDBMS, Relational Database Management System)

### 6.4.2. SQLite3 설치 및 설정.

#### 6.4.2.1 SQLite3 window 설치 및 설정.

- 설치 window.
https://www.sqlite.org/download.html 의 Downloads 에서
Precompiled Binaries for Windows를 찾음.
	1. sqlite-dll-win64-x64-3280000.zip 와 sqlite-tools-win32-x86-3280000.zip 를 찾아서 다운받음.
	2. C:\sqlite 에 압축을 해제하여 넣음.
	4. C:\sqlite; 를 환경변수에 추가.
	5. git bash에서
`winpty sqlite3`명령을 실행하여
실행시 SQLite version 정보가 나타나면 정상 작동.
	6. `code ~/.bash_profile`에서
`alias sqlite3="winpty sqlite3"` 추가 (띄어쓰기 그대로.)
엘리어스 설정, winpty sqlite3 를 sqlite3로 줄이는 것.
	7. git bash에서 `source ~/.bash_profile`  실행.
	8. `sqlite3` 실행시 `winpty sqlite3`와 똑같이 실행되면 정상작동.

- SQLite3 사용 설정.
	1. `sqlite3 db.sqlite3`
	DB에 접속함. (나가는 명령 `.exit`)
	2. `.table`
	테이블 확인
	3. `.schema boards_board`
	boards_board 테이블의 스키마 확인.

#### 6.4.2.2 Django Database 설정.

Django DB 설정 참고 : <https://docs.djangoproject.com/ko/2.2/ref/settings/#std:setting-DATABASES>

### 6.4.3 Django ORM 사용.

#### 6.4.3.1. 기본 설정.

- settings.py에 보면.

	```python
	TEMPLATES = [
	    {
	        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	        'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')], # crud_intro/templates 사용
	        'APP_DIRS': True,
	        'OPTIONS': {
	            'context_processors': [
	                'django.template.context_processors.debug',
	                'django.template.context_processors.request',
	                'django.contrib.auth.context_processors.auth',
	                'django.contrib.messages.context_processors.messages',
	            ],
	        },
	    },
	]
	"""
	... 중간 생량 ...
	"""
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3', # Django ORM sqlite3 사용 설정.
	        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	    }
	}
	# 이렇게 작성되어 있음. 다른 SQL을 사용하려면 설정을 참고하여 수정하여야함.
	
	"""
	중략
	"""
	LANGUAGE_CODE = 'ko-kr'
	
	# template forms 에서 출력되는 시간.
	TIME_ZONE = 'Asia/Seoul'
	
	USE_I18N = True
	
	USE_L10N = True
	# 모델에서도 사용자가 지정한 TIME_ZONE 값을 적용시기기 위해 False로 설정함.
	USE_TZ = False
	"""
	생략
	"""
	```
	**sqlite3**
	> SQLite3 가 기본적으로 설정되어 있음.
	> MySQL, Oracle 등등 다양하게 사용 가능하지만 추가설정이 요구됨.
	
	**USE_TZ=False**
	
	> 모델에서도 사용자가 지정한 TIME_ZONE 값을 적용시기기 위해 False로 설정함.

#### 6.4.3.2. Django ORM으로 DDL, DCL, DML.
DML : DB를 조작하는 언어. CRUD
DCL : DB 접근, 수정 등의 권한
DDL : 테이블, 스키마 등등 DB의 논리구조를 정의하는 언어.

1. layout 작성(models.py 작성)
    모델을 정의하는 단계
    project명/models.py 에서 class를 작성하여 만들어 줌.
	
	- boards/models.py
		```python
	from django.db import models
		
		# Create your models here.
		class Board(models.Model):
		    # 각각이 DB에서 하나의 column이 됨. PK, Title, content, created_at
		
		    # id(PK)는 기본적으로 처음 테이블 생성시 자동으로 만들어짐.
		    # id = models.AutoField(primary_key=True)
		    title = models.CharField(max_length=10) # field에 길이 제한을 줌. max_length가 필수 인자.
		    content = models.TextField() # Text Area의 역할, 설정값이 존재하지만 필수인자는 없음.
		    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add는 생성 일자. DB가 최초 저장시에만 적용.     
		    updated_at = models.DateTimeField(auto_now=True) # auto_now : 수정일자. DB가 새로 저장될 때마다 갱신.
		```
		
		**class Board(models.Model)**
		
		> 모델을 정의. 각 모델은 django.db.models.Model 클래스의 서브클래스로 표현.
		> 각 클래스의 변수는 모델의 데이터베이스 필드를 나타냄.
		> 기본 Not Null 조건이 붙음.
		> id라는 PK 자동으로 생성.
		
		**models.CharField(max_length=None, \*\*options)**
		
		> max_length는 필수 인자.
		> 필드의 최대 길이(문자 수)를 정의 하여 유효성 검사에 사용.
		> 기본 양식 위젯은 TextInput
		
		**models.TextField()**
		
		> A larget size text field.
		> max_length 옵션을 주면 자동양식필드의 textarea 위젯에 반영, 데이터베이스 수준에는 적용되지 않음.
		> 기본 양식 위젯은 Textarea
		
		**models.DateTimeField(auto_now=False, auto_now_add=False, \*\*options)**
		
		> - 생성일자 : auto_now_add=True
		> DB가 최초 저장시에만 현재날짜로 1번 저장.
		>
		> - 수정일자 : auto_now=True
		> DB가 새로 저장될 때마다 현재날짜로 갱신.(업데이트되면 갱신됨.)
		>   
2. migration(설계도) 생성.
`python manage.py makemigrations`
명령을 통해서 해당 'Application폴더'/migrations 폴더에 migration에 해당하는 .py 파일이 생성.
DB는 아직 생성되지 않음.
만약 모델을 수정하면 다시 명령을 실행하여 migraton을 만들어야함.
3. migration(설계도) 확인.
    `python manage.py sqlmigrate boards 0002`
    위 명령어를 실행하면 ORM이 DB로 넘길 SQL명령을 보여 줌.

4. migrate : DB 생성(테이블 생성)
    `python manage.py migrate`
    INSTALLED_APPS 에 요구되는 각각의 models의 migrate를 만들어야 하기때문에 여러개의 DB를 만들어 줌.
    특정 앱을 선택할 수 있음. 뒤에 app이름을 써주면 됨.

#### 6.4.3.3. Djnago ORM을 통해서 DB 조작 1 Create.

- cmd 명령.
	```python
	$ python manage.py shell
	Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	(InteractiveConsole)
	>>> from boards.models import Board
	>>> Board.objects.all() # (SQL에서 SELECT * boards_board 와 같은 역할을 해줌. 테이블 조회)
	<QuerySet []>
	>>> board = Board()
	>>> board.title = 'first' # 인스턴스 객체 board로 인스턴스 변수(title)에 값('first')을 할당. 쉽게 말하면 게시글의 제목을 'first'로 작성한 것.
	>>> board.content = 'django!'
	>>> board # 여기까지는 아직 작성이 안된 것!
	<Board: Board object (None)>
	>>> board.save() # 작성된 내용을 완료를 누르는 과정으로 보면 됨.
	>>> board
	<Board: Board object (1)>
	>>> board = Board(title='second', content='django!!!')
	>>> board.save()
	>>> Board.objects.all()
<QuerySet [<Board: Board object (1)>, <Board: Board object (2)>]>
	>>> Board.objects.create(title='third', content='django!!') # .save()의 기능을 포함하고 있음. 검증을 하지 않고 넘어가기 때문에 사용이 어려움.
<Board: Board object (3)>
	>>> board = Board()
	>>> board.title = 'fourth'
	>>> board.content='django!!!!'
	>>> board.id # 아직 작성된 것이 아니므로 아무것도 나오지 않음.
	>>> board.save() # 작성을 완료함.
	>>> board.id # 작성이 완료된 상태임으로 id가 출력됨.
	4
	>>> board.created_at
	datetime.datetime(2019, 6, 5, 10, 19, 17, 920164)
	>>> board.title = 'asldkfj;aldfkja;dlfkalsdf;alskdjfj'
	>>> board.full_clean() # 유효성 검증
	Traceback (most recent call last):
	  File "<console>", line 1, in <module>
	  File "C:\Users\student\PycharmProjects\crud_intro\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
	    raise ValidationError(errors)
	django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 34 자).'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
	>>> Board.objects.all() # 데이터 조회
	<QuerySet [<Board: Board object (1)>, <Board: Board object (2)>, <Board: Board object (3)>, <Board: Board object (4)>]>
	>>> exit() # 파이썬 종료.
	```

	**python manage.py shell**
	
	> 일반 파이썬 쉘을 통해서는 장고프로젝트 환경에 접근이 불가능함.
	> Django 프로젝트 환경에서 파이썬 쉘을 활용한다고 보면 됨.
	> Django shell에서는 python인터프리터와 다름.
	> Django에서 동작하는 모든 명령을 그대로 테스트할 수 있음.
	> 실제 데이터를 조작하면 장고 프로젝트에도 반영된다.
	
	**from boards.models import Board**
	> Board 모델을 가져옴.
	
	**board.objects.all()**\
	
	> 해당 테이블의 **모든 객체를 Set으로 가져옴.**
	> 각각의 1개 데이터는 모델의 \_\_str\_\_(self) 함수에서 리턴하는 값으로 출력됨.
	
	**※ DB에 데이터 입력 1**
	
	> ```python
	> board = Board()
	> board.title = 'first' # 인스턴스 객체 board로 인스턴스 변수(title)에 값('first')을 할당.
	> 					  # 쉽게 말하면 게시글의 제목을 'first'로 작성한 것.
	> board.content = 'django!'
	> # board # 여기까지는 아직 작성이 안된 것!
	> # board를 출력하면 <Board: Board object (None)>가 출력됨. (HDD에 적용안되어 있음.)
	> # (__str__(self) 함수에서 리턴하는 값으로 출력.)
	> board.save() # 작성된 내용을 완료를 누르는 과정으로 보면 됨.
	> # board를 출력하면 <Board: Board object (1)>가 출력됨. (HDD에 적용됨.)
	> # (__str__(self) 함수에서 리턴하는 값으로 출력.)
	> # Set이 아닌 1개의 행을 객체로 가지고 있음.
	> ```
	> 반드시 board.save() 를 해주어야 HDD에 적용됨.
> 1개의 행을 객체로 가짐.
	> 여기서 title, content는 DBmodel 설계시 작성한 것들.

	**※ DB에 데이터 입력 2**
	
	> ```python
	> board = Board(title='second', content='django!!!')
	> board.save()
	> ```
	> 반드시 board.save() 를 해주어야 HDD에 적용됨.
	> 1개의 행을 객체로 가짐.
	> 여기서 title, content는 DBmodel 설계시 작성한 것들.
	
	**※ DB에 데이터 입력 3**
	> ```python
	> Board.objects.create(title='third', content='django!!')
	> **board.save() 필요 없음 !!!!**
	> 검증을 하지 않기 때문에 사용에 어려움이 있을 수 있다.
	> 1개의 행을 객체로 가짐.
	> 여기서 title, content는 DBmodel 설계시 작성한 것들.
	> ```
	
	**board.save()**
	
	> 수정한 데이터를 하드디스크에 적용하는 작업을 함. DB의 commit명령을 내려줌.
	
	**board.id()**
	> 모델에서 가지는 PK. HDD에 적용된 상태여야 출력됨.
	
	**board.board.full_clean()**
	
	> 유효성 검증함. DB설계시에 만들었던 제약조건에 맞는지 확인.
#### 6.4.3.4. Django ORM을 통해서 DB 조작 2 Read, Delete, Update.

- cmd 명령.

	```python
	'''
	boards/models.py의 Board 클래스에 아래 함수 추가.
	def __str__(self):
	    return f'{self.id}글 - {self.title}: {self.content}'
	# 내용 추가 Set이 아닌 객체를 출력시 해당 함수의 형태를 따름.
	'''
	
	$ python manage.py shell
	Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	(InteractiveConsole)
	>>> from boards.models import Board
	>>> Board.objects.all() # 템플릿에서도 출력되는 형식이므로  바꾸는 것이 좋음.
	<QuerySet [<Board: 1글 - first: django!>, <Board: 2글 - second: django!!!>, <Board: 3글 - third: django!!>, <Board: 4글 - fourth: django!!!!>]>
	>>> boards = Board.objects.filter(title='hello') # filter는 sql의 where 역할.SELCT * FROM boards WHERE title='hello'
	>>> boards
	<QuerySet []>
	>>> boards = Board.objects.filter(title='first') # 1라도 쿼리셋으로 가져옴.
	>>> boards
	<QuerySet [<Board: 1글 - first: django!>]>
	>>> board = Board.objects.filter(title='first').first() # 
	>>> board
	<Board: 1글 - first: django!>
	>>> board = Board.objects.get(id=1) # 반드시 1개만 존재함.Board객체 1개 리턴.
	>>> board
	<Board: 1글 - first: django!>
	>>> board = Board.objects.get(pk=1) # pk와 id는 같음.
	>>> board
	<Board: 1글 - first: django!>
	>>> boards = Board.objects.filter(id=1) # filter를 사용하기 때문에 boardSet이 리턴.
	>>> boards
	<QuerySet [<Board: 1글 - first: django!>]>
	>>> boards = Board.objects.filter(title__contains='fi') # fi 포함하는 Set 리턴
	>>> boards
	<QuerySet [<Board: 1글 - first: django!>]>
	>>> boards = Board.objects.filter(content__endswith='!') # startswith 도 있음.
	>>> boards
	<QuerySet [<Board: 1글 - first: django!>, <Board: 2글 - second: django!!!>, <Board: 3글 - third: django!!>, <Board: 4글 - fourth: django!!!!>]>
	>>> boards = Board.objects.order_by('title') # title 순서대로 배치
	>>> boards
	<QuerySet [<Board: 1글 - first: django!>, <Board: 4글 - fourth: django!!!!>, <Board: 2글 - second: django!!!>, <Board: 3글 - third: django!!>]>
	>>> boards = Board.objects.order_by('-title') # title 역순으로 배치
	>>> boards
	<QuerySet [<Board: 3글 - third: django!!>, <Board: 2글 - second: django!!!>, <Board: 4글 - fourth: django!!!!>, <Board: 1글 - first: django!>]>
	>>> boards[1] # 1개만 잘라서 가져오는 것 가능.
	<Board: 2글 - second: django!!!>
	>>> boards[1:3] # 슬라이싱 가능.
	<QuerySet [<Board: 2글 - second: django!!!>, <Board: 4글 - fourth: django!!!!>]>
	>>> board = Board.objects.get(pk=1)
	>>> board
	<Board: 1글 - first: django!>
	>>> board.title
	'first'
	>>> board.title = 'byebye' # 제목을 수정함.
	>>> board.save() # board 객체에 id가 없을 때는 create(추가), 있으면 수정(update)
	>>> board.title
	'byebye'
	>>> board = Board.objects.get(pk=1)
	>>> board.delete() # 해당 보드를 삭제함.
	(1, {'boards.Board': 1})
	>>> board = Board.objects.get(pk=1) # 삭제되었기 때문에 나오지 않음.
	Traceback (most recent call last):
	  File "<console>", line 1, in <module>
	  File "C:\Users\student\PycharmProjects\crud_intro\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
	    return getattr(self.get_queryset(), name)(*args, **kwargs)
	  File "C:\Users\student\PycharmProjects\crud_intro\venv\lib\site-packages\django\db\models\query.py",
	line 408, in get
	    self.model._meta.object_name
	boards.models.Board.DoesNotExist: Board matching query does not exist.
	>>> board = Board.objects.get(pk=2)
	>>> dir(board) # 사용 가능한 기능들 확인.
	['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 	'_check_column_name_clashes', '_check_constraints', '_check_field_name_clashes', '_check_fields', '_check_id_field', 	'_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', 	'_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes',
	'_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', 	'_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'check', 'clean', 'clean_fields', 'content', 'created_at', 'date_error_message', 'delete', 'from_db', 'full_clean', 'get_deferred_fields', 'get_next_by_created_at', 'get_next_by_updated_at', 	'get_previous_by_created_at', 'get_previous_by_updated_at', 'id', 'objects', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'title', 'unique_error_message', 'updated_at', 'validate_unique']
	```
**board.objects.filter(조건.)**
	
	>**filter명령은 객체 Set을 가져오는 것을 기본으로 함.**
	>해당 table에서 title이 hello인 모든 데이터를 Set으로 리턴.
	>filter는 sql의 where 역할.
	>위 명령어는SELCT * FROM boards WHERE title='hello'
	>1개여도 Set으로 리턴.
	>
	>__***filter의 ()안에 들어갈 수 있는 조건.***__
	>>(title='hello') : title='hello'인 Set
	>>(id=1) : id=1 인 Set
	>>(title\_\_contains='fi') : title에 'fi'를 포함하는 Set
	>>(content\_\_endswith='!') : title 끝에 '!'인 객체 Set
	>>(content\_\_startswith='!') : title 시작에 '!'인 객체 Set'

	**board.objects.filter(title='hello').first()**

	> **1개의 객체를 가져옴.**
	> 해당 table에서 title이 hello인 모든 데이터 중 첫번째 것을 객체로 리턴.

	**Board.objects.order_by('title')**
	
	>객체Set을 title의 이름 순으로 정렬.
	
	**boards = Board.objects.order_by('-title')**
	
	>객체Set을 title의 이름 역순으로 정렬.
	
	**board.objects.get(조건.)**
	
	>**get은 반드시 객체로 가져옴.**
	>
	>__***filter의 ()안에 들어갈 수 있는 조건.***__
	>
	> (pk=1) : pk가 1인 객체.
	>

	**※ 객체Set 다루기**
	
	> boards라는 객체 Set을 가지고 있을 때 사용.
	> `boards[1]` : 1개만 잘라서 **객체로 가져옴**.
	> `boards[1:3]` : 1~3을 잘라서 **Set으로 가져옴**.

	**※ 객체 다루기**
	> board라는 객첼르 가지고 있을 때 사용.
	> `board.title='byebye'` : 해당 객체를 'byebye'로 수정. 
	> `board.save()` : 수정한 용을 적용.
	> 
	>`board.delete()` : 해당객체를 삭제함. board.save()가 필요 없음.
	
	**dir(board)**
	
	>사용가능한 명령 확인.


### 6.4.4. SQLite3 직접 사용.
- cmd 명령창

  ```sqlite
  $ sqlite3 db.sqlite3
  SQLite version 3.28.0 2019-04-16 19:49:53
  Enter ".help" for usage hints.
  sqlite> .tables
  auth_group                  boards_board
  auth_group_permissions      django_admin_log
  auth_permission             django_content_type
  auth_user                   django_migrations
  auth_user_groups            django_session
  auth_user_user_permissions
  sqlite> SELECT * FROM boards_board;
  1|first|django!|2019-06-05 09:53:16.104164|2019-06-05 09:53:16.104164
  ```
	**sqlite3 db.sqlite3**
	> sqlite3 실행
	> pycharm은 내부적으로 가상환경이 만들어져 있기 때문에 **db.sqlite3**를 실행시켜야함.
	> (파일 존재)
	
	**.table**
	
	> 현재 존재하는 table 목록 확인

### 6.4.5. 관리자 생성 및 설정.

- cmd 명령.
  `python manage.py createsuperuser` : ORM을 통해 superuser를 생성함.
  관리자 ID, Email, Password를 정해줌.

- cmd 명령.

	```
	$ sqlite3 db.sqlite3
	SQLite version 3.28.0 2019-04-16 19:49:53
	Enter ".help" for usage hints.
	sqlite> .tables
	auth_group                  boards_board
	auth_group_permissions      django_admin_log
	auth_permission             django_content_type
	auth_user                   django_migrations
	auth_user_groups            django_session
	auth_user_user_permissions
	sqlite> SELECT * FROM auth_user;
	1|pbkdf2_sha256$150000$zaatYSXuQ8hi$8UJgjoe7gstAITkg1X8jMOCeJ1nLEXTJ3o8cObfN+PU=||1|123123|||1|1|2019-06-05 14:05:36.289022|
	```
	**SELECT * FROM auth_user;**

	> 권한을 가진 유저 정보를 나타냄.

- boards/admin.py 에 등록을 해야 사용할 수 있음.
	```python
	from django.contrib import admin
	from .models import Board # 관리자가 사용할 모델 등록.
	
	# Register your models here.
	class BoardAdmin(admin.ModelAdmin):
	    list_display = ['pk', 'title', 'content', 'created_at', 'updated_at',]
	admin.site.register(Board) # 관리자에게 모델을 사용가능한 상태로 만들어 줌.
  ```
	**admin.site.register(Board)**
	> 관리자가 해당 모델을 사용가능한 상태로 만들어 줌.
	
	**class BoardAdmin(admin.ModelAdmin)**
	
	>관리자로 접속하여 table관리 시 col을 나누어줌.

## 6.5. Django ORM, SQLite3 활용. (게시판 만들기 실습)

### 6.5.1. index 페이지.

- views.py 에 추가.
  ```python
  def index(request):
      boards = Board.objects.all()
    context = {'boards':boards}
	    return render(request, 'boards/index.html', context)
	```
	
- boards/urls.py 에 urlpatterns list에 추가.
  ```python
  path('',views.index),
  ```

- boards/templates/boards/index.html
  ```django
  {% extends "base.html" %}
  {% block content %}
   <h1>BOARD Main Page!</h1>
	   {% for board in boards%}
	    <p>{{board.pk}} : <a href="/boards/{{board.pk}}/">{{board.title}}</a>  / {{board.created_at|timesince}}</p>
	    <hr>
	   {% endfor %}
	    <a href="/boards/new/">글 작성</a>
	{% endblock %}
	```
	

### 6.5.2. 새로 글 쓰기.

- views.py 에 추가.
  ```python
  # 1. 글을 작성하는 페이지를 render 할 view 함수
  def new(request):
      return render(request, 'boards/new.html')
  
  # 2. DB에 값을 저장해주는 view 함수 필요.
  def create(request):
      board = Board()
      # new에서 넘어오는 제목과 내용을 저장
      title = request.POST.get('title') # 글 제목을 받아옴.
      content = request.POST.get('content')
      print(f'title = {title}')
      print(f'content = {content}')
      # orm title 과 content에 위에서 넘어온 값을 저장.
      board.title = title
      board.content = content
      # board = Board(title=title, content=content)
      # board.save()
      # Board.objects.create(title=title, content=content) # .save기능 포함
      # DB에 저장.
      board.save()
      id = board.id
      print(f'id={id}')
      # detail.html 페이지를 render
      print('성공.')
      return redirect(f'/boards/{board.pk}')
  ```
  
- boards/urls.py 에 urlpatterns list에 추가.
  ```python
  path('new/', views.new),
  path('create/', views.create),
  ```
  
- boards/templates/boards/new.html
  ```django
  {% extends "base.html" %}
  {% block content %}
     <h1>NEW 새로운 글을 작성</h1>
      <form action="/boards/create/" method="POST">
          {% csrf_token %}
          <label for="title">TITLE</label><!-- for에 inputlabel을 줌. -->
          <input id="title" type="text" name="title">10글자 이하.<br>
          <label for="content">CONTENT</label>
          <textarea id="content" name="content" col="30" row="10"></textarea><br>
          <input type="submit" value="작성">
      </form>
      <a href="/boards/">목록으로</a>
  {% endblock %}
  ```

	**from django.shortcuts import render, redirect**
	> 글 작성 후 바로 작성된 글을 확인하기 위해서는 redirect를 사용해야함.

	**redirect(f'/boards/{board.pk}')**
	
	> 해당 URL로 보냄.

### 6.5.3. 세부내용 보기.

- views.py 에 추가.
  ```python
  def detail(request, pk):
      # 요청으로 들어온 pk 값으로 해당 글을 찾아옴.
    board = Board.objects.get(pk=pk)
      context = {
          'board':board,
      }
      return render(request, 'boards/detail.html', context)
  ```
  
- boards/urls.py 에 urlpatterns list에 추가.
  
  ```python
  path('<int:pk>/',views.detail)
  ```


- boards/templates/boards/index.html
  ```django
  {% extends "base.html" %}
  {% block content %}
      <h1>DETAIL</h1>
      <p>{{board.pk}}</p>
      <hr>
      <p>{{board.title}}</p>
      <p>{{board.content}}</p>
      <p>{{board.created_at}}</p>
      <p>{{board.updated_at}}</p>
      <a href="/boards/">목록으로</a>
  {% endblock %}
  ```

### 6.5.4. 관리자

## 6.5. Django_extention.

기본 기능보다 향상된 확장 기능들을 제공함.

### 6.5.1. Django_extention 설치 및 사용 설정.

- 설치
  `pip install django_extensions` 설치

- crud/settings.py 에 사용 설정.
	
	```python
	INSTALLED_APPS = [
	    # first part apps
	    'boards.apps.BoardsConfig',
	    
	    # thrid part apps
	    'django_extensions', # 위치 중요. Django_extention 사용 설정.
	    
	    # django part apps
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	]
	```

- shell_plus

  - 기본 django-shell 보다 편리한 확장프로그램.
  - shell이 실행되면 현재 프로젝트에서 **사용하고 있는 모든 모듈을 자동으로 import**
  ```python
  $ python manage.py shell_plus
  # Shell Plus Model Imports
from django.contrib.admin.models import LogEntry
  from django.contrib.auth.models import Group, Permission, User
  from django.contrib.contenttypes.models import ContentType
  from django.contrib.sessions.models import Session
  from boards.models import Board
  # Shell Plus Django Imports
  from django.core.cache import cache
  from django.conf import settings
  from django.contrib.auth import get_user_model
  from django.db import transaction
  from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch,
  Q, Sum, When, Exists, OuterRef, Subquery
  from django.utils import timezone
  from django.urls import reverse
  Python 3.6.7 (default, Dec 9 2018, 17:28:26)
  [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)] on
  darwin
  Type "help", "copyright", "credits" or "license" for more information.
  (InteractiveConsole)
  >>>
  ```
  





---


# 참고자료 190604, 190605

> - SQLite 설치 : <https://www.sqlite.org/download.html>
> - Dango DB 설정 : <https://docs.djangoproject.com/ko/2.2/ref/settings/#std:setting-DATABASES>
> - Django_extention Doc : <https://django-extensions.readthedocs.io/>
