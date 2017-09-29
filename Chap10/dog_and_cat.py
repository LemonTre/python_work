file_path_1 = "G:\python_work\Chap10\dog.txt"
file_path_2 = "G:\python_work\Chap10\cat.txt"

def read_file(file_path):
	with open(file_path) as files:
		file = files.read()
		print(file.rstrip())


try:
	read_file(file_path_1)
except FileNotFoundError:
	print("The " + file_path_1 + " is not found!")
	
try:
	read_file(file_path_2)
except FileNotFoundError:
	print("The " + file_path_2 + " is not fountd!")
	