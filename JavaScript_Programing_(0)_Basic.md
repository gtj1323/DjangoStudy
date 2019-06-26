# 1. JavaScript 기초

## 1.1. JavaScript 함수.

### 1.1.1. JavaScript 함수 정의 방법.

1. 함수 선언식으로 함수 작성.
   ```Javascript
   function add(num1, num2){
       return num1+num2
   }
   ```

2. 함수 표현식으로 함수 작성.
   ```Javascript
   const sub = function(num1,num2){
       return num1 - num2
   }
   ```

### 1.1.2. Arrow Fucntion
1. function을 생략해도됨
2. 함수에 매개변수가 단하나 뿐이면 , () 생략가능
3. 함수바디에 표현식이 아니라면 ()와 return도 생략가능.



JavaScript는 callstack, webAPI, callback Qeue 구조를 이해해야함. 