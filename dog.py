class Animals():
	def __init__(self,name,age):
		self.name = name
		self.age =age

	def sit(self):
		print(self.name.title()+' is now sitting.')
    
	def roll_over(self):
		print(self.name.title()+' rolled over.')   

'''class Dog(Animal):
	"""docstring for Dog"Animal"""
	def __init__(self, name, age):
		super().__init__(self, name, age)

    def wangwang(self):
    	print('wangwang')'''
		

print('My dog name is '+my_dog.name.title()+".")
print('My dog is '+str(my_dog.age)+' years old.')