import unittest
from employer import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.my_employee = Employee('Daming', 'Chen', 100)
		self.add = 30
	
	def test_give_default_raise(self):
		self.my_employee.give_raise()
		print("Money is " + str(self.my_employee.money) + ".")
	
	def test_give_custom_raise(self):
		self.my_employee.give_raise(self.add)
		print("My money is " + str(self.my_employee.money) + ".")
		
unittest.main()