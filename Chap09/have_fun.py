from random import randint

class Die():
	"""随机取得掷骰子的数"""
	
	def __init__(self, sides = 6):
		self.sides = sides
	
	def roll_die(self):
		x = randint(1,20)
		print(x)
		
number = Die(20)
flag = 1 
while flag <= 10:
	number.roll_die()
	flag = flag + 1