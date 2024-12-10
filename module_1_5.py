immutable_var = 1, 2, 3, 4, '4', '5', True
print(immutable_var)
print(immutable_var[-1])
print(immutable_var)
print(type(immutable_var))
print(immutable_var[::-1])
print(immutable_var[-1])
print(immutable_var[:-1])
print(type(immutable_var))
# есть возможность работать с разными элементами списка,но нет возможности поменять элементы!
mutable_list = [1, 2, 3, 456, 'pep', '123']
print(mutable_list)
mutable_list[3] = '3'
print(mutable_list)
mutable_list[5] = 123
print(mutable_list)
print(type(mutable_list))
# списки изменяемые, кортежи не изменяемые