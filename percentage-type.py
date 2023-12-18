class Percentage(float):
    def __mul__(self, other):
        return (self / 100) * other

    def __add__(self, other):
        return Percentage(float(self) + float(other))

    def __str__(self):
        return f'{float(self)}%'

discount_rate = Percentage(80)
extra_discount = Percentage(5)
new_discount_rate = discount_rate + extra_discount
print(new_discount_rate)