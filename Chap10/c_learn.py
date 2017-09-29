file_path = 'G:\python_work\Chap10\learning_python.txt'

with open(file_path) as files:
	file_list = files.readlines()
	for file in file_list:
		print(file.replace('python', 'C').rstrip())
	
	


	