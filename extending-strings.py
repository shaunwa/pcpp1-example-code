class UppercaseString(str):
    def __new__(cls, value):
        new_instance = super().__new__(cls, value.upper())
        return new_instance

x = UppercaseString('abcdefg')

print(x)
print(isinstance(x, UppercaseString))