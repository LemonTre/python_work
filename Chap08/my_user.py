def user_message(first, last, **messages):
	my_messages = {}
	my_messages['first_name'] = first
	my_messages['last_name'] = last
	for key, value in messages.items():
		my_messages[key] = value
		
	return my_messages
	
message_list = user_message('Daming', 'Li',
							location = 'Qingdao',
							univercity = 'Qingda',
							mager = 'CS')
							
print(message_list)