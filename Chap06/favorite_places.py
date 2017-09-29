favorite_places = {
	'Daming': ['Beijng', 'Shanghai', 'guangzhou'],
	'Lily': ['qingdao', 'dalian'],
	'Jessica': ['Beijng']
}

for name, places in favorite_places.items():
	print(name.title() + "'s favorite places: ")
	
	for place in places:
		print("\t" + place.title())
		
