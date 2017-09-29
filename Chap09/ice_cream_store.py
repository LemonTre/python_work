class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("The name of restaurant is: " + self.restaurant_name.title() + ".")
		print("The type of restaurant is " + self.cuisine_type + ".")
		
	def open_restaurant(self):
		print("The restaurant is working.")
		
		
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []
	
	def show_ice_creams(self):
		for ice_cream in self.flavors:
			print("The ice cream are: " + ice_cream)
			

IceCreamStand = IceCreamStand('KFC', 'fast food')
IceCreamStand.flavors = ['Apple Ice_cream', 'Banana Ice_cream', 'Orange Ice_cream']
IceCreamStand.show_ice_creams()
	