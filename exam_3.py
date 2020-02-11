'''一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？'''
import math
for i in range(100000):
    k = math.sqrt(i + 100)
    j = math.sqrt(i + 268)

    if k == int(k) and j == int(j):
        print(i)
