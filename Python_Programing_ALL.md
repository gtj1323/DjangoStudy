[TOC]

# 1. 190527 파일 읽고 수정 명령.



## 1-1. 파이썬으로 파일 다루기

- dummy_ex\dummy.py : 성, 이름을 랜덤으로 석어 500개의 .txt파일을 생성

```python
import os
import random

family = ['김','이','박','최','황','오','강','한','제갈','하','정','송','현','손','조']
given = ['길동','준','민준','소미','수진','지은','동해','민태','준호','세정','지훈','성우','성원']

for i in range(500):
    cmd = f"touch {str(i+1)}_{random.choice(family)}{random.choice(given)}.txt"
    print(cmd)
    os.system(cmd)

'''
os.chdir('폴더주소'):작업하고 있는 위치 변경
os.listdir('폴더주소'):저장된 디렉토리 전체 파일 목록을 얻기
os.rename('현재파일 명', '바꿀 파일 명')
'''
```

**f'{변수명} and {변수명}...'**

> [string].format 의 다른 형태로 보면 됨. python 3.7부터 적용되는 함수.



- dummy_ex\handle.py : .txt 파일명 앞에 '지원자_'를 추가함.

```python
import os

os.chdir(r'C:\Users\student\PycharmProjects\menufactual_file\dummy_ex')
# 맥북 사용 시 os.chdir(r'C:/Users/student/PycharmProjects/menufactual_file/dummy_ex')
filenames = os.listdir('.')

for filename in filenames:
    # 확장자명을 소문자로 바꾸어 리턴.
    txt = os.path.splitext(filename)[-1].lower()
    if txt == '.txt':
       os.rename(filename, f'지원자_{filename}')

'''
os.path.splitext(filename) 확장자와 파일명을 구분
('c:/tempython/data.txt') => ('c:/tempython/data, .txt')
'''
```

**os.listdir('.')**

> 해당 디렉토리의 파일 목록을 리턴함.

**os.chdir(r'dir_path')**

> 해당 디렉토리 내의 파일 목록을 읽어 List로 리턴.

**os.path.splitext(filename)**

> 확장자와 파일명을 구분하여 List로 리턴
>
> > ex)  ('c:/tempython/data.txt') => ('c:/tempython/data, .txt')



- dummy_ex\handle2.py : .txt 파일명 앞의 '지원자' -> '합격자'로 변경

```python
import os

os.chdir(r'C:\Users\student\PycharmProjects\menufactual_file\dummy_ex')
# 맥북 사용 시 os.chdir(r'C:/Users/student/PycharmProjects/menufactual_file/dummy_ex')
filenames = os.listdir('.')
for filename in filenames:
    # 파일명과 확장자명을 구분하고, 확장자명을 소문자로 바꾸어 리턴.
    txt = os.path.splitext(filename)[-1].lower()
    if txt == '.txt':
       os.rename(filename, filename.replace('지원자', '합격자'))

'''
os.path.splitext(filename) 확장자와 파일명을 구분
('c:/tempython/data.txt') => ('c:/tempython/data, .txt')
지원자->합격자로 변경하기
'''
```

**os.rename('변환 전 파일 명', '변환 후 파일 명')**

> 파일명을 바꾸어 줌.

**[txt].replace('변환 전', '변환 후')**

> 텍스트의 내용을 변환 전 에서 변환 후로 수정하여 리턴.



## 1-2. 파이썬으로 txt파일 다루기

- text_ex\write_text.py : txt파일 몇줄 반복해서 작성.

```python
f = open('mulcam.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')
f.close() #항상 닫아 줘야함.
##############################################위와 아래가 완전히 동일한 코드
with open('mulcam.txt', 'a') as f:  # 'a'를 하면 뒤에 따라 씀.
    for i in range(10):
        f.write(f'This is line {i + 1}.\n')
```

**open('파일명.확장자', '매개변수 char')**

> 파일을 읽거나 씀. 매개변수 char가 'w', 'r'에 따라 읽기, 쓰기가 가능.
>
> 원래는 반드시 닫야 줘야하지만 with를 씀으로써 극복 가능.

**with**

> 컨텍스트 매니저를 불러서 의도치 않은 상황에서도 자동으로 제한하고 해제하는 역할을 해줌.
>
> close()를 따로 사용할 필요가 없어짐.



- text_ex\read_text.py : txt파일을 읽어서 출력함.

```python
# readlines():파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 함수
#
with open('mulcam.txt', 'r') as f:  #'r'은 읽어 들임.
    lines = f.readlines() # 모든 텍스트를 읽고, 라인마다 하나의 요소로 읽어서 리스트로 만들어 줌.
    for line in lines:
        print(line)

# read() : 파일 내용 전체를 문자열로 return
with open('mulcam.txt', 'r') as f:
    all_text = f.read()
    print(all_text)
```



- text_ex\reverse.py : txt파일을 읽어서 라인별로 뒤집어서 정렬

```python
# 1. line 불러오기
with open('number.txt', 'r') as f:
    lines = f.readlines()

# 2. 뒤집기
lines.reverse()

# 3. 다시 작성하기
with open('number.txt', 'w') as f:
    for line in lines:
        f.write(line)
```

**[list].reverse()**

> 작성된 리스트의 순서를 뒤집음.



## 1-3. 파이썬으로 CSV파일 다루기

- csv_ex\write_csv.py : lunch에 있는 내용을 CSV파일로 만들어서 저장.

```python
lunch = {
    '고갯마루':'02-123-4567',
    '세븐브릭스':'02-234-5678',
    '아랑졸돈까스':'02-345-6789'
}
# 1. string formatting을 사용하는 방법, encodeing을 하지 않으면 한글이 깨짐.
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(f'{item[0]}, {item[1]}\n')

# 2. join을 사용하는 방법
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(','.join(item)+'\n')

# 3. csv.writer
import csv
with open('lunch3.csv', 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)
```

