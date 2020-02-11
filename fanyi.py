
import urllib.request
import urllib.parse
import json
#import pprint
from fake_useragent import UserAgent
#获取postURL的地址
post_url = 'https://fanyi.baidu.com/sug'
word =  input('请输入要查询的单词: ')
#构建post表单数据form_data
form_data = {
	'kw':word,
}
#发送请求过程:
ua = UserAgent()
headers = {'User-Agent': ua.random,}
#构建请求对象
request = urllib.request.Request(url = post_url, headers = headers)
#处理post表单数据,encode()将字符串变成字节
form_data = urllib.parse.urlencode(form_data).encode()
#发送请求
response = urllib.request.urlopen(request,data =form_data ) 
#json.loads将json数据转化为字典数据
json_str = response.read().decode()
#print(json_str)
js = json.loads(json_str)
#pprint.pprint(js)

with open('./txt/bbaidu_fanyi.txt','a') as ft:
	ft.write('\n\n      '+ word + ' :')
	js_data = js['data']
	for i in js_data:
		kv = i['k'] + ' : ' + i['v']
		print (kv)

		ft.write('\n'+kv)

print('查询完成,文件已写入./txt/baidu_fanyi.txt')

