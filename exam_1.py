'''题目：有四个数字：1、2、3、4，能组成
多少个互不相同且无重复数字的三位数？各是多少？'''
li = []
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if i != k and i != j and k != j:
				a = i * 100 + j * 10 + k
				li.append(a)

print(li)
print('共',len(li),'个.')