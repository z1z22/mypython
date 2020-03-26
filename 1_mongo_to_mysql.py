import pymysql
import pymongo
'''将数据由mongo 导入 mysql'''

client = pymongo.MongoClient(host='localhost', port=27017)
mongo_db = client['scrapy_db']
# coll = mongo_db['mmonly']
coll = mongo_db['meitulu']

db = pymysql.connect('localhost', 'root', 'oooo0000', 'mydjango')
cursor = db.cursor()


def mysql_insert(tag):
    # print(item)
    sql = "INSERT INTO meitu_tag(TAG) VALUES('%s')" % (tag)
    # item['tag'],
    # item['src'],
    # item['picstore'])

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def mysql_close():
    db.close()


def mongodb_find():
    item_list = coll.find({}, {'title': 1}).distinct('title')
    # for item in item_list:
    # taglist = list(set([i['tag'] for i in item_list]))
    return item_list


def main():
    tag_list = mongodb_find()
    for tag in tag_list:
        print(tag)

        mysql_insert(tag)
    mysql_close()


if __name__ == '__main__':
    main()
