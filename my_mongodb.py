import pymongo
#创建数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#创建数据库
mydb = myclient["scrapy_db"]

#创建集合
mycol = mydb["aisinei"]
#删除集合
#mycol.drop()
#删除集合中的所有文档
# x = mycol.delete_many({})
# print(x.deleted_count, "个文档已删除")

#删除所有name字段中以F开头的文档,"$regex"使用正则
# myquery = { "name": {"$regex": "^F"} }
# x = mycol.delete_many(myquery)
# print(x.deleted_count, "个文档已删除")

# 删除name为淘宝的第一条数据
# myquery = { "name": "Taobao" }
# mycol.delete_one(myquery)

# #判断集合是否已经存在:
# collist = mydb.list_collection_names()
# print(collist)
# # if 'doubanbooks' in collist:
# 	print('集合已存在')

# k = 1
#查询集合中数据
# for x in mycol.find({},{'_id':0,'bookName':1}):
#   print(x)
#   k+=1
# print(k)
# for x in mycol.find({'bookName':'百年孤独'},):
	# print(x)
# k = 1
#查询集合中数据
a = '''<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>tupian</title>
		</head>
		<body>\n'''

c = '''</body>
		</html>'''	
b = []
for x in mycol.find().limit(50).skip(500):
	src = x['src']
	img = '<img src="{}">\n'.format(src)
	b.append(img)

strings = a+''.join(b) + c
print(strings)



with open('pic.html','w') as pf:
	pf.write(strings) 
# print(k)

#查看数据库列表
# dblist = myclient.list_database_names()
# print(dblist)
# if 'scrapy_db' in dblist:
# 	print('数据库已存在')

#现在查看条数为3
# myresult = mycol.find().limit(3)
 
# # 输出结果
# for x in myresult:
#   print(x)
# insert_many
# insert_one
# 增加数据
# sort('x')按x排序
# sort('x', -1)按x倒序
# update_one() 方法只能修匹配到的第一条记录，如果要修改所有匹配到的记录，可以使用 update_many()。
# https://www.cnblogs.com/melonjiang/p/6536876.html