**[dic].items()**

> 키와 아이템을 튜플 형식으로 리턴

**','.join(item)**

> 아이템에 있는 변수를 ','를 사이에 넣어서 리턴함.

**f.write('content')**

> 파일에 content 를 작성함.

**csv.writer(file)**

> 작성가능하도록 만들어 줌.

**[csv.writer(file)].writerow(item)**

> item에 있는 내용을 ','(csv의 구분자)로 나누어 작성함. 끝에는 \n(계행 문자)를 넣어 줌.

**open('파일 명.확장자', '매개변수 [char]', encoding='utf-8') :**

> 원래라면 따로 close를 해주어야 하지만, with를 사용함으로써 자동으로 close됨.
>
> 파일을 열어서 사용하도록 해줌.
>
> 매개변수[char] 'r' - 읽기, 'w' - 쓰기



- csv_ex\read_csv.py : csv파일을 읽고 각각의 파일에 들어 있는 내용을 구분함.

```python
import csv
# 1. split, strip (rstrip, lstrip)
with open('lunch.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(','))

# 2. csv.reader
with open('lunch.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)
```

**f.readlines()**

> 파일을 한 줄씩 읽어 리스트로 변환하여 리턴함.

**[text]].strip() [text]].rstrip() [text]].lstrip() **

> 내용에 들어있는 계행문자(\n)를 제거함. r을 하면 오른쪽, l을 하면 왼쪽을 제거함.

**[text].split(',')**

> 내용에 들어 있는 문자를 ','를 이용하여 구분 리스트로 반환함.

**csv.reader(f)**

> csv파일을 읽어 사용하는 상태가 됨.



## 1-4. 스크래핑 기초

- scraping_ex\remind.py : 'https://finance.naver.com/sise/' 페이지에서 코스피지수를 출력함.

```python
import requests
# from pprint import pprint # Json, list를 보기 좋게 출력함.
from bs4 import BeautifulSoup

# 1. 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장
req = requests.get('https://finance.naver.com/sise/').text
# print(req)
# print(req.text)
# print(req.status_code)

# 2. 정보를 조작하기 전 편하게 바꾸고,
soup = BeautifulSoup(req, 'html.parser')
# print(soup)

# 3. 바꾼 정보 중 원하는 것만 뽑아서 ,출력한다.
kospi = soup.select_one('#KOSPI_now')
print(kospi.text)
```

**[text, html].text**

> 텍스트만 리턴, html태크 등을 제거하고 리턴함.

**requests.get('페이지 주소')**

> 크롤링할 페이지의 html문서를받아옴.

**BeautifulSoup([requests,html], 'html.parser')**

> html을 다룰 수 있도록 하여 'bs4.BeautifulSoup 객체를 리턴
>
> 'html.parser'는 정해져있음.

**soup.select_one('html 태그')**

> html 문서의 태그를 따라가고, 남아있는 태그와 텍스트를 리턴함.



- scraping_ex\naver.py : 네이버 실시간 검색어를 출력함.

```python
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.naver.com/').text
print(req)
soup = BeautifulSoup(req, 'html.parser')
# print(soup)
top10 = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')

for item in top10:
    print(item.text)
```

**soup.select('html 태그')**

> 해당 태그가 가능한 것들을 list로 리턴함.



- scraping_ex\bithomb.py : 빗썸에서 목록을 가져와 출력함.

```python
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bithumb.com/').text
#print(req)
soup = BeautifulSoup(req, 'html.parser')
# print(soup)
tags = soup.select('#tableAsset > tbody > tr > td:nth-child(1) > p > a > strong')

for tag in tags:
    print(tag.text)
```



- scraping_ex\bithomb2-1.py : 가격정보와 이름을 NEW표시를 지워서 txt파일로 저장함.

```python
# 코인명 /각겨 정보로 txt 저장하기
import requests
from bs4 import BeautifulSoup

# 1. names와 prices 리스트를 받아 옴.
req = requests.get('https://www.bithumb.com/').text
soup = BeautifulSoup(req, 'html.parser')

names = soup.select('#tableAsset > tbody > tr > td:nth-child(1) > p > a > strong')
prices = soup.select('#tableAsset > tbody > tr > td:nth-child(2) > strong')

# 2. zip으로 묶어서 NEW를 분리하여 제거 한 후, 텍스트파일bitbit.txt에 씀.
with open('bitbit.txt', 'w', encoding='utf-8') as f :
    for name, price in zip(names, prices):
        n = name.text.split()
        # if ' NEW' in name.text:
        #     name.text.replace(' NEW', '')
        #     print(name.text, 'new!')
        f.write(f'{n[0]} / {price.text}\n')
```



- scraping_ex\bithomb2-2.py : 가격정보와 이름을 NEW표시를 지워서 txt파일로 저장함.

```python
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bithumb.com/').text

soup = BeautifulSoup(req, 'html.parser')
coin_name_tags = soup.select('#tableAsset > tbody > tr > td:nth-child(1) > p > a > strong')
coin_price_tags = soup.select('#tableAsset > tbody > tr > td:nth-child(2) > strong')

print(coin_price_tags)

for i, item in enumerate(coin_name_tags):
    line = coin_name_tags[i].text.split()[0] + "/" + coin_price_tags[i].text + "\n"
    print(line)

    with open(f'coin.txt', 'a', encoding='utf-8') as f:
        f.write(f'{line}')
```



- scraping_ex\bithomb2-3.py : 가격정보와 이름을 NEW표시를 지워서 txt파일로 저장함.

