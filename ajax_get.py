import urllib.request
import urllib.parse

#Request URL: https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=0&limit=20
#start从第几条开始,limit显示多少条数据.
url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&'
page =1
number = 20
#构建个头参数
data = {
	'start':(page - 1)*number,
	'limit': number,
}
#将字典转化为query_string
query_string = urllib.parse.urlencode(data)

url += query_string
#构建请求对象
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
request = urllib.request.Request(url = url ,headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode())