import requests
res = requests.get('http://www.yc.ifeng.com/book/3121548/1/')
res.raise_for_status()
with open('romeoandjuliet.txt','wb') as fl:
	for chunk in res.iter_content(100000):
		fl.write(chunk)


with open('romeoandjuliet.txt','r') as fl:

    print(fl.read())