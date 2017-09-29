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
		
user_1 = User('July', 'Li', '13')
user_2 = User('Lee', 'Chen', 'Qingdao')
user_3 = User('Lili', 'Chen', '18', 'Huanghe')

user_1.describe_user()
user_1.greet_user()

print("\n")

user_2.describe_user()
user_2.greet_user()

print("\n")

user_3.describe_user()
user_3.greet_user()