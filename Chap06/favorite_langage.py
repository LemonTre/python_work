favorite_langage = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'rudy',
	'phil': 'python',
}

names = ['phil', 'daming', 'sarah', 'lily']

for name in names:
	if name in favorite_langage.keys():
		print(name.title() + ", thank you for coming!")
	else:
		print(name.title() + ", please take our poll!") 