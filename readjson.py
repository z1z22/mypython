import json
with open('snygpl.json', 'r') as fp:
	lists = json.loads(fp.read())
for my_dict in lists:
	print(my_dict['评论时间'])
	print(my_dict['内容'])
	print(my_dict['追评内容'])