[TOC]

# 파이썬 기본.



## 1.1. 파이썬 기본 다루기.

### 1.1.1. 모듈과 시작점

```python
if __name__ == '__main__':
    코드 작성
```

**\_\_main\_\_**

> 모듈의 이름이 저장되는 변수.
> 해당 파이썬 파일을 직접 실행할 때는 \_\_main\_\_ 이 됨.
> 하지만 파일을 import 하는 방식으로 실행시킬 경우 \_\_모듈명\_\_로 나옴. Ex) \_\_app.py\_\_
> 현재 스크립트 파일이 프로그램의 시작점(entry point) 인지 확인하는 작업에 사용.
>
> - 하지만, 파이썬 인터프리터로 스크립트 파일을 직접 실행했을 때는 모듈의 이름이 아니라 `__main__` 이 들어간다.
> - 어떤 스크립트 파일이던 파이썬 인터프리터가 최초로 실행한 스크립트 파일의 `__name__` 에는 `__main__`이 들어간다.
> - `app = Flask(__name__)`
> `__name__` 파라미터는 Flask 어플리케이션을 구분하기 위한 구분자로 사용



### 1.1.2. 집합 자료형(SET)

 집합(set)은 파이썬 2.3부터 지원되기 시작한 자료형. 집합에 관련된 것을 쉽게 처리하기 ㅜ이해 만들어진 자료형.
```python
s1 = set([1,2,3]) # {1,2,3}인 set리턴
s2 = set("Hello") # {'e', 'H', 'l', 'o'}인 set리턴
print(s1)
```
**set([list])**

> 리스트와 같은 요소를 가진 set을 리턴함.

- 특징
	1. 반복 가능한 객체.
	2. 중복을 허용하지않음.
	3. 순서가 없음. (Unordered). 인덱싱으로 값을 얻을 수 없음.
	자료형의 중복을 제거하기 위한 필터 역할로 종종 사용되기도 함.


- 활용 방법
     ```python
     >>> s1 = set([1, 2, 3, 4, 5, 6])
     >>> s2 = set([4, 5, 6, 7, 8, 9])
     ```

  1. 교집합

     ```python
     >>> s1 & s2
     {4, 5, 6}
     ```
     ```
     >>> s1.intersection(s2)
     {4, 5, 6}
     ```
  
  2. 합집합
  
     ```python
     >>> s1 | s2
     {1, 2, 3, 4, 5, 6, 7, 8, 9}
     
     >>> s1.union(s2)
     {1, 2, 3, 4, 5, 6, 7, 8, 9}
     ```

  
  5. 차집합
     
     ```python
     >>> s1 - s2
     {1, 2, 3}
     >>> s2 - s1
     {8, 9, 7}
     
     >>> s1.difference(s2)
     {1, 2, 3}
     >>> s2.difference(s1)
     {8, 9, 7}
     ```

## 1.2. 파이썬으로 파일 다루기

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



## 1.3. 파이썬으로 txt파일 다루기

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
	> 원래는 반드시 닫야 줘야하지만 with를 씀으로써 극복 가능.

	**with**
	> 컨텍스트 매니저를 불러서 의도치 않은 상황에서도 자동으로 제한하고 해제하는 역할을 해줌.
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



## 1.4. 파이썬으로 CSV파일 다루기

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
	> 파일을 열어서 사용하도록 해줌.
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
	>파일을 한 줄씩 읽어 리스트로 변환하여 리턴함.

	**[text]].strip() [text]].rstrip() [text]].lstrip() **
	> 내용에 들어있는 계행문자(\n)를 제거함. r을 하면 오른쪽, l을 하면 왼쪽을 제거함.

	**[text].split(',')**
	
	> 내용에 들어 있는 문자를 ','를 이용하여 구분 리스트로 반환함.

	**csv.reader(f)**
	
	> csv파일을 읽어 사용하는 상태가 됨.



## 1.5. 스크래핑 기초

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
	>html을 다룰 수 있도록 하여 'bs4.BeautifulSoup 객체를 리턴
	>'html.parser'는 정해져있음.

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
	>  멜론의 경우 header를 함께 보내야만 서버에서 응답이 오기 때문에 같이 보내 주기 위해서 dic형태로 header를 작성하여 함께 보내 주어야함.



## 1.6. 파이썬으로 메일 보내기.

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

## 1.7. 파이썬 가상환경.

코드는 사용환경에 따라 차이가 있을 수 있기 때문에 독립된 환경에서 개발을 할 필요가 있다. 모듈간의 네이밍충돌, 평소와 다른 버전 사용, 등등의 이유로 독립된 환경을 구축해야하는데 이를 위해서 사용하는 독립된 환경이다.

1. 가상환경 만들기.
`python -m venv '가상환경 이름' `
ex) `python -m venv form-venv`
venv는 가상환경을 만드는 모듈
2. 가상환경 활성화.
	- window
    `source '가상환경이름'/Scripts/activate`
    ex) `source form-venv/Scripts/activate`
    - Unix or MacOS
    `source '가상환경이름'/bin/activate`
    ex) `source form-venv/bin/activate`
3. 의존성 생성.
	`pip freeze > requirements.txt`
	현재 사용중인 가상환경에 제공되는 모듈 정보를 저장함.
4. 외부에서 사용시 의존성 가져오기.
	`pip install -r requirements.txt`
	requirements.txt 에 있는 의존성 정보를 가져와 설치함.



***

# ※ 참고자료 190527
>  - 참고자료 - 2019년 웹개발자 로드맵 : <https://github.com/kamranahmedse/developer-roadmap>
> - 참고자료 - 2019년 웹개발자 로드맵 : <https://github.com/devJang/developer-roadmap>
> - 참고자료 - 자바스크립트 공부 : <https://eloquentjavascript.net/>
> - 재미있는 거 : 세계적인 크롤링 사이트 : <http://internetlivestats.com>
> - 웹 표준 : <https://www.w3.org/>
> - ChromeExtension - Wappalyzer : 웹개발에 사용된 언어를 알려줌.
> - ChromeExtension  - ublock origin : 광고 차단.
> - ChromeExtension  - Web Developer
> - [emmet cheat sheet](https://docs.emmet.io/cheat-sheet/) -  html 작성에 유용한 툴.
> - python 문서 : <https://docs.python.org/ko/3.6/>
