class NonEmptyString(str):
    def __new__(cls, value):
        if len(value) == 0:
            raise TypeError('You cannot create a non-empty string with an empty string!')

        return super().__new__(cls, value)

class NonZeroInt(int):
    def __new__(cls, value):
        if value == 0:
            raise TypeError('Do not try to create an instance of NonZeroInt with the value zero!')

        return super().__new__(cls, value)

x = NonZeroInt(10)
print(x)