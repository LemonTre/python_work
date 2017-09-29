places = {}
flag = True

while flag :
	name = input("Input your name :")
	place = input("If you could visit one place in the world, where would you go? ")
	places[name] = place
	
	get_answer = input("Would you like another one to have the test?(yes/no) ")
	print("\n")
	if get_answer == 'no':
		flag = False
		
print("\nThere are the something about our test: ")
for name, place in places.items():
	print(name + " would like to " + place + ".")
