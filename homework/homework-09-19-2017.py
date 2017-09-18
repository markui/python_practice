import requests
from bs4 import BeautifulSoup

response = requests.get('http://comic.naver.com/webtoon/list.nhn?titleId=651673')

soup = BeautifulSoup(response.text, 'html.parser')


webtoon_titles = [

	item.select_one('a').text
	for item 
	in soup.select('td.title')
	
	]


print(webtoon_titles)
