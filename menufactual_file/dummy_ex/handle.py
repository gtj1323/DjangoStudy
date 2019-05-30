import os

os.chdir(r'C:\Users\student\PycharmProjects\menufactual_file\dummy_ex')
# 맥북 사용 시 슬래시 사용
filenames = os.listdir('.')
for filename in filenames:
    txt = os.path.splitext(filename)[-1].lower()
    if txt == '.txt':
       os.rename(filename, f'지원자_{filename}')

'''
os.path.splitext(filename) 확장자와 파일명을 구분
('c:/tempython/data.txt') => ('c:/tempython/data, .txt')
'''