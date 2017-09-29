my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('dog')
friend_foods.append('cat')

print("My favorite pizzas are: ")
for food in my_foods:
	print(food)
	
print("My friend is favorite pizzas are: ")
for food in friend_foods:
	print(food)

