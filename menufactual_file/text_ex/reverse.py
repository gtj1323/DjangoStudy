# 1. line 불러오기


# 2. 뒤집기
with open('number.txt', 'r') as f:
    lines = f.readlines()
lines.reverse()
# 3. 다시 작성하기
with open('number.txt', 'w') as f:
    for line in lines:
        f.write(line)