name_lists = ['admin', 'daming', 'xiaoli', 'linda', 'lili']

for name in name_lists:
	if name == 'admin':
		print("Helle admin, would you like to see a status report?")
	else:
		print("Hello " + name + ", thank you for logging in again.")
		
name_lists = []

if name_lists:
	print("Ok")
else:
	print("We need to find some users.")