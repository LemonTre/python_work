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
		
class Admin(User):
	def __init__(self, first_name, last_name, *list):
		super().__init__(first_name, last_name, *list)
		self.privileges = []
		
	def show_privileges(self):
		"""打印管理员中的属性列表"""
		for privilege in self.privileges:
			print("The privilege is: " + privilege)
			

admin = Admin('Lily', 'Chen', '29', 'Qingdao')
admin.privileges = ['can add post', 'can delete post', 'can ban user']
admin.show_privileges()