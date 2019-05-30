[TOC]

# 1. 190527 파일 읽고 수정 명령.



## 1.1. 파이썬으로 파일 다루기

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



## 1.2. 파이썬으로 txt파일 다루기

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



## 1.3. 파이썬으로 CSV파일 다루기

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



## 1.4. 스크래핑 기초

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



## 1.5. 파이썬으로 메일 보내기.

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




# 2. 190528 CSS 다루기.



## 2.0. VS Code로 html 다루기 tip

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



## 2.1. CSS 사용하기

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
> 단, 동일한 head에 외부스타일을 나중에 정의할 경우, 나중에 정의한 외부스타일이 먼저 적용. 마지막에 덮어씌워지기 때문.



## 2.2. 다양한 글씨 사이즈 적용.

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



## 2.3. class, id에 적용하기.

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



## 2.4. 박스모델 다루기

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



## 2.5. display 다루기 /none, hidden

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



## 2.6. position 다루기

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



### 2.6.1. 예제 position,박스 옮기기 1

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



### 2.6.2. 예제 position,박스 옮기기 2

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



## 3.0. 부트스트랩

materialize라는 비슷한 프로그램이 있었으나.(구글에서 만듦.) 거의 사장.

부트스트랩은 twitter에서 만듦. 오픈소스.

프론트에서 깔끔하게 만들기 위해서 사용함.

CDN : 캐싱됨. 부트스트랩서버를 이용하기 때문에 운영하는 서버사용이 줄어듦. 때문에 많이 사용함.



## 3.1. 부트스트랩 기초

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



## 3.2. 부트스트랩 grid 다루기

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



## 3.3. 다양한 bootstrap 요소 사용하기.

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




# 3. 190529 부트스트랩



- 부트스트랩, 폰트어썸, daneden Animate.css사용을 사용하기 위한  기본 템플릿[.html]

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<!-- 폰트 어썸 --><script defer src="https://use.fontawesome.com/releases/v5.8.2/js/all.js" integrity="sha384-DJ25uNYET2XCl5ZF++U8eNxPWqcKohUUBUpKGlNLMchM7q4Wjg2CUpjHLaL8yYPH" crossorigin="anonymous"></script>
	<!-- daneden Animate.css 가져오기. 사용법은 Github에 나옴. --><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>title</title>
</head>

<body>
	
	
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>

</html>
```

> 이하에서는 바디만 작성(부트스트랩CND제외). 헤더에 추가하는 내용은 있는 경우 추가된 내용만 작성함.



## 3.4. 애니메이션 효과 사용하기.

- 03_animate.html

```html
<head>
	<style>
		/* 웹폰트 사용 설정. 폰트를 직접 다운받아서 사용하는 것이 아니라 직접 사용함. */
		@import url('https://fonts.googleapis.com/css?family=Yeon+Sung&display=swap&subset=korean');
		body {
			font-family: 'Yeon Sung', cursive;
		}
        
        
		.square {
			width: 100px;
			height: 100px;
		}
		p {
			/* 텍스트가 1줄일 경우 위아래 정렬하는 방법. 박스의 사이즈와 라인 높이를 같게 함. */
			line-height: 100px; 
		}
		.square:hover { /* :hover는 마우스를 올렸을 때 옵션. */
			background-color: crimson !important; /* !important를 이용하여 우선순위를 높임. */
			opacity: 0.7; /* 투명도 설정. */
            /* jello라는 효과를 사용함. 2s는 2초동안 천천히 움직임 설정. */
			animation: jello 2s infinite; /* infinite 설정은 무한 반복 설정. */
		}
	</style>
</head>
<!---------------------------------------------------------------------------->
<body>
    <!-- jello 라는 효과, 2초 딜레이 후, slow로 느리게 작동, 무한반복은 infinite -->
	<h1 class="animated jello delay-2s slow">EXAMPLE</h1>
	<br>
	<div class="container">
		<div class="square bg-primary d-inline-block mx-3 text-center">
			<p>1</p>
		</div>
		<div class="square bg-primary d-inline-block mx-3 text-center">
			<p>2</p>
		</div>
	</div>
	폰트 어썸<br>
	<i class="fas fa-money-bill-alt fa-5x faa-vertical animated-hover"></i>
