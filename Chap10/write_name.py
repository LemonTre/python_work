file_path = "G:\python_work\Chap10\learning_python.txt"

with open(file_path, 'w') as file:
	message = input("Enter your name: ")
	file.write(message)