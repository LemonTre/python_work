class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("The name of restaurant is: " + self.restaurant_name.title() + ".")
		print("The type of restaurant is " + self.cuisine_type + ".")
		
	def open_restaurant(self):
		print("The restaurant is working.")
		
	def set_number_served(self, numbers):
		"""修改吃饭的人数"""
		self.number_served = numbers
		
	def increment_number_served(self, increments):
		"""增加的人数值"""
		self.number_served += increments
		
restaurant = Restaurant('KFC', 'fast food')

print("The numbers in this restaurant are: " 
	+ str(restaurant.number_served) + " guys.")
	
restaurant.number_served = 12
print("The numbers in this restaurant are: " 
	+ str(restaurant.number_served) + " guys.")

restaurant.set_number_served(15)
print("The numbers in this restaurant are: " 
	+ str(restaurant.number_served) + " guys.")
	
restaurant.increment_number_served(100)
print("The numbers that you think the restaurant can hold: " 
	+ str(restaurant.number_served) + " guys.")

