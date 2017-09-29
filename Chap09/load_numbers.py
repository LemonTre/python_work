class User():
	def __init__(self, first_name, last_name, login_attempts, *list):
		self.first_name = first_name
		self.last_name = last_name
		self.list = list
		self.login_attempts = login_attempts
		
	def describe_user(self):
		print("\nUser's name is: " + self.first_name.title() + " " 
		+ self.last_name.title() + ".")
		for user in self.list:
			print("Something about you : " + user + ".")
			
	def greet_user(self):
		print("Hello, " + self.first_name.title() + " "
		+ self.last_name.title() + ".")
		
	def increment_login_attempts(self):
		"""将属性login_attempt的值加1"""
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		"""将属性login_attempt的值进行重置"""
		self.login_attempts = 0 
		
user = User('Lily', 'Chen', 23, 'Qingdao')
full_name = user.first_name + " " + user.last_name
user.increment_login_attempts()
user.increment_login_attempts()

print("The " + full_name.title() + "'s times of login are: " 
	+ str(user.login_attempts) + ".")
	
user.reset_login_attempts()
print("The " + full_name.title() + "'s times of login are: " 
	+ str(user.login_attempts) + ".")