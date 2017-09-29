import json

def store_favorite_number():
	number = input("Your favorite number is: ")
	filename = 'G:\python_work\hello.json'
	
	with open(filename, 'w') as file:
		json.dump(number, file)

def get_favorite_number():
	filename = 'G:\python_work\hello.json'
	try:
		with open(filename) as file:
			number = json.load(file)
	except FileNotFoundError:
		return False
	else:
		print("I know your favorite number! It's " + number)
		return True

flag = get_favorite_number()
if flag:
	pass
else:
	print("I dot not have your favorite number!")
	store_favorite_number()
	