</body>
```

> font awesome은 SVG로 가져옴.



## 3.5. flax사용하여 배치하기.

더 자세한 [FLAX링크 CSS-TRICKS](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) 참초

- 04_flax_00.html

```html
<head>
	<style>
    .container{
        /* display: flex; */
        height: 100vh;
        border: 10px solid royalblue;
        /* display: inline-flex; */
        /* flex-direction: row; */ /* row가 기본값 */
        flex-wrap: wrap;
    }
    .item{
        width: 1000px;
    }
    </style>
</head>
<!---------------------------------------------------------------------------->
<body>
    <div class="container">
        <div class="item item1">1</div>
        <div class="item item2">2</div>
        <div class="item item3">3</div>
        <div class="item item4">4</div>
        <div class="item item5">5</div>
        <div class="item item6">6</div>
        <div class="item item7">7</div>
        <div class="item item8">8</div>
        <div class="item item9">9</div>
        <div class="item item10">10</div>
        <!-- <div class="item item11">11</div>
        <div class="item item12">12</div> -->
    </div>
</body>
```

**display : 택 1 ( flex | inline-flex );**

> 해당  <u>**오브젝트가 여러개인 경우 정렬**</u>에 사용.
>
> flex -  한 줄에 1개만 가능.
>
> inline-flex - 한 줄에 여러 그릴 수 있음.

**flex-direction: 택 1 ( row | row-reverse | column | column-reverse );**

> 해당 오브젝트 <u>**내부에 있는 오브젝트의 정렬**</u>에 사용.
>
> row - 왼쪽에서 오른쪽으로 정렬함(default)
>
> row-reverse - 오른쪽에서 왼쪽으로 정렬함.
>
> column - 위에서 아래로 정렬함.  ★가로와 세로의 개념도 회전됨.
>
> column-reverse - 아래에서 위로 정렬함(반대로).  ★가로와 세로의 개념도 회전됨.



- 04_flax_01.html

```html
<head>
	<style>
        .container{
            display: flex;
            border:10px solid royalblue;
            height: 100vh;
        }
        .item{
            height:200px;
            height: 100vh;
        }
        .item1{
            flex-grow: 1;
        }
        .item2{
            flex-grow: 2;
        }
        .item3{
            flex-grow: 4;
        }
    </style>
</head>
<!---------------------------------------------------------------------------->
<body>
    <div class="container">
        <div class="item item1">1</div>
        <div class="item item2">2</div>
        <div class="item item3">3</div>
        <!-- <div class="item item4">4</div>
        <div class="item item5">5</div>
        <div class="item item6">6</div>
        <div class="item item7">7</div>
        <div class="item item8">8</div>
        <div class="item item9">9</div>
        <div class="item item10">10</div>
        <div class="item item11">11</div>
        <div class="item item12">12</div> -->
    </div>
</body>
```

**flex-grow : 숫자**

> 가로영역으로 배열하고, 남은 영역에서 flex-grow의 상대비율로 너비를 맞춤.



- 04_flax_02.html

```html
<head>
	<style>
        .container{
            display: flex;
            border:10px solid royalblue;
            height: 100vh;
            /* 상단 정렬 */
            align-items:flex-start;
            /* 하단 정렬 */
            align-items:flex-end;
            /* 하단 정렬 */
            align-items:center;
            /* 상하단 꽉차게 (기본값) */
            align-items: stretch;
            /* 폰트의 밑줄에 맞게 */
            align-items: baseline;
        }
        .item{
            width: 300px;
            border: 10px solid olive;
            /* 왼쪽 정렬{기본} */
            /* justify-content: flex-start; */
            /* 오른쪽 정렬 */
            /* justify-content: flex-end; */
            /* 중간 정렬 */
            justify-content: center;
            /* 균등 좌우 정렬(안쪽 여백은 좌우 여백의 2배 */
            /* justify-content: space-around; */
        }
        .item1{
            font-size:2rem;
        }
        .item2{
            font-size:10rem;
        }
        .item3{
            font-size:5rem;
        }
    </style>
</head>
<!---------------------------------------------------------------------------->
<body>
    <div class="container">
        <div class="item item1">1</div>
        <div class="item item2">2</div>
        <div class="item item3">3</div>
    </div>
