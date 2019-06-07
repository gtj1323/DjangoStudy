[TOC]

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

>   이하에서는 바디만 작성(부트스트랩CND제외). 헤더에 추가하는 내용은 있는 경우 추가된 내용만 작성함.



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
	**※ 참고**
	
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
	> flex -  한 줄에 1개만 가능.
	> inline-flex - 한 줄에 여러 그릴 수 있음.

	**flex-direction: 택 1 ( row | row-reverse | column | column-reverse );**
	>해당 오브젝트 <u>**내부에 있는 오브젝트의 정렬**</u>에 사용.
	>row - 왼쪽에서 오른쪽으로 정렬함(default)
	>row-reverse - 오른쪽에서 왼쪽으로 정렬함.
	>column - 위에서 아래로 정렬함.  ★가로와 세로의 개념도 회전됨.
	>column-reverse - 아래에서 위로 정렬함(반대로).  ★가로와 세로의 개념도 회전됨.



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
	
	>가로영역으로 배열하고, 남은 영역에서 flex-grow의 상대비율로 너비를 맞춤.



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
	> flex-start : 해당 아이템들이 컨테이너의 윗줄에 맞춤.
	> flex-end : 해당 아이템들이 컨테이너의 아랫줄에 맞춤.
	> center : 가운데 맞춤.
	> stretch : 컨테이너를 꽉 채우도록 세로로 늘림.
	> baseline : 해당 아이템의 텍스트 밑단을 맞추어 정렬함.

	**justify-content : 택1 (flex-start | flex-end | center | space-between | space-around | space-evenly)**
	>컨테이너 내부의 가로배열된 오브젝트의 가로방향 정렬 방식을 결정함.
	>flex-start : 왼쪽으로 붙임.
	>flex-end : 오른쪽으로 붙임.
	>center : 모아서 가운데로
	>space-around : 아이템 양 쪽 끝에 일정한 여백을 차지하도록함. 양쪽 끝 여백은 아이템 사이 여백의 절반.
	>space-evenly : 양 끝을 포함하여 일정한 여백을 만들어줌.



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
	>해당 오브젝트의 세로방향 위치를 결정함.
	>flex-start : 위쪽을 기준으로 맞춤.
	>flex-end : 아래쪽을 기준으로 맞춤.



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

	**justify-content-\***
	> 내부의 오브젝트 정렬에 사용.

	**align-items-***
	>내부의 오브젝트 정렬에 사용.

	**align-self-***
	
	>해당 오브젝트의 세로위치 변경에 사용.



***

# ※ 참고자료 190529
>  - 참고 - 웹폰트 사이트 : <https://fonts.google.com/>
>  - 참고 - 폰트어썸 : <https://fontawesome.com/>
>  - 참고 - 폰트어썸 애니메이션 : <https://www.npmjs.com/package/font-awesome-animation>
>  - 참고 - 폰트어썸 애니메이션 : <https://l-lin.github.io/font-awesome-animation/>
>  - 참고 - 플랫아이콘 : <https://www.flaticon.com/>
>  - flex 정리된 된 사이트 1 :  <https://css-tricks.com/snippets/css/a-guide-to-flexbox/>
>  - flex 정리된 된 사이트 2 : https://naradesign.github.io/article/flex-justify-align.html
>  - flex 간단한 게임 : <https://flexboxfroggy.com/#ko>
>  - <https://startbootstrap.com/>
>  - <http://www.pythontutor.com/>



