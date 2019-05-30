# readlines():파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 함수
#
with open('mulcam.txt', 'r') as f:  #'r'은 읽어 들임.
    lines = f.readlines() # 모든 텍스트를 읽고, 라인마다 하나의 요소로 읽어서 리스트로 만들어 줌.
    for line in lines:
        print(line)

# read() : 파일 내용 전체를 문자열로 return
with open('mulcam.txt', 'r') as f:
    all_text = f.read()
    print(all_text)