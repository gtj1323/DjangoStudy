[TOC]

## 6.4. Django ORM, SQLite3
`pip install django`
`django-admin startproject crud .`
`python manage.py startapp boards`


### 6.4.1. ORM?

**※ ORM 이란?**
 ORM(Object-Relational Mapping)이란 단순히 말하면 객체와 관계의 설정. 여기서 관계는 개발자들이 사용하는 관계형 데이터베이스를 의미.
 관계를 이용하여 해당 개발언어를 이용하여 자동으로 Query문을 자동으로 작성, 개발을 손쉽게 해주는 Tool. 개발 언어를 이용하여 DB의CRUD가 가능해짐.

![151187385175F03A24](https://user-images.githubusercontent.com/43361320/58874442-c5852600-8703-11e9-9d3b-ca7c5c457c24.jpg)

**※ ORM 장점.**

- 객체 지향적인 코드로 인해 더 직관적이고 비즈니스 로직에 더 집중할 수 있게 도와준다.
  - 선언문, 할당, 종료 같은 부수적인 코드가 없거나 급격히 줄어든다.
  - 각종 객체에 대한 코드를 별도로 작성하기 때문에 코드의 가독성을 올려준다.
  - SQL의 절차적이고 순차적인 접근이 아닌 객체 지향적인 접근으로 인해 생산성이 증가한다.
- 재사용 및 유지보수의 편리성이 증가한다.
  - ORM은 독립적으로 작성되어있고, 해당 객체들을 재활용 할 수 있다.
  - 때문에 모델에서 가공된 데이터를 컨트롤러에 의해 뷰와 합쳐지는 형태로 디자인 패턴을 견고하게 다지는데 유리하다.
  - 매핑정보가 명확하여, ERD를 보는 것에 대한 의존도를 낮출 수 있다.
- DBMS에 대한 종속성이 줄어든다.
  - 대부분 ORM 솔루션은 DB에 종속적이지 않다.
  - 종속적이지 않다는것은 구현 방법 뿐만아니라 많은 솔루션에서 자료형 타입까지 유효하다.
  - 프로그래머는 Object에 집중함으로 극단적으로 DBMS를 교체하는 거대한 작업에도 비교적 적은 리스크와 시간이 소요된다.
  - 또한 자바에서 가공할경우 equals, hashCode의 오버라이드 같은 자바의 기능을 이용할 수 있고, 간결하고 빠른 가공이 가능하다.

**※ ORM 단점.**

-  ORM 으로만 완전한 서비스를 구현하기가 어렵다.
  - 사용하기는 편하지만 설계는 매우 신중하게 해야한다.
  - 프로젝트의 복잡성이 커질경우 난이도 또한 올라갈 수 있다.
  - 잘못 구현된 경우에 속도 저하 및 심각할 경우 일관성이 무너지는 문제점이 생길 수 있다.
  - 일부 자주 사용되는 대형 쿼리는 속도를 위해 SP를 쓰는등 별도의 튜닝이 필요한 경우가 있다.
  - DBMS의 고유 기능을 이용하기 어렵다. (하지만 이건 단점으로만 볼 수 없다 : 특정 DBMS의 고유기능을 이용하면 이식성이 저하된다.)
- 프로시저가 많은 시스템에선 ORM의 객체 지향적인 장점을 활용하기 어렵다.
  - 이미 프로시저가 많은 시스템에선 다시 객체로 바꿔야하며, 그 과정에서 생산성 저하나 리스크가 많이 발생할 수 있다.

**※ Django ORM**
- Django 에서는 ORM을 제공함. 이때 default로 사용하는 DB가 SQLite이다. 다른 SQL도 사용가능하지만, 추가적인 설정이 요구됨.

### 6.4.2. SQLite3 설치 및 설정.
- 설치
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
	7. git bash에서 `source ~/.bash_profile`  실행.
	8. `sqlite3` 실행시 `winpty sqlite3`와 똑같이 실행되면 정상작동.

- SQLite3 사용.
	1. `sqlite3 db.sqlite3`
	DB에 접속함.
	2. `.table`
	테이블 확인
	3. `.schema boards_board`
	boards_board 테이블의 스키마 확인.

### 6.4.3 Django ORM 사용.

#### 6.4.3.1. 기본 설정.

- settings.py에 보면.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# 이렇게 작성되어 있음.
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

> SQLite3 가 기본적으로 설정되어 있음. MySQL, Oracle 등등 다양하게 사용 가능하지만 추가적인 설정이 요구됨.

**USE_TZ=False**

> 모델에서도 사용자가 지정한 TIME_ZONE 값을 적용시기기 위해 False로 설정함.

#### 6.4.3.2. Django ORM으로 DDL, DCL, DML
DML DB를 조작하는 언어. CRUD
DCL 권한
DDL 테이블, 스키마 등등 DB의 논리구조를 정의하는 언어.

1. layout 작성
    모델을 정의하는 단계
    project명/models.py 에서 class를 작성하여 만들어 줌.
	
	- crud.py
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
		    update_at = models.DateTimeField(auto_now=True) # auto_now : 수정일자. DB가 새로 저장될 때마다 갱신.
		```
2. migration(설계도) 생성.
`python manage.py makemigrations`
명령을 통해서 해당 Application폴더에/migrations 폴더에 migration에 해당하는 .py 파일이 생성.
DB는 아직 생성되지 않음.
만약 모델을 수정하면 다시 명령을 실행하여 migraton을 만들어야함.
3. migration(설계도) 확인.
`python manage.py sqlmigrate boards 0002`
위 명령어를 실행하면 ORM이 DB로 넘길 SQL명령을 보여 줌.
4. migrate : DB 생성(테이블 생성)
`python manage.py migrate`
INSTALLED_APPS 에 요구되는 각각의 models의 migrate를 만들어야 하기때문에 여러개의 DB를 만들어 줌.
특정 앱을 선택할 수 있음. 뒤에 app이름을 써주면 됨.



# 참고자료 190604

> - SQLite 설치 : <https://www.sqlite.org/download.html>








