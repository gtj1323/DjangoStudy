[TOC]

## 8. 관리자 생성 및 설정.

Django 에서는 기본적인 관리자 페이지가 이미 다 만들어져 있기 때문에 이를 그냥 사용하면 된다.

- 관리자를 생성
  `python manage.py createsuperuser` : ORM을 통해 superuser를 생성함.
  관리자 ID, Email, Password를 정해줌.

- 관리자 권한을 가진 유저 확인.

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

- 관리자 Customizing 하기.

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

  > 관리자로 접속하여 table관리 시 col을 나누어줌.



## 9. URL namespace 만들기.

앱에서 이름 중복을 피하기 위해서 각 앱의 namesapce를 지정해 줄 수 있다.
- app_name/urls.py 에서 app의 namesapce 지정해줄 수 있다..
	```python
	app_name = 'motion_app'
	urlpatterns = [
	    path('motion/', views.motion, name='motion')
	]
	```
	
	여기서 app_name과 name이 앞으로 사용할 어플리케이션에서 해당 app의 namespace에 해당한다.

- views.py 에서 namespace 사용하기.

  ```python
  def method(request):
      return redirect('motion_app:motion')
  ```

- .html 파일에서 namespace 사용하기.

  ```django
  {% url 'motion_app:motion' %}
  ```

  위와 같은 방법으로 마치 C++의 namesapce를 사용하듯 사용이 가능하다.



## 10. Django_extensions.

기본 기능보다 향상된 확장 기능들을 제공함.

### 10.1. Django_extensions 설치 및 사용 설정.

- 설치 `pip install django_extensions` 설치

- crud/settings.py 에 사용 설정.

  ```
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

10.1. Django_extensions

- shell_plus

  - 기본 django-shell 보다 편리한 확장프로그램.
  - shell이 실행되면 현재 프로젝트에서 **사용하고 있는 모든 모듈을 자동으로 import**

  ```
  $ python manage.py shell_plus
  # Shell Plus Model Imports
  from django.contrib.admin.models import LogEntry from django.contrib.auth.models import Group, Permission, User from django.contrib.contenttypes.models import ContentType from django.contrib.sessions.models import Session from boards.models import Board
  # Shell Plus Django Imports
  from django.core.cache import cache from django.conf import settings from django.contrib.auth import get_user_model from django.db import transaction from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery from django.utils import timezone from django.urls import reverse Python 3.6.7 (default, Dec 9 2018, 17:28:26) [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)] on darwin Type "help", "copyright", "credits" or "license" for more information. (InteractiveConsole)
  > > > 
  ```

- 사용법.
`python manage.py show_urls` : 현재 프로젝트의 모든 url을 확인.
`python manage.py shell_plus` : 현재 사용하고 있는 모든 모듈을 자동으로 import한 상태로 shell 사용.



## 11. Django_bootstrap4
## 11.1. Django_bootstrap4 설치
`pip install django_bootstrap4`









## 12. django allauth

<https://django-allauth.readthedocs.io/en/latest/index.html>

























## 12. Error

`NoReverseMatch` : 현재 접속한 페이지에 잘못되거나 존재하지 않는 url이 설정되어 있기 때문.










URI : URL 과 URN의 개념을 포함하는 큰 개념.

URL은 파일만 식별

URI, URL 은 자원의 위치를 나타내거나, 서버를 나타내면 

쿼리스트링을 포함하는 경우 : URL은 맞지만. search 까지가 URL 뒤 쿼리스트링이라는 식별자가 필요하므로 URI

URN : 서버 내부적으로 사용.



scheme/Protocol://Host :Port/Path

http://localhost:8000/boards







REST API ? 



---

`pip install ipython` : 

from IPython import embed

embed() 함수에서 정지하고 각각의 값을 알 수 있게 해줌.



---


# 참고자료 190610

> - SQLite 설치 : <https://www.sqlite.org/download.html>
> - Dango DB 설정 : <https://docs.djangoproject.com/ko/2.2/ref/settings/#std:setting-DATABASES>
> - Django_extention Doc : <https://django-extensions.readthedocs.io/>

```

```