sandwitch_orders = ['meat', 'partition', 'fruit', 'partition', 'vegetable', 'partition']

print("The partition is solded out!")

while 'partition' in sandwitch_orders:
	sandwitch_orders.remove('partition')
	
print("\nThe new orders are here:")
print(sandwitch_orders)