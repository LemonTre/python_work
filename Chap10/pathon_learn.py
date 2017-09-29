file_path = 'G:\python_work\Chap10\learning_python.txt'

with open(file_path) as file_object:
	file_1 = file_object.read()
	print(file_1)
	
print("\n")

with open(file_path) as file_object:
	for file in file_object:
		print(file.rstrip())
		
print("\n")

with open(file_path) as file_object:
	file_list = file_object.readlines()
	
for file in file_list:
	print(file.rstrip())
