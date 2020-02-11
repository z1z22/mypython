'''设置代理访问'''
import urllib.request
import urllib.parse

handler =  urllib.request.ProxyHandler({'http':'111.111.111.111:9999'})
opener = urllib.request.build_opener(handler)
url = 'https://www.baidu.com/s?ie=utf-8&wd=ip'

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

request = urllib.request.Request(url = url, headers = headers)

response = opener.open(request)
with open("ip.html",'wb') as fp:
 	fp.write(response.read())