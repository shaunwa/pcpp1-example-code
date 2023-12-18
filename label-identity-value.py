x = 5
y = 'Hello'
my_list_1 = [1, 2, 3]
my_list_2 = [1, 2, 3]

print(id(x))
print(id(y))
print(id(my_list_1))
print(id(my_list_2))

if my_list_1 == my_list_2:
    print('my_list_1 and my_list_2 have the same value!')

if id(my_list_1) == id(my_list_2):
    print('my_list_1 and my_list_2 are really the same list!')