</body>
```

**align-items : 택1 (flex-start | flex-end | center | stretch | baseline);**

> 컨테이너 내부의 가로배열된 오브젝트의 높이방향 정렬 방식을 결정함.
>
> flex-start : 해당 아이템들이 컨테이너의 윗줄에 맞춤.
>
> flex-end : 해당 아이템들이 컨테이너의 아랫줄에 맞춤.
>
> center : 가운데 맞춤.
>
> stretch : 컨테이너를 꽉 채우도록 세로로 늘림.
>
> baseline : 해당 아이템의 텍스트 밑단을 맞추어 정렬함.

**justify-content : 택1 (flex-start | flex-end | center | space-between | space-around | space-evenly)**

> 컨테이너 내부의 가로배열된 오브젝트의 가로방향 정렬 방식을 결정함.
>
> flex-start : 왼쪽으로 붙임.
>
> flex-end : 오른쪽으로 붙임.
>
> center : 모아서 가운데로
>
> space-around : 아이템 양 쪽 끝에 일정한 여백을 차지하도록함. 양쪽 끝 여백은 아이템 사이 여백의 절반.
>
> space-evenly : 양 끝을 포함하여 일정한 여백을 만들어줌.



- 04_flax_03.html

```html
<head>
	<style>
        body {
            background-color: darkmagenta;
        }
        .container {
            display: flex;
            border: 10px solid royalblue;
            height: 100vh;
        }
        .item {
            width: 300px;
            border: 10px solid olive;
            height: 300px;
            line-height: 300px;
        }
        .item2{
			height: 100%;
		}
		.item8{
			align-self: flex-start;
		}
		.item4{
			align-self: flex-end;
		}
    </style>
</head>
<!---------------------------------------------------------------------------->
<body>
    <div class="container">
        <div class="item item1">1</div>
        <div class="item item2">2</div>
        <div class="item item3">3</div>
        <div class="item item4">4</div>
        <div class="item item5">5</div>
        <div class="item item6">6</div>
        <div class="item item7">7</div>
        <div class="item item8">8</div>
        <div class="item item9">9</div>
        <div class="item item10">10</div>
        <div class="item item11">11</div>
        <div class="item item12">12</div>
    </div>
</body>ㅇ
```

**align-self : 택1 (flex-start  | flex-end)**

> 해당 오브젝트의 세로방향 위치를 결정함.
>
> flex-start : 위쪽을 기준으로 맞춤.
>
> flex-end : 아래쪽을 기준으로 맞춤.



- 04_flax_04.html

```html
<head>
	<style>
        body {
            background-color: darkmagenta;
        }
        .container {
            display: flex;
            border: 10px solid royalblue;
            height: 100vh;
        }
        .item {
            width: 300px;
            border: 10px solid olive;
            height: 300px;
            line-height: 300px;
        }
        .item1{
            order:0;
            /* 기본값이 0 */
        }
        .item2{
            order:1;
            /* order가 더 작은 것 보다 뒤로 감. 음수 가능 */
        }
        .item5{
            order:-2;
        }
    </style>
</head>
<!---------------------------------------------------------------------------->
<body>
    <div class="container">
        <div class="item item1">1</div>
        <div class="item item2">2</div>
        <div class="item item3">3</div>
        <div class="item item4">4</div>
        <div class="item item5">5</div>
        <div class="item item6">6</div>
        <div class="item item7">7</div>
        <div class="item item8">8</div>
        <div class="item item9">9</div>
        <div class="item item10">10</div>
        <div class="item item11">11</div>
        <div class="item item12">12</div>
    </div>
</body>
```

**order : 숫자**

> 해당 아이템들의 정렬 기준.
>
> defualt = 0, 음수 가능, order가 작으면 왼쪽, 크면 오른쪽으로 감.



- 05_col.html

```html
<head>
	<link rel="stylesheet" href="col_temp.css">
