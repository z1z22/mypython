import pymysql
import pymongo
'''将数据由mongo 导入 mysql'''
# SELECT LAST_INSERT_ID()
# 获取最后插入的ID适用于自增项目


class PyMongo(object):
    '''创建mongodb类,提供查询工作'''

    def __init__(self, database):
        '''注册登陆mongodb'''
        client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = client[database]

    def getlist(self, collection, title):
        '''从mongodb中查询提取数据,返回数据列表'''
        coll = self.db[collection]
        result = coll.find({'title': title}, {'picname': 1,
                                              'src': 1, 'picstore': 1})  # .distinct('src')
        return result

    def insert(self, collection, **kw):
        '''向mongodbcollection里插入数据'''
        coll = self.db[collection]

        data1 = {
            'id': '20170101',
            'name': 'Jordan',
            'age': 20,
            'gender': 'male'
        }
        # data2 = {
        # 	'id': '20170101',
        # 	'name': 'Jordan',
        # 	'age': 20,
        # 	'gender': 'male'
        # 	}

        coll.insert_one(data1)
        # result = coll.insert_many([data1,data2])


class PyMysql(object):
    """ PyMysql类,实现登陆及查询、添加数据工作"""

    def __init__(self, database):
        '''注册并登陆Mysql'''
        self.db = pymysql.connect('localhost', 'root', 'oooo0000', database)

    def getlist(self, mytable):
        '''查询关联数据库, 从mysql里提取并返回id,及其他字段字典列表'''
        # sql = "SELECT * FROM %s where titletag_id>10"%mytable
        sql = "SELECT * FROM %s where titletag_id=27" % mytable
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        titlelist = []
        try:
            # 使用 execute()  方法执行 SQL 查询
            cursor.execute(sql)
            # fetchall()获取所有记录列表,fetchone()方法获取单条数据.
            results = cursor.fetchall()
            for row in results:
                item = {'id': row[0], 'title': row[1]}
                titlelist.append(item)
        except:
            print ("Error: unable to fetch data")

        return titlelist

    def insert(self, table, picdict, picid):
        '''向mysql插入数据,具体字段需根据数据库结构做修改'''
        cursor = self.db.cursor()
        sql = "INSERT INTO %s(PICNAME,SRC,PICSTORE,PICTITLE_ID) VALUES('%s','%s','%s','%s')" % (
            table, picdict['picname'], picdict['src'], picdict['picstore'], picid,)
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def close(self):
        '''关闭数据库'''
        self.db.close()


class DuplicatesPipeline(object):
    '''用于去重和去除无效item'''

    def __init__(self):
        self.src_ls = set()

    def process_item(self, item):
        if item['src'] is None:
            print('Drop empty item!!')
            return None
        elif item['src'] in self.src_ls:
            print("Duplicate item found")
            return None
        else:
            self.src_ls.add(item['src'])
            return item


def main():
    # 实例化并登陆mysql
    sq = PyMysql('mydjango')
    # 实例化并登陆mongodb
    mg = PyMongo('scrapy_db', )

    titlelist = sq.getlist('meitu_title')
    for titledict in titlelist:
        print(titledict)
        piclist = mg.getlist('ishsh', titledict['title'])
        # piclist = mg.getlist('mmonly',titledict['title'])
    # 	# dp = DuplicatesPipeline()
        for picdict in piclist:
            # if 'zhuamei.net' in picdict['src']:
            # 	picdict['src'] = picdict['src'].replace('zhuamei.net', 'zhuamei5.com')
            # else:
            # 	picdict['src'] = 'http://www.zhuamei5.com/' + picdict['src']
            # 		# picdict = dp.process_item(picdict)
            print(picdict['picname'], picdict['src'], str(titledict['id']))
            # if picdict is None:
            # 	continue∫
            # else:
            sq.insert('meitu_pic', picdict, titledict['id'])
    sq.close()


if __name__ == '__main__':
    main()
