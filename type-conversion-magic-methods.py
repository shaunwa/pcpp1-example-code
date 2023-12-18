class USD:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        return f'${format(self.__float__(), ".2f")}'

    def __repr__(self):
        return f'USD({self.dollars}, {self.cents})'

    def __format__(self, format_spec):
        if format_spec == 'regular':
            return self.__str__()
        elif format_spec == 'long':
            return f'{self.dollars} dollars and {self.cents} cents'
        else:
            return NotImplemented

    def __float__(self):
        return self.dollars + (self.cents / 100.0)

    def __int__(self):
        return self.dollars * 100 + self.cents

    def __bool__(self):
        return bool(self.dollars) or bool(self.cents)

amount1 = USD(0, 0)
amount2 = USD(2, 99)

print(amount1)
