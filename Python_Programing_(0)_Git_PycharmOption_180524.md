[TOC]

ver.1.0(190529)

# 0. 190524 기초 설정 및 옵션

Git에 대해서 알아 봅시다.

## 0.1. Git ?

- **0.1.1 git 이란?**
  분산형 버전관리 시스템(DVCS- Distributed Version Control System).
  소스코드의 버전, 공유, 이력을 관리하기 위해 사용.

### 0.1.1 git 알기.

1. **git의 구조**
   working dir  ==  staging area  == git dir(repository)
   3개 층으로 구분.
   ![Git_layer](https://user-images.githubusercontent.com/43361320/58688063-5daaa480-83be-11e9-8500-c1d940ab82fc.png)

   - working dir   =>   staging area

     > stage file 과정 (git add 명령)

   - staging area   =>  repo

     > commit 과정 (git push 명령)

   - working dir  <=  repo

     > checkout the project 과정.

2. **git의 브랜치**
   git을 사용 중 목적에 따라 격리한 상태로 무언가를 만들 때 사용.
   파일을 안전하게 격리된 상태에서 다른 방향으로 수정, 나누어 작업하는 경우 

   - master

     > 전체 브랜치를 합치는 merge권한을 가짐. master 브랜치.

   - branch : 전체 브랜치 중 가지로 나온 한 부분. 같은 프로젝트에 포함되어 있음.

     > 전체 브랜치 중 가지로 나온 한 부분. 같은 프로젝트에 포함되어 있음.
     > 각각의 브랜치는 서로 독립적이며 별도의 히스토리를 가짐.

   - HEAD

     > 현재 사용 중인 (로컬)브랜치를 나타냄. 
   
3. **git의 파일 수정 상태**
   git은 파일의 상태를 4가지로 정의함.
   ![Git_modification_layer](https://user-images.githubusercontent.com/43361320/58688092-6e5b1a80-83be-11e9-8228-d03f54f924a4.png)

   - Untracked

     > git에서 관리하지 않는 상태의 파일.
     > 최초 파일을 생성한 경우, Unmodified 상태에서 remove한 경우.

   - Unmodified

     > 저장소의 초기 수정을 하지 않은 상태(init, clone, commit 한 상태)
     >
     > Tracked 이면서 Unmodified인 상태

   - Modified

     > init, clone 후 파일을 수정한 상태.

   - Staged

     > Modified인 파일을 Stage(`git add`)한 경우.

### 0.1.2. Git Setting

1. **git 설치(윈도우 환경)**
   https://git-scm.com/ 에서 설치
2. **사용자 설정**
   메일주소는 반듯 GitHub계정과 동일 해야함.
   `--globl` 옵션을 사용시 1번만 하면 된다. 만약 빼면 프로젝트마다 다른 이름과 메일 사용.
   `git config --global user.name "example"
   git config --global user.email test@example.com`
   ※ 이름은 틀려도 큰 문제가 없지만 메일 주소가 틀리면 저장이 올바르게 되지 않음.
3. **git 명령어 자동 색칠**
   `git config --global color.ui true`
4. **설정 확인**
   `git config --global --list`
5. **한글파일명 깨짐 해결**
   window 환경 : `git config --global core.quotepath false`
   linux / mac 환경 : `git config --global core.autocrlf input`



## 0.2. github 브랜치 1개 관리.


### 0.2.1. Git 사용1 - Repository에 저장하기.

1. 저장소 설정
    `git init`
    ※ 반드시 작업 디렉토리에서 git을 사용하고 있는지, 작업 후  (master) 표시가 생겼는지 확인.
3. commit 할 목록에 담기
	공유할 파일을 정하는 과정.
    `git add 파일명.확장자`  : 특정 파일을 목록에 담음.
    `git add .` <-작업디렉토리에 있는 변경사항 전부를 목록에 담음.
    `git add *.확장자` : 해당 확장자인 파일을 목록에 담음.
	`git add -i` : 파일을 목록에 담을 때, 대화식으로 함.
4. commit 하기
   push하여 공유 혹은 최종본을 올리기 전 필수 과정.
   `git commit -m 'commit 메세지.'` 소스코드 상태를 스탭샷을 찍는 것과 동일.
   `staging area`에 담겨 있는 내용을 이력으로 기록.
   `git commit -a -m 'commit 메세지.'` Tracked 상태의 파일을 자동으로 Staging Area에 추가.
   StagingArea는 관리가 힘들어서 -a 옵션을 통해서 사용.


### 0.2.2. Git 사용 2 - Repository 가져오기. (clone)
- Repo를 로컬dir로 가져오기.
`git clone /로컬저장소경로` 로컬 저장소를 복제 하는 명령.
`git clone 사용자명@호스트:/원격저장소경로` 원격 서버의 저장소를 복제하는 명령.
Ex) `git clone git://github.com/example/test.git 폴더명 `
   grit(혹은 폴더명)이라는 하위 dir를 생성하여 원격 저장소에서 로컬로 복사함.
   이 때, 브랜치를 포함한 히스토리가 함께 복사됨.
   ※ 반드시 작업 디렉토리에서 git 사용여부를 확인한 후 사용.
### 0.2.3. Git 사용 3 - 로컬dir update. (pull)
- `git pull`
현재 사용중인 디렉토리를 최신화함.(clone 후 다른 곳에서 push, commit한 내용을 업데이트함.)

### 0.2.4. Git 사용 3 - 상태확인, 수정, 삭제, 파일 제외.

1. 상태 확인하기
   `git status`

1. 저장소(repository)에 담는 과정의 개념
   github 저장소(원격저장소) url을 origin 이라는 이름으로 설정
   `$ git remote add origin https://github.com/example/test.git`

   - Github repository를 처음 생성한 경우 (**최초 commit**).
     최초 add 된 모든 파일을 commit함.
   - Github repository가 있는 경우 (**변경사항 commit**).
     Saging Area에 옮긴 파일(add 한 파일)만 commit 대상. 추가되지 않은 파일은 제외됨.

2. Tracked상태인 파일 **워킹 디렉토리에서 삭제함.**
   `git rm 파일명.확장자`
   워킹 디렉토리에서 삭제됨.
   파일을 수정한 경우 -f 옵션 추가
   **※ rm을 이용하여 지우면, Stage Area에 있는 파일은 존재함, commit 하면 추가됨.**

3. **Staging Area의 파일 삭제**, 워킹 디렉토리에서는 파일을 지우지 않음.
   add 명령어로 Staging Area에 있는 파일을 지움.
   `git rm --cached log.txt` #log.txt 파일을 commit된 상태에서 뺌.
   commit 하면 Repo에서 D(삭제)됨.
   `git rm log/\*log`

5. 파일명 변경
   `git mv 전파일명 새파일명`
   Ex) `git mv README.txt README`

   - Ex)는 아래 동일 명령 3줄과 동일함.

     `mv README.txt README`
     `git rem README.txt`
     `git add README`

