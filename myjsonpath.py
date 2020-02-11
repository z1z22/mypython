from jsonpath import jsonpath
import json
# f = open('jdt.txt','w')

object = json.load(open('jjd.json','r', encoding = 'utf8'))

obj_ls = jsonpath(object, '$.comments[*]')
for obj in obj_ls:
	nickname = jsonpath(obj,'$.nickname')
	content = jsonpath(obj,'$.content')
	creationTime = jsonpath(obj,'$.creationTime')
	productColor = jsonpath(obj,'$.productColor')
	productSize = jsonpath(obj,'$.productSize')
	zhui = jsonpath(obj,'$.showOrderComment.content')

	print('{0} {2}\n{3}{4}\n{1}\n{5}\n\n'.format(nickname,content,creationTime,productColor,productSize,zhui))
# for obj in obj_ls:
# 	f.write(str(obj['id']) + '  ' + obj['creationTime'] + '\n' + obj['content']+'\n\n')
# f.close()
