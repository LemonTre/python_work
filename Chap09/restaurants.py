class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("\nThe name of restaurant is: " + self.restaurant_name.title() + ".")
		print("The type of restaurant is: " + self.cuisine_type + ".")
		
	def open_restaurant(self):
		print("The restaurant is working.")
		

"""
restaurant_1 = Restaurant('Chuancheng', 'chuanwei')
restaurant_2 = Restaurant('KFC', 'fast food')
restaurant_3 = Restaurant('Modolao', 'delicious')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
"""