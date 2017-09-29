print("Please enter your age(Enter 'quit' to quit): ")
message = ""
active = True
while active :
	message = input()
	if message == 'quit':
		active = False
		break
	age = int(message)
	if age < 3:
		print("You are free!")
	elif age < 12:
		print("Your price is 10.")
	else:
		print("Your price is 15.")