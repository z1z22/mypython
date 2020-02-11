class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name

	def set_scort(self,score):
		if 0 <= score <=100:
		    self.__score = score
		else:
			raise ValueError('bad score')

	def get_grade(self):
		if self.__score >=90:
			return ' A'
		elif self.__score >=60:
			return ' B'
		else:
			return ' C'
	
    #def show(self):
        #return('%s: %s' %(self.name,self.score))
   

bart = Student('bart simpson', 69)
print (bart.get_grade())
print(bart.get_name())


#print(bart.show())
#print(bart.__name.title()+bart.get_grade())

		