class Company(object):
	'''魔法函数(__xxx__的内置函数)的学习'''
	# def __init__(self,employee_list):

	# 	self.employee = employee_list
	# def __getitem__(self,item):
	# 	'''把类变为可迭代类型'''

	# 	return self.employee[item]
	# def __len__(self):
	# 	return len(self.employee)
	


company = Company(['zzz','ddd','kkk'])

# employee = company.employee

for em in company:
	'''有了__getitem__这个魔法函数后,可以直接对类进行迭代'''
	print(em)
company1 = company[:2]
#还可以进行切片
print(len(company1))