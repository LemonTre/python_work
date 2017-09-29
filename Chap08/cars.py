def car_show(maker, type, **car_message):
	car_list = {}
	car_list['maker_name'] = maker
	car_list['car_type'] = type
	for key, value in car_message.items():
		car_list[key] = value

	return car_list
	
car = car_show('subaru', 'outback',
				color = 'blue',
				tow_package = True,
				)
				
print(car)