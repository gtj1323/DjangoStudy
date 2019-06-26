Board 게시글

Comment 댓글

1개의 Board에 여러개의 Comment가 달릴 수 있음.(두개의 관계를 어떻게 연결 지을 것인가. 외래키 사용(foreign key)를 사용하여 연결. 외래키는 부모의 유일한 값을 참조(일반적으로 PK))

Board:Comment = 1:N 관계

1개의 Comment에는 1개의 board에 달릴 수 있음.



Movie.objects.annotate(score_avg=Avg(score_avg=Avg('score__score')).order_by('?'))

매번 새로 고침할 때마다 순서가 바뀜.



Movie.objects.annotate(score_avg=Avg(score_avg=Avg('score__score')).get(pk=1))

movie_pk가 1이면서 score 모델의 score 컬럼의 평균을 score_avg라는 새로운 컬럼으로 추가적으로 붙여서 결과를 받겠다. 실제 DB에는 존재하지 않음. 필요한 순간에만 col을 만들어서 사용하는 방법.

'모델명__컬럼명' 으로 사용.





----

1. 가상환경 만들기
`python -m venv '가상환경 이름' `
ex) `python -m venv form-venv`

2. 가상환경 활성화 
`source '가상환경이름'/Scripts/activate`
ex) `source form-venv/Scripts/activate`

3. 





장고 부트스트랩

<https://django-bootstrap4.readthedocs.io/en/latest/>







장고 작성법 1 : FBV(Function Based View) CBV보다는 코드가 길다. 개발자가 원하는 대로 수정이 용이.

장고 작성법 2 : CBV(Class Based View) 매우 짧고 장고가 해주는게 많음, 자유도가 떨어짐. 기존의 템플릿 사용.









M:N related_name='patients'옵션 전.

```python
$ python manage.py shell_plus
# Shell Plus Model Imports
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from manytomany.models import Doctor, Patient, Reservation
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
from django.utils import timezone
from django.urls import reverse
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: patient = Patient.objects.get(pk=1)

In [2]: patient.reservation_set.all()
Out[2]: <QuerySet [<Reservation: 1번 의사의 1번 환자 예약>, <Reservation: 2번 의사의 1번 환자 예약>]>

In [3]: patient.doctors.all()
Out[3]: <QuerySet [<Doctor: 1번 의사 Kim>, <Doctor: 2번 의사 Kang>]>

In [4]: doctor2= Doctor.objects.get(pk=2)

In [5]: doctor2
Out[5]: <Doctor: 2번 의사 Kang>

In [6]: doctor2.patients.all()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-a32766861a8f> in <module>
----> 1 doctor2.patients.all()

AttributeError: 'Doctor' object has no attribute 'patients'

In [7]: doctor2.patient_set.all()
Out[7]: <QuerySet [<Patient: 1번 환자 John>]>

In [8]: 
```





M:N related_name='patients'옵션 후.

```python
$ python manage.py shell_plus
# Shell Plus Model Imports
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from manytomany.models import Doctor, Patient, Reservation
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
from django.utils import timezone
from django.urls import reverse
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: doctor = Doctor.objects.get(pk=1)

In [2]: doctor
Out[2]: <Doctor: 1번 의사 Kim>

In [3]: doctor.patients.all()
Out[3]: <QuerySet [<Patient: 1번 환자 John>, <Patient: 2번 환자 Tom>]>

In [4]: 
```

위 관계를 역참조라 함.





throuth를 지우면 중계 모델이 삭제됨.

```python
$ python manage.py shell_plus
# Shell Plus Model Imports
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from manytomany.models import Doctor, Patient
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
from django.utils import timezone
from django.urls import reverse
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: doctor = Doctor.objects.create(name="Kim")

In [2]: patient = Patient.objects.create(name="John")

In [3]: doctor.patients.add(patient)

In [4]: patient.doctors.add(doctor)

In [5]: doctor.patients.remove(patient)

In [6]: doctor.patients.all()
Out[6]: <QuerySet []>

In [7]: patient.doctors.all()
Out[7]: <QuerySet []>

In [8]: 
```





좋아요 만들기 (유저는 board에 lilke할 수 있음. board는 여러 user로 부터 like 받을 수 있음.)

User:Board  (좋아요)

User:User  (팔로우)

해당 게시글을 좋아요한 모든 유저를 불러야함.











```python
from django.db import models
from django.conf import settings # 유저모델을 가져오는 것.

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 보드에 들어가는 유저 정보.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # settings.AUTH_USER_MODEL : 유저 모델, 스트링. 실행특성상 최초에는 이 model을 사용함.
    # get_user_model() 함수 (installed app을 실행 후 알 수 있음.)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_boards')
    # 1:N관계에서 user.board_set.all()=자신이 작성한 글
    # 사용 중이므로 related_named을 꼭 써야함. user.like_board.all() (자신이 좋아요한 모든 글)
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',) # pk를 기준으로 역순으로 정렬함.

    def __str__(self):
        return self.content
```

board.user = 게시글을 작성한 유저

board.like_users = 게시글을 좋아요한 유저

user.board_set : 유저가 작성한 게시글들

user.like_boards : 유저가 좋아요한 게시글 들(related_name으로 설정)





- 템플릿 분할

특정 구역을 모듈화 하여 사용함.

---

java script(ecmascipt)

- ESCMAscript5 변화, 5로 넘어가면서 큰 변화가 있었음.
var(전역 변수)
let(지역 변수(함수기반))
const(유일 값 상수)

자바스크립트 공부 : <https://eloquentjavascript.net/>

코뿔소 책 : 

---

VS Code 가상환경 활성화 방법 2.

1. `ctrl`+`shift`+`P`

2. python : Select Interpreter



---

0619

USER django 기본적으로 제공해준 모델이 있음.

직접 만들어서 쓸 수 있음.

`AbstractUser` : 장고에서 제공해주는 확장 User모델

`models.Model`-> `AbstractBaseUser`->`AbstractUser`->`User`

django/contrib/auth/base_user.py에 AbstractBaseUser

django/contrib/auth/models.py에 AbstractUser



---

0620

좋아요 버튼 선택

각각 버튼에 이벤트 생성

해당 버튼의 id찾고 (data-id)

좋아요 요청을 보냈을 때(axios)

view에서 보내준 boolean 값에 따라

특정 클래스에 따라 선택

---

배포



gitignore추가

*.bak

*.sqlite3

*.env



pip install python-decouple





폴더에 .env

SECRET_KEY='pmv#bdjht^5!2xe=2gltj!r40kgojpg-za4blhvnnum^!m17rs'(장고settings.py에서 복사.)











django-heroku 설치(<https://github.com/heroku/django-heroku>)

pip install django-heroku

<https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile>



heroku-cli 설치

