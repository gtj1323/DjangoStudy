f = open('mulcam.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')
f.close() #항상 닫아 줘야함.
##############################################위와 아래가 완전히 동일한 코드
with open('mulcam.txt', 'a') as f:  # 'a'를 하면 뒤에 따라 씀.
    for i in range(10):
        f.write(f'This is line {i + 1}.\n')