import requests
# from pprint import pprint # Json, list를 보기 좋게 출력함.
from bs4 import BeautifulSoup

# 1. 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장
req = requests.get('https://finance.naver.com/sise/').text
# print(req)
# print(req.text)
# print(req.status_code)

# 2. 정보를 조작하기 전 편하게 바꾸고,
soup = BeautifulSoup(req, 'html.parser')
print(type(soup))
# 3. 바꾼 정보 중 원하는 것만 뽑아서 ,출력한다.
kospi = soup.select_one('#KOSPI_now')
print(kospi.text)