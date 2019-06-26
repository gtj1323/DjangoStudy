[TOC]

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
	```html
	h3{
	    color : blue !important /*<!-- 거의 쓰지 않음. 최 우선순위로 사용-->*/
	}
	```

	**※ 스타일 적용 우선 순위**

	> !important > inline > embedding > file link > browser default
	>   단, 동일한 head에 외부스타일을 나중에 정의할 경우, 나중에 정의한 외부스타일이 먼저 적용. 마지막에 덮어씌워지기 때문.



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
	**※ 글자 크기**
	
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



***


# ※ 참고자료 190528
>  - 참고 - 브라우저 점수 : [http://www.html5test.com](http://www.html5test.com/)
>  - 참고 - 브라우저 사용가능여부 확인 : <https://caniuse.com/>
>  - 참고 - 색상 확인 :<https://www.w3.org/TR/css-color-3/>
>  - 참고 - 색상 확인 : <https://htmlcolorcodes.com/>
>  - 참고 - UI 맞추기 : <https://cantunsee.space/>
>  - 참고 - 부트스트랩 : <https://getbootstrap.com/>
>  - 참고 - Trello : <https://trello.com/> 그룹별로 자료를 공유하고, 표시하는 기능.
>  - 참고 - notion : <https://www.notion.so/> 온라인 앱 통합하여 사용 가능.(유료는 비쌈.)



