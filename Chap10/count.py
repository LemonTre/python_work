file_path = "G:\python_work\count.txt"

result = 0 
with open(file_path) as files:
	for file in files:
		len = int(file.lower().count('the'))
		result += int(len)
		
print(result)

