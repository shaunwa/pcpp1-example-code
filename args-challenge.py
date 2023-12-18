def test_immutable(x):
    x = -99

def test_mutable(y):
    y[0] = -99
    # y = [100, 200, 300]

# id(x)

pi = 3.14159
numbers = [1, 2, 3]

test_mutable(numbers)
print(numbers)