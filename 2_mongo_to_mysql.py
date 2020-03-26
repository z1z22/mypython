import pymysql
import pymongo
'''将数据由mongo 导入 mysql'''

client = pymongo.MongoClient(host='localhost', port=27017)
mongo_db = client['scrapy_db']
coll = mongo_db['meitulu']
# coll = mongo_db['mmonly']

db = pymysql.connect('localhost', 'root', 'oooo0000', 'mydjango')
cursor = db.cursor()


def mysql_insert(title, titleid):
    # print(item)
    sql = "INSERT INTO meitu_title(TITLE, titletag_id) VALUES('%s','%s')" % (
        title, titleid,)
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


def idmysql(mytable):
    '''从mysql里提取id列表'''
    # sql = "SELECT * FROM %s where id>10"%mytable
    sql = "SELECT * FROM %s" % mytable
    taglist = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            item = {'id': row[0], 'tag': row[1]}
            taglist.append(item)
    except:
        print ("Error: unable to fetch data")

    return taglist


def searchmongo(tag):
    item_list = coll.find({'title': tag}, {'dirname': 1}).distinct(
        'dirname')  # .sort('title')
    # title_list = list(set([i['dirname'] for i in item_list]))
    return item_list


def main():

    taglist = idmysql('meitu_tag')
    # print(taglist)
    for tagdict in taglist:
        titlelist = searchmongo(tagdict['tag'])
        # print(titlelist)
        for title in titlelist:
            print(title,tagdict['id'])

            mysql_insert(title, tagdict['id'])
    mysql_close()

    # titlelist = searchmongo('Aiss爱丝')
    # for title in titlelist:
    #     print(title)

        # mysql_insert(title, 27)
    # mysql_close()


if __name__ == '__main__':
    main()