```python
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bithumb.com/').text

soup = BeautifulSoup(req, 'html.parser')
tags = soup.select('.coin_list tr')

with open('bitbit.txt', 'w', encoding='utf-8') as f:
    for tag in tags:
        name = tag.select_one('td:nth-of-type(1) a strong').text.replace(' NEW', '').strip()
        price = tag.select_one('td:nth-of-type(2) strong').text
        f.write(f'{name} / {price}\n')
```



- scraping_ex\melon.py : 멜론의 실시간 차트 1~50까지의 순위/ 타이틀/ 아트스트를 파일로 작성.

```python
import  requests
from bs4 import BeautifulSoup

# 일반적인 크롤링이 불가능 한 경우 헤더를 함께 보내야 응답하는 경우가 있음. 반드시 헤더는 dirc 형태로 보내야 함.
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
req = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text

soup = BeautifulSoup(req, 'html.parser')
tags = soup.select('#lst50')

with open('MelonCart.txt', 'w', encoding='utf-8') as f:
    for tag in tags:
        rank = tag.select_one('td:nth-child(2) .rank').text
        artist = tag.select_one('td:nth-child(6) .ellipsis.rank01 a').text
        title = tag.select_one('td:nth-child(6) .ellipsis.rank02 a').text
        print(f'{rank}위 / {artist} / {title}')
        f.write(f'{rank}위 / {artist} / {title}\n')
```

> 멜론의 경우 header를 함께 보내야만 서버에서 응답이 오기 때문에 같이 보내 주기 위해서 dic형태로 header를 작성하여 함께 보내 주어야함.



## 1-5. 파이썬으로 메일 보내기.

- email_ex\naver_text_email.py

```python
import smtplib
from email.message import EmailMessage
from getpass import getpass

password = getpass('Password : ')
msg = EmailMessage()
msg['Subject'] = '제목을 지어 줍니다. 지금은 Untitled'
msg['From'] = 'gtj1323@naver.com'

# 한명에게 보낼 경우
# msg['To'] = 'oops0429@naver.com'
# 여러명에게 보낼 경우
email_list=['gtj1323@naver.com', 'oops0429@naver.com', 'jbt95955142@gmil.com']
msg['To'] = ','.join(list)

msg.set_content('햄 메일한번 보내 봅니다.')

s = smtplib.SMTP_SSL('smtp.naver.com', '995') # '메일', '포트' - 메일 설정에서 가져와야함.
s.login('gtj1323', password)
s.send_message(msg)

print('이메일 전송 완료 !!')

```

**getpass()**

> 패스워드를 직접 입력받아서 쓰기 위해 사용.



- email_ex\naver_html_email.py

```python
import smtplib
#from email.message import EmailMessage
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart

password = getpass('Password : ')

msg = MIMEMultipart()
msg['Subject'] = '제목을 지어 줍니다. 지금은 Untitled'
msg['From'] = 'gtj1323@naver.com'

# 한명에게 보낼 경우
# msg['To'] = 'oops0429@naver.com'
# 여러명에게 보낼 경우
email_list=['gtj1323@naver.com', 'oops0429@naver.com', 'jbt95955142@gmil.com']
msg['To'] = ','.join(list)

html = """
<html>
    <body>
        <img src="http://sampleimg.com/asdasd.png">
        <p>HI,</p>
        <a href = "https://www.google.com">GO TO GOGGLE</a>
    </body>
</html>
"""
part = MIMEText(html, 'html')
msg.attach(part)

s = smtplib.SMTP_SSL('smtp.naver.com', '995') # '메일', '포트'
s.login('gtj1323', password)
s.send_message(msg)

print('이메일 전송 완료 !!')

```



- html 문서 간단한 표만들기

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Html_table_ex</title>
</head>

<body>
	<td>
		<h1>
			<font face='궁서체'>2019 타임테이블</font>
		</h1>
		<br />
		<table border="1">
			<tr>
				<td colspan="2">
					<h2>
						<div id='center' font face='고딕체'>TIME INDOOR</div>
					</h2>
				</td>
				<td colspan="2">
					<h2>
						<div id='center' font face='고딕체'>OUTDOOR</div>
					</h2>
				</td>
			</tr>
			<tr>
				<th></th>
				<th>소극장</th>
				<th>잔디마당</th>
				<th>대공연장</th>
			</tr>
			<tr>
				<td>10:00</td>
				<td rowspan="2">키썸</td>
				<td></td>
				<td>10CM</td>
			</tr>
			<tr>
				<td>13:00</td>
				<td rowspan="2">볼빨간 사춘기</td>
				<td rowspan="2">장범준</td>
			</tr>
			<tr>
				<td>15:00</td>
				<td></td>
			</tr>
			<tr>
				<td>17:00</td>
				<td>헤이즈</td>
				<td></td>
				<td>ColdPlay</td>
			</tr>
		</table>
	</td>
</body>

