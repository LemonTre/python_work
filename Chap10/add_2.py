print("Please enter two numbers, and we will add them.")
print("Enter 'q' to quit!")
while True:
	try:
		msg_1 = input("First number: ")
		if msg_1 == 'q':
			break
		else:
			value_1 = int(msg_1)
	
		msg_2 = input("Last number ")
		if msg_2 == 'q':
			break
		else:
			value_2 = int(msg_2)
			
	except ValueError:
		pass
	
	else:
		answer = value_1 + value_2
		print(answer)
	