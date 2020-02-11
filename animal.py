class Animal(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age    
	def sit(self):
		print(self.name.title()+ ' is running...')


class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name, age):
		super().__init__(self, name, age)
class Cat(Animal):
	"""docstring for Cat"""
	def __init__(self, name,age):
		super().__init__(self, name, age)

dog = Dog('chang',9)
dog.sit()

	
