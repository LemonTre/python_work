

def get_city_function(city_name, country_name, population = ''):
	
	if population:
		full_name = city_name + ", " + country_name + " - population " + population
	else:
		full_name = city_name + ", " + country_name
	
	return full_name.title()
	

def get_message():
	print("Enter 'q' to quit!")
	while True:
		city_name = input("\nEnter a name of city: ")
		if city_name == 'q':
			break
		country_name = input("Enter a name of country: ")
		if country_name == 'q':
			break
		population = input("Enter the population: ")
		if population == 'q':
			break
		full_name = get_city_function(city_name, country_name, population)
		print("Full name is :" + full_name)
		
#get_message()