def city_country(name, nation):
	my_country = {'city_name': name, 'city_nation': nation}
	return my_country
	
my_country = city_country('santiage', 'chile')
print(my_country['city_name'].title() + ", " + my_country['city_nation'].title() + "." )
