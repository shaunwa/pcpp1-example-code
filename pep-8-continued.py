# Do NOT put extra spaces inside the parentheses:
def add( x, y, z ): # NO
    return x + y + z

result = add( 1, 2, 3 ) # NO

def subtract(x, y, z): # YES
    return x + y + z

result_2 = subtract(1, 2, 3) # YES

# Also DO NOT use extra spaces with lists, tuples, dictionaries, etc.
numbers = [ 1, 2, 3 ] # NO
numbers[ 0 ] # NO
coords = ( 1, 2, 3 ) # NO
small_tuple = (1, ) # NO
person = { 'first_name': 'Shaun', 'last_name': 'Wassell' } # NO

numbers = [1, 2, 3] # YES
numbers[0] # YES
coords = (1, 2, 3) # YES
small_tuple = (1,) # YES
person = {'first_name': 'Shaun', 'last_name': 'Wassell'} # YES

# No spaces around colons with functions, if statements, etc.
def my_function() : # NO
    return 'This is wrong'

if True : # NO
    print('Do not put a space between the condition and the colon!')

for x in range(10) : # NO
    print('No spaces!')

# Colons with ranges
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_numbers[1:5]) # YES
print(my_numbers[1:8:2]) # YES

start = 1
end = 5
offset = 2

my_numbers[start + offset : end + offset] # YES
my_numbers[start + offset:end + offset] # NO

# Here, we take a look at variable assignment alignment and why you
# should avoid it

# NO for this:
x          = 5
message    = 'Hello!'
is_running = True

# YES for this:
x = 5
message = 'Hello!'
is_running = True

a = 10
b = 20
hypotenuse = a*a + b*b # YES
something_else = (a+a) * (b+b) # YES
y = 2*a + b # YES
