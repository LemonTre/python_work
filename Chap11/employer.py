class Employee():
	def __init__(self, first_name, last_name, money):
		self.first_name = first_name
		self.last_name = last_name
		self.money = money
		
	def give_raise(self, add = 50):
		self.money += add
		return self.money
		
		
#employee = Employee('Lili', 'Da', 22)
#print(employee.money)
#print(employee.give_raise())