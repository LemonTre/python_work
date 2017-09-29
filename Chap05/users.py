current_users = ['daming', 'xiaoli', 'mary', 'lily', 'xiaoming']

new_users = ['daming', 'xiaoli', 'aili', 'mingming', 'lili']

for user in new_users:
	if user.lower() in current_users:
		print("This name is used, please use another one.")
	else:
		print("This name is not used, you can use this one.")