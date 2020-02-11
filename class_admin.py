from user4 import User

class Admin(User):
	"""docstring for admin"""
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)

		self.privileges = ls
	

	def show_privieges(self):
		print(self.first_name.title()
			+self.last_name.title()
			+"拥有的权限是:", end=" ")
		ls =['can add post','can delete post','can ban user']

        for i in ls:
			print(i, end = ',')
	
my_admin = Admin('zhou','hui')
my_admin.show_privieges()
my_admin.full_name
