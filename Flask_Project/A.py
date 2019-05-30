from flask import Flask

app = Flask(__name__)


def fuc():
    print('function A.py')


print('top-level A.py')

if __name__ == '__main__':
    print('A.py가 직접 실행')
else :
    print('B.py 모듈로서 실행됨.')