#СЛОВАРЬ

my_dict = {'a': 1234, 'b': 567 , 'c': 8910}
print(my_dict)

print(my_dict['a'])

my_dict['d'] = 45007
print(my_dict['d'])

my_dict.update({'g': 3456, 'q': 6718})
UD = my_dict.pop('a')
print(UD)

print(my_dict)

#МНОЖЕСТВА
my_set = {1,1,2,3,4.5,'a','a','b','c'}
print(my_set)

my_set.update((7,8,9))
my_set.discard(1)
print(my_set)