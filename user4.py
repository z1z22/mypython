class User(object):
	"""docstring for User"""
	def __init__(self, first_name,last_name):
		
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts =0

	def full_name(self):
	    return self.full_name.title()+self.last_name.title()

	def increment_login_attempts(self):
		self.login_attempts += 1
		
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		

	def describe_user(self):
		print(self.first_name.title()
			+self.last_name.title()
			+' is VIP')

	def greet_user(self):
		print('Hello! '+self.first_name.title()
			+self.last_name.title())

user = User('zhou','zhu')
user.greet_user()
user.describe_user()
user.increment_login_attempts()

print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

		