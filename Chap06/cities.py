cities = {
	'beijing': {
		'country': 'china',
		'population': 2000,
		'fact': 'it is a beautiful city',
	},
	
	'qingdao':{
		'country': 'china',
		'population': 30213,
		'fact': 'this is a big city.',
	},
	
	'qingdao':{
		'country': 'china',
		'population': 98347,
		'fact': 'this is my favorite city',
	}
}

for city_name, city_information in cities.items():
	print("Message about " + city_name.title() + ": ")
	print("\tCountry: " + city_information['country'].title())
	print("\tPopulation: " + str(city_information['population']))
	print("\tFact: " + city_information['fact'])
	
	
