def show_magicians(name_list):
	print("\n")
	for magician in name_list:
		print(magician)
		
def make_great(name_list, change_list):
	while name_list:
		magician = "the Great " + name_list.pop()
		change_list.append(magician)
	
	return change_list
		
name_list = ['Daming', 'lili', 'lily']
change_list = []
show_magicians(name_list)
name_list = make_great(name_list, change_list)
show_magicians(name_list)