print("Please enter your age(Enter 'quit' to quit): ")
message = ""
while message != 'quit':
	message = input()
	if message == 'quit':
		break
	age = int(message)
	if age < 3:
		print("You are free!")
	elif age < 12:
		print("Your price is 10.")
	else:
		print("Your price is 15.")