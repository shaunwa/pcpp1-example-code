# 4 spaces of indentation is the norm
def my_function():
    return 'Hello!'

# 4 spaces extra for indented args
def my_function(
        arg_1='A',
        arg_2='B',
        arg_3='C'):
    return 'Hello!'


# Option 1 for calling functions: line up newlines with first arg
my_function('Apple', 'Banana',
            'Canteloupe')

# Option 2 for calling functions: start a new line immediately
my_function(
    'Apple', 'Banana',
    'Canteloupe')

# Incorrect:
my_function('Apple', 'Banana',
    'Canteloupe')

# If statements with multi-line conditions
if (5 > 10 or
    8 > 20 or
    -1 < -5):
    # Uh oh, better tell the user
    print('Math no longer works!')

if (5 > 10
        or 8 > 20
        or -1 < -5):
    print('Math no longer works!')

# Lining up brackets and parentheses
my_list = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
]

my_list_2 = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
    ]

result = my_function(
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
)

result_2 = my_function(
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    )

# Splitting lines

# Function arguments
result_3 = my_function(
    'apple', 'banana', 'canteloupe',
    'date', 'eggplant', 'fig')

# Doing math
answer = 1 + 2 + 3 + 4 \
    + 5 + 6 + 7 + 8 \
    + 9 + 10 + 11 + 12 \
    + 13 + 14 + 15 + 16 \
    + 17 + 18

# Breaking up long strings
long_string = "Deep in the jungle, surrounded by wild animals and" \
    "mysterious sounds, our hero finds an ancient door..." \
    "Would you like to open the door?"

another_long_string = """
Deep in the jungle, surrounded by wild animals and
mysterious sounds, our hero finds an ancient door...
Would you like to open the door?
"""

one_more_long_string = ("Deep in the jungle, surrounded by wild animals and"
    "mysterious sounds, our hero finds an ancient door..."
    "Would you like to open the door?")

# Separate function and class definitions with two lines on either side


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


class MyClass:
    pass

# Methods inside of classes are separated by 1 line on either side

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello():
        print(f'Hello my name is {self.name}')

    def say_goodbye():
        print('Goodbye')

# Separate function bodies into logical sections using single empty lines

def get_average(*args):
    total = 0
    for arg in args:
        total += arg

    average = total / len(args)

    return average