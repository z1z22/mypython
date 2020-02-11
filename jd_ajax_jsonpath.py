import requests
import json
from inputdigit import inputdigit
import re
import time
from jsonpath import jsonpath
url = 'https://sclub.jd.com/comment/productPageComments.action?callback={}&score=0&sortType=5&pageSize=10'

num = input('请输入JSON编号及Id号(例:fetchJSON_comment98vv10445&productId=7652013): ')
filename = input('请输入保存文件名: ') 
pages = inputdigit('输入评论页数(每页20条): ') 
url = url.format(num)
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
	'Referer': 'https://item.jd.com/893780.html'
} 
f = open('jd/{}.txt'.format(filename),'w')
n = 1
for page in range(1, pages+1):
	data = {'page': page,}

	r = requests.get(url, params = data, headers = headers,timeout = 5)
	# print(r.text)
	pattern = re.compile(r'fetchJSON_comment.*?\((.*?)\);') 
	json_string = pattern.findall(r.text)
	if len(json_string):
		json_string = json_string[0]
	else:
		print('第{}页无内容,已跳过.'.format(n))
		n += 1
		continue

	jsondict = json.loads(json_string)

	obj_ls = jsonpath(jsondict, '$.comments[*]')
	for obj in obj_ls:
		nickname = jsonpath(obj,'$.nickname')
		content = jsonpath(obj,'$.content')
		creationTime = jsonpath(obj,'$.creationTime')

		productColor = jsonpath(obj,'$.productColor')

		productSize = jsonpath(obj,'$.productSize')
		zhui = jsonpath(obj,'$.afterUserComment.hAfterUserComment.content')
		if zhui is False:
			zhui = ['*' * 50]
		text = '{0} {2}\n{3} {4}\n{1}\n\n{5}\n\n'.format(nickname[0], content[0], creationTime[0], productColor[0], productSize[0], zhui[0])

		f.write(text)
	print('第({}/{})页下载完成.'.format(n, pages))
	n += 1
	time.sleep(1)
f.close()
print('保存文件{}.txt成功.'.format(filename))


