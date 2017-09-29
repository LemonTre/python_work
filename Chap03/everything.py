favorite_things = ['river', 'mountain', 'Chain', 'Qingzhou']
print(favorite_things)

#revise the data
favorite_things[0] = 'ChangJiang'
print(favorite_things)

#add a data
favorite_things.append('DaLian')
print(favorite_things)
favorite_things.insert(0, 'HuangHe')
print(favorite_things)

#delete a data
del favorite_things[0]
print(favorite_things)
favorite_things.pop(2)
print(favorite_things)

#sort the list
favorite_things.sort()
print(favorite_things)

favorite_things.sort(reverse = True)
print(favorite_things)

change_list = sorted(favorite_things)
print(change_list)
print(favorite_things)

change_list = sorted(favorite_things, reverse = True)
print(change_list)
print(favorite_things)

#reverse the data by using time
favorite_things.reverse()
print(favorite_things)

#the length of the list
length = len(favorite_things)
print(length)