6. commit 히스토리 조회하기
   `git log` 명령을 통해서 볼 수 있음.
   commit 고유한 hash값, commit 메세지, 시간과 날짜, 작성자<계정>을 전부 표시.

   - `git log`명령 옵션.

	   | git log 옵션 키 | 설  명                                                       |
	   | --------------- | ------------------------------------------------------------ |
	   | -p              | 각 commit에 적용된 패치를 보여준다.                          |
	   | --stat          | 각 commit에서 수정된 파일의 통계 정보를 보여준다.            |
	   | --shortstat     | '--stat' 명령의 결과 중에 수정한 파일, 추가된 줄, 삭제된 줄만 보여준다. |
	   | --name-only     | commit 정보 중에서 수정된파일의 목록만 보여준다.             |
	   | --name-status   | 수정된 파일의 목록을 보여줌. <br />추가, 수정, 삭제한 것인지도 보여준다. |
	   | --abbrev-commit | 40자짜리 SHA-1 체크섬을 처음 몇자만 보여준다.                |
	   | --relative-date | '2주전' 처럼 상대적인 형식으로 시간을 보여줌.                |
	   | --graph         | 브랜치와 머지 히스토리 정보까지 아스키 그래프로 보여준다.    |
	   | --pretty        | 지정한 형식으로 보여줌.<br />-\<n>, --pretty(oneline, short, full, fuller, format)<br />옵션을 사용. format은 원하는 형식으로 출력할 때 사용.<br /><br />Ex) <br />-\<n>  :  최근 n개의 커밋 목록 출력<br />--pretty  =>  출력포맷 지정 해주는 옵션<br />--pretty=oneline<br />--pretty=short<br />--pretty=full<br />--pretty=fuller<br />--pretty=format:"패턴" |

   - `git log --pretty=format:"패턴 옵션"`
     Ex) `git log --pretty=format:"%h - %an, %ar : %s"

     | Option | Description of Output                            |
     | ------ | ------------------------------------------------ |
     | %H     | Commit hash 해쉬값                               |
     | %h     | Abbreviated commit hash 해쉬값 짧게 나옴.        |
     | %T     | Tree hash                                        |
     | %t     | Abbreviated tree hash                            |
     | %P     | Parent hashes                                    |
     | %p     | Abbreviated parent hashes                        |
     | %an    | Author name                                      |
     | %ae    | Author e-mail                                    |
     | %ad    | Author date (format respects the --date= option) |
     | %ar    | Author date, relative                            |
     | %cn    | Committer name                                   |
     | %ce    | Committer email                                  |
     | %cd    | Committer date                                   |
     | %cr    | Committer date, relative                         |
     | %s     | Subject(커밋 메세지)                             |

7. 파일 상태를 unstage 상태로 변경.
     `git reset HEAD 파일명`
     이미 commit한 파일을 unstage 상태로 변경함.
     commit 하면 수정, 삭제, 추가되지 않음.

8. Modified 파일 되돌리기.
    `git checkout -- 파일명` : 특정 파일을 가장 최근의 커밋 버전에서 꺼내어 복원함.
   위 명령은 로컬의 변경 내용을 변경 전 상태(HEAD)로 되돌림. 다만, 이미 인덱스에 추가된 변경 내용과 새로 생성한 파일은 그대로 남음.

9. 파일 무시하기(.gitignore 파일)
   로그, .class, .exe 등 자동생성, 등의 이유로 관리가 필요하지 않은  파일.
   운영체제, 사용언어, 사용에디터에 따라 차이가 있음.

   - 작성 방법 (<https://www.gitignore.io/> 여기서 자동으로 만들 수 있음.)

     ```
     # a comment - 해당 줄의 '#'뒤는 무시함.
     \*.a	   # 확장자가 .a인 파일 무시함.
     \!lib.a	   # 윗 줄에서 확장자가 .a인 파일은 무시하게 했지만 lib.a는 무시하지 않음.
     /TODO	   # 루트dir에 있는 TODO파일 무시, subdir/TODO처럼 dir하위에 있으면 무시하지 않음.
     build/	   # build/ 디렉터리에 있는 파일은 무시하지 않음.
     doc/*.txt  # 'doc/notes.txt' 같은 파일은 무시, doc/server/arch.txt는 무시하지 않음.
     ```

10. 내장 GUI 명령
     `gitk`



## 0.3. Git 함께 사용하기. (여러개의 브랜치를 관리.)

- Git에서는 격리된 master와 격리된 새로운 브랜치를 생성하여 별도의 수정 삭제, 병합 등이 가능함.

### 0.3.1. Git 브랜치 생성, 삭제.

- 새로운 브랜치 생성, 삭제 명령
  `git checkout -b feature_x` feature_x라는 새로운 브랜치를 만들고 갈아탐.
  `git checkout master` 마스터 브랜치로 갈아탐.
  `git branch -d feature_x` feature_x 라는 브랜치 삭제
  `git push origin <가지이름>` 새로 만든 가지를 원격 저장소로 전송하기 전까지는 다른 사람들이 접근 불가.

### 0.3.2. 브랜치 병합.

1. 병합(merge).
	병합은 서로다른 프로젝트를 합치는 과정.
	`git merge <가지이름>`
	문제는 가끔 충돌(같은 파일에 내용이 다른 부분이 존재하는 경우.)이 일어남.
2. 병합 전후 비교.
	git diff <원래 가지> <비교 대상 가지>
	ㅇ
3. 충돌 해결 후 파일 추가.
	충돌이 일어난 경우 충돌을 해결하고 파일을 별도로 저장하야 함.
	`git add <파일 이름>`
4. master 바꾸기
	`git reset --hard origin/master`
5. 로컬의 모든 변경 내용과 확정본을 포기.
	`git fetch origin` :로컬에 있는 모든 변경 내용과 확정본을 포기하는 명령.



# ※ 참고자료 190524
>  - git 다운로드 사이트 : <https://git-scm.com/>
>  - gitignore 사이트 : <https://www.gitignore.io/>
>  - <https://rogerdudler.github.io/git-guide/index.ko.html>
>  - git 공식 한글사용 설명 : <https://git-scm.com/book/ko/v2>
>  - git 입문 사용 설명 : <https://backlog.com/git-tutorial/kr/intro/intro1_1.html>
>  - git 간편 사용 설명 : <https://rogerdudler.github.io/git-guide/index.ko.html>

