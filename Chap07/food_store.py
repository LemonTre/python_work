sandwitch_orders = ['meat', 'fruit', 'vegetable']
finished_sandwitched = []

while sandwitch_orders:
	sandwitch = sandwitch_orders.pop()
	print("I made your " + sandwitch + " sandwitch.")
	finished_sandwitched.append(sandwitch)
	
print("\nThere are the sandwitches that you would like to have: ")
for sandwitch in finished_sandwitched:
	print(sandwitch)