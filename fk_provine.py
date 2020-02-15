import json, pymysql

db = pymysql.connect('localhost', 'root', 'oooo0000', 'yiqing2020')
cursor = db.cursor()

with open('/users/mac/python/yiqing2020/yiqing_data/[2020-02-10]yiqing_full.json') as ft:
    r = ft.read()

jsdict = json.loads(r)
print(jsdict)
for province in jsdict['data']['areaList']:
    provinceName = province['provinceName']
    sql = ''' ALTER TABLE %s
        ADD CONSTRAINT fk_provinceId
        FOREIGN KEY (provinceId)
        REFERENCES province2020(provinceId)''' %provinceName
    print (sql)
    try:
        cursor.execute(sql)
        print('---------------链接provinceid外键成功------------')
    except:
        db.rollback()
        print('---------------链接provinceid外键不成功-------------')
db.close()
