class User():
	def __init__(self, first_name, last_name, *list):
		self.first_name = first_name
		self.last_name = last_name
		self.list = list
		
	def describe_user(self):
		print("\nUser's name is: " + self.first_name.title() + " " 
		+ self.last_name.title() + ".")
		for user in self.list:
			print("Something about you : " + user + ".")
			
	def greet_user(self):
		print("Hello, " + self.first_name.title() + " "
		+ self.last_name.title() + ".")