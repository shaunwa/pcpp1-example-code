import random

class MyIterable:
    def __init__(self, ls):
        self._list = ls

    def __iter__(self):
        print('__iter__ has been called!')
        return RandomOrderIterator(self._list)

    # def __contains__(self, value):
    #     return value in self._list

    def __reversed__(self):
        return MyIterable(list(reversed(self._list)))

class AscendingOrderIterator:
    def __init__(self, ls):
        self._list = sorted(ls)
        self._current_index = 0

    def __next__(self):
        if self._current_index >= len(self._list):
            raise StopIteration

        current_element = self._list[self._current_index]
        self._current_index += 1
        return current_element

class RandomOrderIterator:
    def __init__(self, ls):
        self._list = random.sample(ls, len(ls))
        self._current_index = 0

    def __next__(self):
        if self._current_index >= len(self._list):
            raise StopIteration

        current_element = self._list[self._current_index]
        self._current_index += 1
        return current_element
    
class NormalOrderIterator:
    def __init__(self, ls):
        self._list = ls
        self._current_index = 0

    def __next__(self):
        if self._current_index >= len(self._list):
            raise StopIteration

        current_element = self._list[self._current_index]
        self._current_index += 1
        return current_element


mi1 = MyIterable([100, 3, 98, -2, 64])

# 1. For loops
for x in mi1:
    print(x)

# 2. Unpacking Operator
mi1_extended = [100, *mi1, 6]
print(mi1_extended)

def multiply(*args):
    product = 1
    for x in args:
        print(f'Multiplying {x}')
        product *= x
    return product

multiply(*mi1)

# 3. Sequence Unpacking

a, b, c, d, e = mi1

print(f'a is {a}, b is {b}, c is {c}, d is {d}, e is {e}')

# 4. list and tuple constructors

mi1_as_list = list(mi1)
mi1_as_tuple = tuple(mi1)

print(mi1_as_list)
print(mi1_as_tuple)

# 5. Comprehension

doubled_mi1 = [x * 2 for x in mi1]
negative_mi1 = [x for x in mi1 if x < 0]

print(doubled_mi1)
print(negative_mi1)

# 6. Built-in Functions

total = sum(mi1)
print(f'The sum of all the values in mi1 is {total}')

# 7. The 'in' operator, but only when we have no __contains__ magic method

print(f'-2 is in mi1: {-2 in mi1}')