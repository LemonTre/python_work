file_path = 'G:\python_work\Chap10\program.txt'

while True:
	message = input("\nWhy would you like programming('Enter 'q' to quit!'): ")
	if message == 'q':
		break
		
	else:
		with open(file_path, 'a') as file:
			file.write(message + "\n")