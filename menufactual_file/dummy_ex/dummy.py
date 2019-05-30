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