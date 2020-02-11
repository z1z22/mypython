from random import randint

class Die():
	"""docstring for Die"""
	def __init__(self,sides):
		self.sides = sides

	def roll_die(self):
		self.rool = randint(1,self.sides)
		print(self.rool)

my_die = Die(6)
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()





