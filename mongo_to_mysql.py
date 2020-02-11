import pymysql
import pymongo
'''将数据由mongo 导入 mysql'''

client = pymongo.MongoClient(host='localhost', port=27017)
mongo_db = client['scrapy_db']
coll = mongo_db['asnasn']

db = pymysql.connect('localhost','root','oooo0000','meitu')
cursor = db.cursor()

def mysql_create_table():

	cursor.execute("DROP TABLE IF EXISTS ASNASN")

	sql = '''CREATE TABLE ASNASN(
			PICNAME CHAR(40),
			TITLE CHAR(100),
			TAG CHAR(20),
			SRC CHAR(100),
			-- CRAWLED DATE(),
			PICSTORE CHAR(200))
		'''
	cursor.execute(sql)
	return


def mysql_insert(item):
	print(item['picstore'])
	sql = "INSERT INTO meituxiu_meitu(TITLE,PICNAME,TAG,SRC,PICSTORE)\
	VALUES('%s','%s','%s','%s','%s')"%(	
		item['title'].replace('/','_'),
		item['picname'],
		item['tag'],
		item['src'],
		item['picstore'])
	# cursor.execute('insert into asnasn values(%s,%s,%s,%s,%s)'%(item['picname'],item['title'],item['tag'],item['src'],item['picstore']))
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()

def mysql_close():
	db.close()

def mongodb_find():
	item_list = coll.find()#.limit(10)
	# for item in item_list:
	return item_list

def main():	
	# mysql_create_table()
	item_list = mongodb_find()
	for item in item_list:
		# print(dict(item))
		mysql_insert(item)
	mysql_close()


if __name__ == '__main__':
	main()




	