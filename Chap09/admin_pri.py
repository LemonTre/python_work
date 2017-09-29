from user import User

class Privileges():
	def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
		self.privileges = privileges
		
	def show_privileges(self):
		"""打印管理员中的属性列表"""
		for privilege in self.privileges:
			print("The privilege is: " + privilege)
		
class Admin(User):
	def __init__(self, first_name, last_name, *list):
		super().__init__(first_name, last_name, *list)
		self.my_privileges = Privileges()