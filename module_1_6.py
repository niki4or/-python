my_dict = {'Роман': 3}
print(my_dict)
my_dict.update({'Милена': 7, 'Никита': 7})
print(my_dict)
my_dict['Дима'] = 4
print(my_dict)
print(my_dict.get('Никита'))
print(my_dict.get('Сергей'))
a = my_dict.pop('Никита')
print(my_dict)
print(a)
my_set = {12, 13, 14, 'Роман', 'Милена', 12, 14, 'Милена'}
print(my_set)
my_set.add(20)
my_set.add(40)
print(my_set)
my_set.remove(13)
print(my_set)
