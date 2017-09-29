my_guest = ['Zhou Enlai', 'Linda', 'Jessica']
my_guest.insert(0, 'Lucy')
my_guest.insert(3, 'XiaoLi')
my_guest.append('XiaoHong')

print("I am sorry, the big table can not came in time.")

left_guy = my_guest.pop()
print(left_guy + ", I am sorry , I can not eat with you.")
left_guy = my_guest.pop()
print(left_guy + ", I am sorry, I can not eat with you.")
left_guy = my_guest.pop()
print(left_guy + ", I am sorry, I can not eat with you.")
left_guy = my_guest.pop()
print(left_guy + ", I am sorry, I can not eat with you.")

first_guest = my_guest[0]
print(first_guest + ", I can eat with you.")
second_guest = my_guest[1]
print(second_guest + ", I can eat with you.")
del my_guest[1]
del my_guest[0]
print(my_guest)