</html>
```



- from을 이용한 간단한 작성

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Html_table_ex</title>
	<style>
			body {
				height: 1000px;
			}
		</style>
</head>

<body>
	<!-- emmet 치트 시트라고 치면 많이 나옴. -->
	<!-- .container>.row>ul>li*10>a[href="#"]>{items$} -->
	<!-- 결과 -->
	<!-- <div class="container">
		<div class="row">
			<ul>
				<li><a href="#">items1</a></li>
				<li><a href="#">items2</a></li>
				<li><a href="#">items3</a></li>
				<li><a href="#">items4</a></li>
				<li><a href="#">items5</a></li>
				<li><a href="#">items6</a></li>
				<li><a href="#">items7</a></li>
				<li><a href="#">items8</a></li>
				<li><a href="#">items9</a></li>
				<li><a href="#">items10</a></li>
			</ul>
		</div>
	</div> -->
	<!-- /결과 -->
	<h1 face="견명조">FORM</h1>
		<p>주문서를 작성하여 주십시오.</p>

		<form>
			이름 : <input type="text" placeholder="이름을 입력해 주세요."><br>
			<h2>1. 샌드위치 선택</h2>
			<input type="radio" name="sendwhitch" value="egg" checked>에그 마요<br>
			<input type="radio" name="sendwhitch" value="itelic">이탈리안 비엠티<br>
			<input type="radio" name="sendwhitch" value="terkyb">터키 베이컨 아보카도<br>

			<h2>2. 사이즈 선택</h2>
			<input type="number" name="size" value="15" step="15" min="15" max="30">

			<h2>3. 빵</h2>
			<select>
				<option value="1">허니오트</option>
				<option value="2" disabled>플랫브레드</option>
				<option value="3" selected>하티 이탈리안</option>
			</select>

			<h2>4. 야채 소스</h2>
			<input type="checkbox" name="option" value="tomato">토마토<br>
			<input type="checkbox" name="option" value="오이">오이<br>
			<input type="checkbox" name="option" value="할라피뇨">할라피뇨<br>
			<input type="checkbox" name="option" value="핫 칠리">핫 칠리<br>
			<input type="checkbox" name="option" value="바베큐">바베큐<br>

			<input type="submit" value="주문하기">
		</form>

</body>

</html>
```







------

# ※ 참고자료 190527

> - 참고자료 - 2019년 웹개발자 로드맵 : <https://github.com/kamranahmedse/developer-roadmap>
> - 참고자료 - 2019년 웹개발자 로드맵 : <https://github.com/devJang/developer-roadmap>
> - 참고자료 - 자바스크립트 공부 : <https://eloquentjavascript.net/>
> - 재미있는 거 : 세계적인 크롤링 사이트 : <http://internetlivestats.com>
> - 웹 표준 : <https://www.w3.org/>
> - ChromeExtension - Wappalyzer : 웹개발에 사용된 언어를 알려줌.
> - ChromeExtension  - ublock origin : 광고 차단.
> - ChromeExtension  - Web Developer
> - [emmet cheat sheet](https://docs.emmet.io/cheat-sheet/) -  html 작성에 유용한 툴.















[TOC]

# 2. 190528 CSS 다루기.



## 2-0. VS Code로 html 다루기 tip

- alt+ctrl : html 다중 선택.
- alt+shift : html 라인 복사.
- alt+shift : 라인 이동.
- span태그와 div태그는 모두 의미는 없지만 마크업을 해야 CSS를 적용시킬 수 있기 때문에 활용.
- VC Code 설정 : ctl + shift + p / setting.json 파일을 아래와 같이 설정.

```json
{
    "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
    "[html]": {
        "editor.fontFamily":"Hack",
        "editor.tabSize": 2,
        "editor.defaultFormatter": "HookyQR.beautify"
    },
}
```



## 2-1. CSS 사용하기

- 00_css.html

```html
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="00.css">
  <title>Documents</title>
</head>

<body>
  <h1 style="color : aqua">inline</h1>
  <h2>내부 참조</h2>
  <h3>외부 참조</h3>
</body>

</html>
```

- 00.css

```css
h3{
    color : blue !important /*<!-- 거의 쓰지 않음. 최 우선순위로 사용-->*/
}
```

**> 스타일 적용 우선 순위**

> !important > inline > embedding > file link > browser default
>   단, 동일한 head에 외부스타일을 나중에 정의할 경우, 나중에 정의한 외부스타일이 먼저 적용. 마지막에 덮어씌워지기 때문.



## 2-2. 다양한 글씨 사이즈 적용.

- 01_unit.html

```html
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport">
  <meta http-equiv="X-UA-Compatible">
  <link rel="stylesheet" href="01.css">
  <title>Documents</title>
</head>

<body>
  <p>20px</p>
  <ol>
    <li>1.2rem</li>
  </ol>
  <ul>
    <li>1.2em</li>
  </ul>
  <p class="vh">5vh</p>
  <p class="vw">5vw</p>
  <p class="vmin">10vmin</p>
</body>

</html>
```

- 01.css

```css
html{
    font-size: 20px;
}
ol, ol li{ /*ol과 ol안의 li태그에 적용.*/
    font-size: 1.2rem; /*부모의 1.2배*/
}
ul, ul li{/*ul과 ul태그 안의 li(리스트)에 적용. ul li는 부모의 1.44(1.2 * 1.2)배가 적용 됨.*/
    font-size: 1.2em;
}
.vh{ /*vh, vw, vmin 은 반응형 class 선택은 [.'class 명']*/
    font-size: 5vh;
}
.vw{
    font-size: 5vw;
}
.vmin{
    font-size: 10vmin;
}
```

> px : 픽셀의 크기는 제각각
> % : default 크기의 상대값.
> em : 부모의 상대적 사이즈 1이면 부모의 사이즈를 그대로 따라 감.
> rem : r은 HTML의 루트를 뜻함. (일반적으로 1rem = 16px) 이것의 상대 크기. - 권장.



## 2-3. class, id에 적용하기.

- 02_selector_1.html

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="02.css">
  <title>title</title>
</head>

<body>
  <p>전체 선택자</p>
  <h1>TAG 선택자</h1>
  <h2 class="pink">class 선택자</h2>
  <h3 id="green">id 선택자</h3>
  <h3 id="green" class="pink">id > class</h3>
  <h2 class="pink">class > tag</h2>

  <p><span class="pink">핑크색</span>, <span id="yellow">노란색</span></p>

  <p class="bold blue pink">볼드체, CSS에서 나중에 선언된 blue가 적용됨.</p><!-- 3개의 클래스가 들어감. -->
  <p class="bold pink blue">볼드체, CSS에서 나중에 선언된 blue가 적용됨.</p><!-- 3개의 클래스가 들어감. -->
  <p><strong>볼드체</strong></p><!--strong태그를 사용해야 음성처리시 강조함.-->
  <p><b>볼드체</b></p><!--b태그는 음성처리 시 강조하지 않음.-->
  <img src="" alt="바다 이미지"></img><!--.-->
</body>

</html>
```

- 02.css

```css
*{/* 전체에 적용. */
    color:red;
    background: black;
}
h1{ /* h1 태그에 적용. */
    color:blue;
}
h2{
    color:white
}
.pink{ /* class가 pink인 경우에 적용. */
    color:pink;
}
#green{/* id가 green인 경우에 적용. */
    color:green;
}
#yellow{
    color:yellow;
}
.bold{
    font-weight: bold;
}
.blue{
    color: blue;
}
```



- 03_selector_2.html

```html
<!DOCTYPE html>
<html>

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<link rel="stylesheet" href="03.css">
	<title>title</title>
