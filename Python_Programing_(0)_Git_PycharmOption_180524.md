[TOC]

ver.1.0(190529)

# 0. 190524 기초 설정 및 옵션



## 0.0. github

### 0.0.0. Git ?

- **git 이란?**
분산형 버전관리 시스템(DVCS- Distributed Version Control System).
소스코드의 버전, 공유, 이력을 관리하기 위해 사용.

1. **git의 구조**
    working dir  ==  staging area  == git dir(repository)
    3개 층으로 구분.
   
   - working dir   =>   staging area
   
     > stage file 과정 (git add 명령)
   
   - staging area   =>  repo
   
      > commit 과정 (git push 명령)
   - working dir  <=  repo
     
      > checkout the project 과정.

2. **git의 브랜치**
    git은 혼자 쓰기 위해서 사용 하는 것이 아님. 여러사람이 함께 사용하면서 하나의 프로젝트를 완성하기 위해서 사용하는 경우도 있음.
    
   - master
     
     > 전체 브랜치를 합치는 merge권한을 가짐. master 브랜치.
   
   - branch : 전체 브랜치 중 가지로 나온 한 부분. 같은 프로젝트에 포함되어 있음.
     > 전체 브랜치 중 가지로 나온 한 부분. 같은 프로젝트에 포함되어 있음.
   각각의 브랜치는 서로 독립적이며 별도의 히스토리를 가짐.

   - HEAD

     > 현재 사용 중인 (로컬)브랜치를 나타냄. 
   
3. **git의 파일 수정 상태**
    git은 파일의 상태를 4가지로 정의함.
    
    - Untracked
      
      >git에서 관리하지 않는 상태의 파일.
      >최초 파일을 생성한 경우, Unmodified 상태에서 remove한 경우.
    - Unmodified
      
      >저장소의 초기 수정을 하지 않은 상태(init, clone, commit 한 상태)
      >
      >Tracked 이면서 Unmodified인 상태
    - Modified
      
      >init, clone 후 파일을 수정한 상태.
    - Staged
      
      >Modified인 파일을 Stage(`git add`)한 경우.

### 0.0.1. Git Setting

1. **git 설치(윈도우 환경)**
https://git-scm.com/ 에서 설치
2. **사용자 설정**
메일주소는 반듯 GitHub계정과 동일 해야함.
`--globl` 옵션을 사용시 1번만 하면 된다. 만약 빼면 프로젝트마다 다른 이름과 메일 사용.
`git config --global user.name "example"
git config --global user.email test@example.com`
3. **git 명령어 자동 색칠**
`git config --global color.ui ture`
4. **설정 확인**
`git config --global --list`
5. **한글파일명 깨짐 해결**
window 환경 : `git config --global core.quotepath false`
linux / mac 환경 : `git config --global core.autocrlf input`


### 0.0.2. Git 사용1 - Repository에 저장하기.

1. 저장소 설정
    `git init`
    ※ 반드시 작업 디렉토리에서 git을 사용하고 있는지, 작업 후  (master) 표시가 생겼는지 확인.
2. commit 할 목록에 담기
    `git add 파일명.확장자`  : 특정 파일을 목록에 담음.
    `git add .` <-작업디렉토리에 있는 변경사항 전부를 목록에 담음.
    `git add *.확장자` : 해당 확장자인 파일을 목록에 담은.
3. 커밋 하기
    `git commit -m '커밋 메세지.'` 소스코드 상태를 스탭샷을 찍는 것과 동일.
    `staging area`에 담겨 있는 내용을 이력으로 기록.
    `git commit -a -m '커밋 메세지.'` Tracked 상태의 파일을 자동으로 Staging Area에 추가.
    StagingArea는 관리가 힘들어서 -a 옵션을 통해서 사용.
4. 상태 확인하기
    `git status`
5. 저장소(repository)에 담기
    github 저장소(원격저장소) url을 origin 이라는 이름으로 설정
    `$ git remote add origin https://github.com/example/test.git`

     - Github repository를 처음 생성한 경우.
     - Github repository가 있는 경우.

### 0.0.3. Git 사용 2 - Repository 가져오기. (clone)

1. Repo를 로컬dir로 가져오기.
   `git clone git://github.com/example/test.git 폴더명 `
   grit(혹은 폴더명)이라는 하위 dir를 생성하여 원격 저장소에서 로컬로 복사함.
   이 때, 브랜치를 포함한 히스토리가 함께 복사됨.
   ※ 반드시 작업 디렉토리에서 git 사용여부를 확인한 후 사용.

### 0.0.4. Git 사용 3 - Repository 가져오기.

1. 파일 무시하기(.gitignore 파일)
로그, .class, .exe 등 자동생성, 등의 이유로 관리가 필요하지 않은  파일.
운영체제, 사용언어, 사용에디터에 따라 차이가 있음.
2. 작성 방법
\# a comment : 해당 줄 무시
\*.a : 확장자가 .a인 파일 무시
\!lib.a : 윗 줄에서 확장자가 .a인 파일은 무시하게 했지만 lib.a는 무시하지 않는다.
/TODO : 루트 디렉터리에 있는 TODO 파일은 무시하고 subdir/TODO처럼 하위 디렉터리에 있는 파일은 무시하지 않는다.
build/ : build/ 디렉터리에 있는 파일은 무시하지 않는다.
doc/*.txt : 'doc/notes.txt' 같은 파일은 무시, doc/server/arch.txt는 무시하지 않는다.
\

## 0-121324134. 


- from을 이용한 간단한 작성

```html

```

결과







***


# ※ 참고자료 190524
>  - git 다운로드 사이트 : <https://git-scm.com/>
