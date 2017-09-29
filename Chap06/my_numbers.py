favorite_numbers_0 = {
	'jane' : [4, 3],
	'li' : [2, 3],
	'daming' : [5, 9],
	'xiaoli' : [10, 12],
	'lily' : [1,8],
	}
	
for name , numbers in favorite_numbers_0.items():
	print(name.title() + "'s favorite numbers: ")
	for number in numbers:
		print("\t" + str(number))