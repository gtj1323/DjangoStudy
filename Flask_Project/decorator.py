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