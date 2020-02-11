class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name,cuisine_type):
		super(Restaurant, self).__init__()
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name.title()+' is a very good restaurant.')

	def open_restaurant(self):
		print(self.restaurant_name.title()+' is opend')

	def serverd(self,num):
		self.num = num
		print(str(self.num) + ' man are serverd.' )

my_r =Restaurant('wenxinjia','small')
print (my_r.restaurant_name.title() + ' is '+my_r.cuisine_type)
my_r.open_restaurant()
my_r.describe_restaurant()
my_r.serverd(90)
		