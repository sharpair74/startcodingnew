import requests
from bs4 import BeautifulSoup

# naver 웹사이트 연결
response = requests.get("https://www.naver.com")
# naver html 가져오기
html = response.text
# css 로 html 테그 구분해서 가져오기
soup = BeautifulSoup(html,'html.parser')
# id NM_set_home_btn 인 놈 가져오기
word = soup.select_one("#NM_set_home_btn")

# text 하나 가져오기11111
print(word.text)