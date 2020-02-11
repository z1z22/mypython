import urllib.request
import urllib.parse

url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
#创建一个handler
handler = urllib.request.HTTPHandler()
#通过handler创建opener
opener = urllib.request.build_opener(handler)
#opener 就是一个对象,发送请求时,就用opener里面的方法.不用urlopen.
#构建请求对象
request = urllib.request.Request(url =url, headers=headers)
response = opener.open(request)


with open('baidu.html', 'wb') as fp:
	fp.write(response.read())