</head>

<body>
	<!-- 그룹 선택자 -->
	<p>그룹 선택자 적용1</p>
	<h3>그룹 선택자 적용2</h3>
	<p class="black_bg">그룹1</p>
	<p class="white">그룹2</p>

	<div class="red">레드</div>
	<div class="blue">블루</div>
	<div>무지</div>
	<hr>
	<!-- h1 + p -->
	<h1>H1</h1>
	<p>h1의 형제 p</p>

	<!-- 자식 선택자 -->
	<ol>
		<li>ol의 자식 li, 자손 아님.</li>
	</ol>
	<ol id="chocolate">
		<li>화이트 초코</li>
	</ol>
	<ul>
		<div>
			<li>ul의 자손1</li>
			<li>ul의 자손2</li>
			<li>ul의 자손3</li>
		</div>
	</ul>

	<!-- nth -->
	<div id="mulcam">
		<h2>어떤 것이 선택될까요?</h2>
		<p>111</p>
		<p>222</p>
		<p>333</p>
		<p>444</p>
	</div>
</body>

</html>
```

- 03.css

```css
p, h3{
    color:gray;
}
.black_bg, .white{
    color: white;
    background-color: black;
}
div{
    width:100px;
    height:100px;
    border: 1px solid black; /*순서 상관 없음.*/
}
.red{
    background-color: red;
}
.blue{
    background-color: blue;
}
/*인접 선택자에 적용하는 방법*/
.red + .blue + div{/*red클래스 옆의 blue클래스에 붙어 있는 div태그에 적용*/
    background-color: purple;
}
/* 형제 선택자에 적용하는 방법 */
h1 + p{ /* h1 옆에 있는 p 태그 */
    color: crimson;
}
/* 직계자식 선택자에 적용하는 방법 */
ol > li{
    color:darkgreen;
}
ol#chocolate > li{ /*ol의 id가 chocolate인 경우 자식의 색*/
    color:chocolate;
}
/* 후손 선택자에 적용하는 방법 */
ul li{ /* ul의 자손 중 li에 적용*/
    color: lime;
}
/* nth 중 특정 자식의 순서를 선택하여 적용하기 */
#mulcam > p:nth-child(2){/* 모든 자식 중 2번 째 */
    color: red;
}
/* nth 중 특정 태그인 자식의 특정 순서에 적용하기 */
#mulcam > p:nth-of-type(2){/* p태그를 가진 자식 중 2번 째 */
    color: blue;
}
```



## 2-4. 박스모델 다루기

- 04_boxmodel.html

```html
<!DOCTYPE html>

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="04.css">
	<title>title</title>
</head>

<body>
  <div>
    <p>100% !</p>
  </div>
  <div style="width: 50%">
    <p>50.0%!</p>
  </div>

  <div class="square">
    <p>컨텐츠 영역 100 * 100</p>
  </div>

  <div class="square padding-10">
    <p>컨텐츠 영역 100 * 100</p>
  </div>

  <div class="square padding-10 border-box">
      <p>120 * 120 padding 10</p>
  </div>

  <div class="square margin-100">
    <p>100*100 margin 100</p>
  </div>

  <div class="square margin-top-100">
    <p>100*100 margin-top 100</p>
  </div>

  <div class="square margin-left">
    <p>100*100 margin-top 100</p>
  </div>

</body>

</html>
```

- 04.css

```css
.square{
    width: 100px;
    height: 100px;
    background-color: darkgray;
    border: 1px solid black;
    /* border-radius:15px 75px */
}
.padding-10{
    padding: 10px;
}
.border-box{ /*보더박스를 기준으로 바꿈.*/
    box-sizing: border-box;
    /* 기본값은 content-box */
}
.margin-100{
    margin: 100px;
}
.margin-top-100{
    margin-top: 100px;
}
.margin-left{
    margin-left:auto;
    /* 오른쪽 정렬 */
}
.margin-auto{
    margin:auto;
    /* 가운데 정렬 */
}
.test{
    margin: 25px 25px 25px 25px
    /* 4개 t  r  b  l 순서로 지정 */
    /* 3개 t  rl  b */
    /* 2개 tb  rl */
    /* 1개 trbl */
}
```

**박스 모델**

> 배경 > border > content // 사이 간격은 margine, padding 이라는 명칭 사용.



## 2-5. display 다루기 /none, hidden

- 05_display.html

```html
<!DOCTYPE html>

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<link rel="stylesheet" href="05.css">
	<title>title</title>
</head>

<body>
	<h1>block</h1>
	<p>block</p>
	인라인 : <input type="text" name="">
	<span>인라인</span>
	<a href="#">인라인</a>

	<!-- none/hidden -->
	<h2 class="none">display none1</h2>
	<h2>display none2</h2>
	<h2 class="hidden">display hidden1</h2>
	<h2>display hidden1</h2>
	<h2>빠잉</h2>
	
</body>

</html>
```

- 05.css

```css
.none{ /*  */
    display: none;
    /* 구조가 깨질 수 있음. */
}
.hidden{
    visibility:hidden;
}
```

**none**

> 내용도 보이지 않고, 자리도 사라짐. 다른 것들이 해당 자리로 들어오기 때문에 form이 깨짐.

**hidden**

> 내용은 보이지 않지만 자리는 빈 상태로 남아 있음.



## 2-6. position 다루기

- 06_position.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Document</title>
	<link rel="stylesheet" href="06.css">
</head>

<body>
	<div class="square">
		<div class="relative-box square"></div>
	</div>
	<br>
	<div class="square">
		<div class="abs absolute-box square"></div>
	</div>
	<div class="fixed">
		포지션연습
	</div>

</body>

</html>
```

- 06.css

```css
body{
    height: 10000px;
}
.square {
    /* position: relative; */
    position: static;
    width: 100px;
    height: 100px;
    background-color: darkgray;
}
.relative-box{
    /* 자신의 원래 위치를 기준으로 움직임. */
    position: relative;
    background-color:navy;
    top: 10px;
    left: 10px;
}
.absolute-box{
    position: absolute;
    /* 부모 혹은 상위 중 static이 아닌 부모를 기준으로 이동함.
    부모가 static인 경우 더 상위인 부모에서 static이 아닌 부모를 자동으로 찾음. */
    background-color: red;
    top: 30px;
    left: 30px;
}
.fixed{
    position: fixed;
    background-color: chocolate;
    bottom: 10px;
    left: 10px;
}
```



### 2-6-1. 예제 position,박스 옮기기 1

- example2.html

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>BOX</title>
  <link rel="stylesheet" href="style1.css">
</head>

<body>
  <div class="big-box">
    <div class="small-box" id="red"></div>
    <div class="small-box" id="gold"></div>
    <div class="small-box" id="green"></div>
    <div class="small-box" id="blue"></div>
    <div class="small-box" id="pink"></div>
  </div>
</body>

</html>
```

- style1.css

```css
.big-box {
    position: relative;
    margin: 100px auto 500px;
    border: 5px solid black;
    width: 500px;
    height: 500px;
}

.small-box {
    width: 100px;
    height: 100px;
}

#red {
    background-color: red;
    /* 큰 사각형 내부의 우측 하단 모서리에 빨간 사각형 위치시키기 */
    position: absolute;
    /* 부모가 static이 아님. */
    bottom: 0px;
    right: 0px;
}

#gold {
    background-color: gold;
    /* 브라우저의 하단에서 50px, 우측에서 50px 위치에 고정하기 */
    position: fixed;
    bottom: 50px;
    right: 50px;
}

#green {
    background-color: green;
    /* absolute 이용해서 큰 사각형의 가운데 위치시키기 */
    /* z-index: 2; /* 숫자가 클 수록 앞으로 옴. */
    position: absolute;
    top: 200px;
    left: 200px;
}

#blue {
    background-color: blue;
    position: relative;
    top: 100px;
    left: 100px;
    /* relative를 사용해서 큰 사각형 좌측 상단 모서리에서 100px, 100px 띄우기 */
}

#pink {
    background-color: pink;
    position: absolute;
    top: 0px;
    left: 0px;
    /* 큰 사각형 내부의 좌측 상단 모서리로 옮기기*/
}
```

**relative**

> position 적용 전 (static 일 때) 기준으로 움직임. 움직인 후 원래 공간이 유지됨.

**absolute**

> 기본 레이어 관계에서 벗어남(붕 뜸.) 즉 다른 도형들도 새로운 자리로 움직이게됨.
> 움직인 후 원래 공간이 없어짐(집 나감).
> position이 static 이 아닌 부모를 찾아서 그부모를 기준점으로 삼음.



### 2-6-2. 예제 position,박스 옮기기 2

- example2.html

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>BOX</title>
  <link rel="stylesheet" href="style2.css">
</head>

<body>
  <div class="big-box">
    <div class="small-box" id="red"></div>
    <div class="small-box" id="gold"></div>
    <div class="small-box" id="green">
      <div class="small-box" id="purple"></div>
    </div>
    <div class="small-box" id="blue">
      <div class="small-box" id="orange"></div>
    </div>
    <div class="small-box" id="pink"></div>
  </div>
</body>

</html>
```

- style2.css

```css
.big-box {
    position: relative;
    margin: 100px auto 500px;
    border: 5px solid black;
    width: 500px;
    height: 500px;
}
.small-box {
    width: 100px;
    height: 100px;
}
#red {
    background-color: red;
    /* 큰 사각형 내부의 우측 하단 모서리에 빨간 사각형 위치시키기 */
    position: absolute;
    /* 부모가 static이 아님. */
    bottom: 0px;
    right: 0px;
}

#gold {
    background-color: gold;
    /* 브라우저의 하단에서 50px, 우측에서 50px 위치에 고정하기 */
    position: fixed;
    bottom: 50px;
    right: 50px;
}
#green {
    background-color: green;
    /* absolute 이용해서 큰 사각형의 가운데 위치시키기 */
    /* z-index: 2; /* 숫자가 클 수록 앞으로 옴. */
    position: absolute;
    top: 200px;
    left: 200px;
}
#blue {
    background-color: blue;
    position: relative;
    top: 100px;
    left: 100px;
    /* relative를 사용해서 큰 사각형 좌측 상단 모서리에서 100px, 100px 띄우기 */
}
#pink {
    background-color: pink;
    position: absolute;
    top: 0px;
    left: 0px;
    /* 큰 사각형 내부의 좌측 상단 모서리로 옮기기*/
}

#purple {
    background-color: purple;
    position: absolute;
    top: 100px;
    left: 100px;
    /* 초록의 왼쪽 아래, green의 자식 */
}
#orange {
    background-color: orange;
    position: absolute;
    bottom: 100px;
    left: 100px;
    /* 파란색의 오른쪽 위, pink의 자식 */
}
```



