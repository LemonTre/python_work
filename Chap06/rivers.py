rivers = {
	'nile': 'egypt',
	'changjiang': 'china',
	'huanghe': 'china',
}

#to have the key and the values
for key, value in rivers.items():
	print("The " + key + " runs through " + value + ".")	
print("\n")

#to have the key
for key in set(rivers.keys()):
	print(key.title())
print("\n")

#to have the value
for value in set(rivers.values()):
	print(value.title())