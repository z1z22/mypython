import urllib.request
import urllib.parse

post_url = ''

form_data = {
	
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
request = urllib.request.Request(url = post_url,headers = headers)
form_data = urllib.parse.urlencode(form_data),encode()
response = urllib.request.urlopen(request, data = form_data)
print(response.read().decode())