# 3. 190528 부트스트랩



## 3-0. 부트스트랩

materialize라는 비슷한 프로그램이 있었으나.(구글에서 만듦.) 거의 사장.

부트스트랩은 twitter에서 만듦. 오픈소스.

프론트에서 깔끔하게 만들기 위해서 사용함.

CDN : 캐싱됨. 부트스트랩서버를 이용하기 때문에 운영하는 서버사용이 줄어듦. 때문에 많이 사용함.



## 3-1. 부트스트랩 기초

- 00_bootstrap.html

```html
<!DOCTYPE html>
<html lang="en">

</html>

<head>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
		integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>title</title>

	<style>
		div{
			width: 100px;
			height: 100px;
			/* background-color: royalblue; */
			/* border : 1px white solid */
		}
		/* mt-1 -> 0.5
		mt-2 -> 1
		mt-3 -> 1.5
		mt-4 -> 3 */
	</style>
</head>

<body>
	<div class="mt-3 bg-primary border border-warning">기본 mt-3</div>
	<div class="p-2 mt-2 bg-danger text-white border border-bottom text-right">p-2 mt-2</div>
	<div class="mt-2 mx-auto bg-warning rounded-top text-center">가운데</div>
	<div class="mt-2 mr-auto bg-info rounded-pill">mt-2 왼쪽 정렬</div>
	<div class="mt-2 ml-auto bg-dark text-white rounded-circle">mt-2  오른쪽 정렬</div>
	<span class="d-block">기본적으로 인라인 태그</span>
	<div class="m-2 bg-danger d-sm-none d-md-block">시작해봅니다.</div>
		<!-- ↑ sm이면 none(사라짐), md이면 block -->
	<div class="m-2 bg-warning d-md-none d-xl-block"></div>
		<!-- ↑ md이면 none(사라짐), xl이면 block -->
	<div class="fited-top bg-dark"></div>
	<div class="fited-bottom bg-warning"></div>
	


	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
		integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
	</script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
		integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
	</script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
		integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
	</script>

</body>

</html>
```



## 3-2. 부트스트랩 grid 다루기

- 01_greid.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
		integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>title</title>
	<style>
		.square {
			background-color: pink;
			border: 1px solid gray;
		}
	</style>
</head>

<body>
	<div class="container">
		<div class="alert alert-primary" role="alert">
			A simple primary alert—check it out!
		</div>
		<!-- 양쪽에 약간 여백이 생김. container가 여백이 있는 공간이기 때문 -->
	</div>

	<div class="container-fluid">
		<div class="alert alert-primary" role="alert">
			A simple primary alert—check it out!------------
		</div>
		<!-- 양쪽에 약간 여백이 생김. container는 더 넓음. -->
	</div>

	<!-- grid 시스템 사용하기 주로 container 안에서 사용. -->
	<br>
	<div class="container">
		<div class="row">
			<div class="square col-1">1</div>
			<div class="square col-1">2</div>
			<div class="square col-1">3</div>
			<div class="square col-1">4</div>
			<div class="square col-1">5</div>
			<div class="square col-1">6</div>
			<div class="square col-1">7</div>
			<div class="square col-1">8</div>
			<div class="square col-1">9</div>
			<div class="square col-1">10</div>
			<div class="square col-1">11</div>
			<div class="square col-1">12</div>
		</div>

		<br>

		<div class="row">
			<div class="square col-3">1 / 3</div>
			<div class="square col-4">2 / 3</div>
			<div class="square col-5">3 / 3</div>
		</div>

		<br>

		<div class="row">
			<div class="square col-4">1 / 3</div>
			<div class="square col-8">2 / 3</div>
		</div>

		<br>

		<div class="row">
			<div class="square col-1">1 / 3</div>
			<div class="square col-2 offset-5">1 / 3</div><!-- 5칸 띄워서 2칸짜리 -->
		</div>

		<br>
		<!-- 1줄 col 1개, sm 2개,  md 3개, lg 4개, xl 6개 -->
		<div class="row">
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">1</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">2</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">3</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">4</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">5</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">6</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">7</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">8</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">9</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">10</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">11</div>
			<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">12</div>
		</div>
	</div>

	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
		integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
	</script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
		integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
	</script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
		integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
	</script>
</body>