</head>
<!---------------------------------------------------------------------------->
<body>
    <!-- JUSTIFY-CONTENT
    ============================================ -->
    <div class="container">
        <h1 class="display-1 text-center">JUSTIFY-CONTENT</h1>
        <br>
        <!-- justify-content-center -->
        <div class="row justify-content-center">
            <div class="col-2">1</div>
            <div class="col-2">2</div>
            <div class="col-2">3</div>
        </div>
        <br>
        <!-- justify-content-start -->
        <div class="row justify-content-start">
            <div class="col-2">1</div>
            <div class="col-2">2</div>
            <div class="col-2">3</div>
        </div>
        <br>
        <!-- justify-content-end -->
        <div class="row justify-content-end">
            <div class="col-2">1</div>
            <div class="col-2">2</div>
            <div class="col-2">3</div>
        </div>
        <br>
        <!-- justify-content-between -->
        <div class="row justify-content-between">
            <div class="col-2">1</div>
            <div class="col-2">2</div>
            <div class="col-2">3</div>
        </div>
        <br>
        <!-- justify-content-around -->
        <div class="row justify-content-around">
            <div class="col-2">1</div>
            <div class="col-2">2</div>
            <div class="col-2">3</div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
    <!-- /JUSTIFY-CONTENT -->

    <br>
    <br>

    <!-- ALIGN ITEMS
    ============================================ -->
    <div class="container">
        <h1 class="display-1 text-center">ALIGN ITEMS</h1>
        <br>
        <!-- align-items-center -->
        <div class="row row-vh align-items-center">
            <div class="col">1</div>
            <div class="col">2</div>
            <div class="col">3</div>
        </div>
        <br>
        <div class="row row-vh align-items-start">
            <div class="col">1</div>
            <div class="col">2</div>
            <div class="col">3</div>
        </div>
        <br>
        <div class="row row-vh align-items-end">
            <div class="col">1</div>
            <div class="col">2</div>
            <div class="col">3</div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
    <!-- /ALIGN ITEMS -->

    <br>
    <br>

    <!-- ALIGN SELF
    ============================================ -->
    <div class="container">
        <h1 class="display-1 text-center">ALIGN SELF</h1>
        <br>
        <div class="row align-items-center row-vh">
            <div class="col align-self-start">1</div>
            <div class="col align-self-center">2</div>
            <div class="col align-self-end">3</div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
    <!-- /ALIGN SELF -->

</body>
```

- col_temp.css

```css
body {
    margin: 5rem auto;
    background-color: darkslategray;
    color: white;
}

.container {
    margin: 10px auto;
    padding: 20px auto;
    border: 10px solid yellow;
}

.container h1 {
    text-transform: uppercase;
}

.row {
    border: 10px solid lightblue;
}

.container>.row>div {
    padding: 20px 10px;
    border: 10px solid white;
    font-size: 50px;
    text-align: center;
}

.container>.row>div:nth-child(odd) {
    background: orange;
}

.container>.row>div:nth-child(even) {
    background: green;
}

.row-vh {
    height: 500px;
}

```

justify-content-\***

> 내부의 오브젝트 정렬에 사용.

**align-items-***

> 내부의 오브젝트 정렬에 사용.

**align-self-***

> 해당 오브젝트의 세로위치 변경에 사용.





------

# ※ 참고자료 190529

> - 참고 - 웹폰트 사이트 : <https://fonts.google.com/>
> - 참고 - 폰트어썸 : <https://fontawesome.com/>
> - 참고 - 폰트어썸 애니메이션 : <https://www.npmjs.com/package/font-awesome-animation>
> - 참고 - 폰트어썸 애니메이션 : <https://l-lin.github.io/font-awesome-animation/>
> - 참고 - 플랫아이콘 : <https://www.flaticon.com/>
> - flex 정리된 된 사이트 1 :  <https://css-tricks.com/snippets/css/a-guide-to-flexbox/>
> - flex 정리된 된 사이트 2 : https://naradesign.github.io/article/flex-justify-align.html
> - flex 간단한 게임 : <https://flexboxfroggy.com/#ko>
> - <https://startbootstrap.com/>
> - <http://www.pythontutor.com/>




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

> app말고 다른 이름을 쓰면 별도의 설정이 필요함.
> 인스턴스를 생성시켜 줌.



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

> jinja 문법은 연산이 가능함.
> for 문을 사용한 후 종료를 해야함.



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



------

# ※ 참고자료 190530

> - 참고 - Flask 공식문서 : <http://flask.pocoo.org/>
> - 참고 - Jinja 템플릿 문법 : <http://jinja.pocoo.org/>



