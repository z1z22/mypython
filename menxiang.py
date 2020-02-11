import requests
from bs4 import BeautifulSoup

url = 'https://www.lz13.cn/mingrenmingyan/4956.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
r = requests.get(url = url, headers = headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')
text_zhu = soup.select('.PostContent > p')
for text in text_zhu:
	print(text.text)


