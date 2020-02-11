catname = ['z','a','b','c']
name = 'z'
while True:
	
	if name == '':
		break
	if name not in catname:
		catname.append(name)
	if name in catname:
        print('你输入的名字已存在.')
print(catname)