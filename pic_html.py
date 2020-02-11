import pymongo,webbrowser
from inputdigit import inputdigit

myclient = pymongo.MongoClient("mongodb://localhost:27017/")#创建数据库
mydb = myclient["scrapy_db"]#创建数据库
mycol = mydb["aisinei"]#创建集合

def mongodbtohtml(limit, skip):

	html = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>picture</title>
</head>
<body style="background: #0e0e0e;">
<div align="center">{}</div> 
</body>
</html>'''	
	img_list = []
	for x in mycol.find().limit(limit).skip(skip):
		src_html = '<img src="{}">\n'.format(x['src'])
		img_list.append(src_html)
		img_html = ''.join(img_list)

	strings = html.format(img_html)
	# print(strings)
	return strings

def main():
	'''将mangodb的图片转换为html打开'''
	filename = input('filename: ')
	skip = inputdigit('skip: ')
	limit = inputdigit('limit: ')
	strings = mongodbtohtml(limit, skip)
	filepath = '/Users/mac/python/htmlfile/{}.html'.format(filename)
	with open(filepath, 'w') as pf:
		pf.write(strings)
	print('{} is write done'.format(filename.title()))
	file_browser = 'file://'+filepath
	webbrowser.open(file_browser)

if __name__ == '__main__':
	main()
