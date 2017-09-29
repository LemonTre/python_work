from collections import OrderedDict

order_number = OrderedDict()

order_number['append'] = 'add the data'
order_number['insert'] = 'insert the data'
order_number['del'] = 'delete the data'
order_number['pop'] = 'delete the data, and you can use the data'
order_number['upper'] = 'the function that you can make the all data big'

for key, value in order_number.items():
	print(key + ": " + value + ".")