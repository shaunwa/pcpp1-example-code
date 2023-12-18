class OddInt(int):
    def __new__(cls, value):
        print('Inside new!')
        if value % 2 == 0:
            adjusted_value = value + 1
        else:
            adjusted_value = value

        new_instance = super().__new__(cls, adjusted_value)
        return new_instance

    def __init__(self, value):
        print('Inside init!')

x = OddInt(6)
y = OddInt(13)

print(x)
print(y)

class RoundedFloat(float):
    def __new__(cls, value, num_decimal_places):
        adjusted_value = round(value, num_decimal_places)
        return super().__new__(cls, adjusted_value)

z = RoundedFloat(3.14159, 10)
print(z)