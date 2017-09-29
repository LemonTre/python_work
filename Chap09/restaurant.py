class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("The name of restaurant is: " + self.restaurant_name.title() + ".")
		print("The type of restaurant is " + self.cuisine_type + ".")
		
	def open_restaurant(self):
		print("The restaurant is working.")
		
restaurant = Restaurant('Quanjude','Jingwei')

print("Name is: " + restaurant.restaurant_name.title())
print("Type is: " + restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()