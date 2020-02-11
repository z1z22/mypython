class People():
	"""docstring for people"""
	name = ""
	age = 0
	__weight = 0
	def __init__(self, n, a, w):
		self.name = n
		self.age = a
		self.__weight = w

	def speak(self):
		print('%s 说: 我 %d 岁.' 
			%(self.name.title(), self.age))

class Student(People):
	"""docstring for student"""
	def __init__(self, n, a, w, g):
		People.__init__(self, n, a, w)
		self.grade = g

	def speak_1(self):
		print('%s说: 我今年%d岁, 上%d年级.' 
			%(self.name.title(), self.age,self.grade))


class Speaker():
	"""docstring for speak"""
	def __init__(self, n, t):
		self.name = n
		self.topic = t

	def speak_2(self):
		print('我叫%s,我演讲的题目是 %s.' 
			%(self.name.title(), self.topic))

class Sample(Speaker, Student):
	def __init__(self,n,a,w,g,t):
		Student.__init__(self, n,a,w,g)
		Speaker.__init__(self,n,t)

test = Sample("tim",15,60,3,"海洋生物")
test.speak_2()
test.speak_1()
		
		