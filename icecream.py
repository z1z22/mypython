class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name,cuisine_type):

		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name.title()+' is a very good restaurant.')

	def open_restaurant(self):
		print(self.restaurant_name.title()+' is opend')

	def serverd(self,num):
		self.num = num
		print(str(self.num) + ' man are serverd.' )

class IceCreamstand(Restaurant):
	'''建立有的冰激凌小店的餐馆'''
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = ['草莓','巧克力','香草','芒果','榴莲']


my_ic = IceCreamstand("美食家",'冰激凌')
print(my_ic.restaurant_name+'店里卖'+my_ic.cuisine_type)
print('口味有:')
for i in my_ic.flavors:
	print(i,end=',')
my_ic.open_restaurant()