</html>
```



## 3-3. 다양한 bootstrap 요소 사용하기.

- 02_components.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
		integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>title</title>
</head>

<body>
	<div class="container">

		<nav class="navbar navbar-expand-lg navbar-light bg-light">
			<a class="navbar-brand" href="#">Navbar</a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
				aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>

			<div class="collapse navbar-collapse" id="navbarSupportedContent">
				<ul class="navbar-nav mr-auto">
					<li class="nav-item active">
						<a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="#">Link</a>
					</li>
					<li class="nav-item dropdown">
						<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown"
							aria-haspopup="true" aria-expanded="false">
							Dropdown
						</a>
						<div class="dropdown-menu" aria-labelledby="navbarDropdown">
							<a class="dropdown-item" href="#">Action</a>
							<a class="dropdown-item" href="#">Another action</a>
							<div class="dropdown-divider"></div>
							<a class="dropdown-item" href="#">Something else here</a>
						</div>
					</li>
					<li class="nav-item">
						<a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
					</li>
				</ul>
				<form class="form-inline my-2 my-lg-0">
					<input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
					<button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
				</form>
			</div>
		</nav>





		<button type="button" class="btn btn-primary"> 내용 </button>

		<div class="card" style="width: 18rem;">
			<img src="..." class="card-img-top" alt="...">
			<div class="card-body">
				<h5 class="card-title">Card title</h5>
				<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's
					content.</p>
				<a href="#" class="btn btn-primary">Go somewhere</a>
			</div>
		</div>

		<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
			<div class="carousel-inner">
				<div class="carousel-item active">
					<img src="..." class="d-block w-100" alt="...">
				</div>
				<div class="carousel-item">
					<img src="..." class="d-block w-100" alt="...">
				</div>
				<div class="carousel-item">
					<img src="..." class="d-block w-100" alt="...">
				</div>
			</div>
		</div>

		<p>
			<a class="btn btn-primary" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false"
				aria-controls="collapseExample">
				Link with href
			</a>
			<button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#collapseExample"
				aria-expanded="false" aria-controls="collapseExample">
				Button with data-target
			</button>
		</p>
		<div class="collapse" id="collapseExample">
			<div class="card card-body">
				Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. Nihil anim
				keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident.
			</div>
		</div>

		<div class="dropdown">
			<button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown"
				aria-haspopup="true" aria-expanded="false">
				Dropdown button
			</button>
			<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
				<a class="dropdown-item" href="#">Action</a>
				<a class="dropdown-item" href="#">Another action</a>
				<a class="dropdown-item" href="#">Something else here</a>
			</div>
		</div>

		<form>
			<div class="form-group">
				<label for="exampleInputEmail1">Email address</label>
				<input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
					placeholder="Enter email">
				<small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
			</div>
			<div class="form-group">
				<label for="exampleInputPassword1">Password</label>
				<input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
			</div>
			<div class="form-group form-check">
				<input type="checkbox" class="form-check-input" id="exampleCheck1">
				<label class="form-check-label" for="exampleCheck1">Check me out</label>
			</div>
			<button type="submit" class="btn btn-primary">Submit</button>
		</form>

		<div class="jumbotron jumbotron-fluid">
			<div class="container">
				<h1 class="display-4">Fluid jumbotron</h1>
				<p class="lead">This is a modified jumbotron that occupies the entire horizontal space of its parent.</p>
			</div>
		</div>

		<!-- Button trigger modal -->
		<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
			Launch demo modal
		</button>

		<!-- Modal -->
		<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
			aria-hidden="true">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
						<button type="button" class="close" data-dismiss="modal" aria-label="Close">
							<span aria-hidden="true">&times;</span>
						</button>
					</div>
					<div class="modal-body">
						...
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
						<button type="button" class="btn btn-primary">Save changes</button>
					</div>
				</div>
			</div>
		</div>

		<div class="progress">
			<div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
		</div>
		<div class="progress">
			<div class="progress-bar" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0"
				aria-valuemax="100"></div>
		</div>
		<div class="progress">
			<div class="progress-bar" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0"
				aria-valuemax="100"></div>
		</div>
		<div class="progress">
			<div class="progress-bar" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0"
				aria-valuemax="100"></div>
		</div>
		<div class="progress">
			<div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0"
				aria-valuemax="100"></div>
		</div>

		<div class="spinner-border" role="status">
			<span class="sr-only">Loading...</span>
		</div>

		<button class="btn btn-primary" type="button" disabled>
			<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
			<span class="sr-only">Loading...</span>
		</button>
		<button class="btn btn-primary" type="button" disabled>
			<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
			Loading...
		</button>
		<br>
		<br>

		<table class="table">
			<thead>
				<tr>
					<th scope="col">#</th>
					<th scope="col">First</th>
					<th scope="col">Last</th>
					<th scope="col">Handle</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<th scope="row">1</th>
					<td>Mark</td>
					<td>Otto</td>
					<td>@mdo</td>
				</tr>
				<tr>
					<th scope="row">2</th>
					<td>Jacob</td>
					<td>Thornton</td>
					<td>@fat</td>
				</tr>
				<tr>
					<th scope="row">3</th>
					<td>Larry</td>
					<td>the Bird</td>
					<td>@twitter</td>
				</tr>
			</tbody>
		</table>

		<nav aria-label="Page navigation example">
			<ul class="pagination">
				<li class="page-item"><a class="page-link" href="#">Previous</a></li>
				<li class="page-item"><a class="page-link" href="#">1</a></li>
				<li class="page-item"><a class="page-link" href="#">2</a></li>
				<li class="page-item"><a class="page-link" href="#">3</a></li>
				<li class="page-item"><a class="page-link" href="#">Next</a></li>
			</ul>
		</nav>

	</div>







	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
		integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
	</script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
		integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
	</script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
		integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
	</script>
</body>

</html>
```

**button**

**pagenation**

**Jumbotron**

등등 엄청 많이 있음.



------

# ※ 참고자료 190528

> - 참고 - 브라우저 점수 : [http://www.html5test.com](http://www.html5test.com/)
> - 참고 - 브라우저 사용가능여부 확인 : <https://caniuse.com/>
> - 참고 - 색상 확인 :<https://www.w3.org/TR/css-color-3/>
> - 참고 - 색상 확인 : <https://htmlcolorcodes.com/>
> - 참고 - UI 맞추기 : <https://cantunsee.space/>
> - 참고 - 부트스트랩 : <https://getbootstrap.com/>
> - 참고 - Trello : <https://trello.com/> 그룹별로 자료를 공유하고, 표시하는 기능.
> - 참고 - notion : <https://www.notion.so/> 온라인 앱 통합하여 사용 가능.(유료는 비쌈.)



