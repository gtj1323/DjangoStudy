import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.naver.com/').text
print(req)
soup = BeautifulSoup(req, 'html.parser')
# print(soup)
top10 = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')

for item in top10:
    print(item.text)