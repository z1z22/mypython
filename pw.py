import pymysql,pymongo
import datetime


db = pymysql.connect('localhost', 'root', 'oooo0000', 'mypw')
cursor = db.cursor()

def select_mysql(string):
    sql = "SELECT * from `pw_hub` where %s" % string
    # print(sql)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    except:
        db.rollback()
        return None
    db.close()

def insert_mysql(item):
    sql = '''INSERT INTO `pw_hub` (
        `date`,
        `webname`,
        `username`,
        `password`,
        `email`,
        `telephone`
        ) VALUES('%s','%s','%s','%s','%s','%s')''' %(
            str(datetime.date.today()),
            item['webname'],
            item['username'],
            item['password'],
            item['email'],
            item['telephone']
            )
    # print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print('---------------写入pw_hub成功------------')
    except:
        db.rollback()
        print('---------------写入不成功------------')
    db.close()




def main():
    item={}
    itemlist = ['password','username','webname','email','telephone']
    i = input('您要查询的字段：用户名(1),网站或应用名称(2),邮箱(3),手机号(4),其余键退出:')
    if i in ['0','1','2','3','4']:
        i = int(i)
    else:
        exit()

    while True:
        item[itemlist[i]] = input('请输入{}:'.format(itemlist[i]))
        string = "{}='{}'".format(itemlist[i], item[itemlist[i]])
        print(string)
        info = select_mysql(string)
        # print（info）

        if len(info) != 0:
            print('\n查询到以下{}条信息：'.format(len(info)))
            for row in info:
                print('登记时间：{}；应用：{}；用户名：{}；密码：{}；邮箱：{}；电话：{}'.format(row[1],row[2],row[3],row[4],row[5],row[6]))
            # print(info)

        else:
            print('\n------未查到您用户名匹配的信息------')
        
        q = input('\nq退出，n新建信息，任意键重新查询:')
        if q == 'q' or q == 'Q':
            print('q退出程序')
            exit()
        elif q == 'n'or q == 'N':
            print ('\n新建信息')
            break
    item['username'] = input('请输入用户名：')
    item['webname'] = input('请输入网站或应用名称：')
    item['password'] = input('请输入密码：')
    item['email'] = input('请输入邮箱：')
    item['telephone'] = input('请输入手机号：')
    

    insert_mysql(item)

if __name__ == '__main__':
    main()