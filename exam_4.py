'''题目：输入某年某月某日，判断这一天是这一年的第几天？'''

from datetime import datetime
import time

dt = datetime(2019, 3 , 18)
print (dt)
t =time.strptime(str(dt),'%Y-%m-%d %X')
print(t)
