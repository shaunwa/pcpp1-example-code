class StringTuple(tuple):
    def __new__(cls, *args):
        transformed_items = (str(x) for x in args)
        new_instance = super().__new__(cls, transformed_items)
        return new_instance

class TupleExtended(tuple):
    def __new__(cls, *args):
        return super().__new__(cls, args)

    def first(self):
        return self[0]

    def last(self):
        return self[len(self) - 1]

te1 = TupleExtended(1, 2, 3, 4, 5)
print(te1.first())
print(te1.last())

st1 = StringTuple(1, 'Hello', True, { 'a': 1, 'b': 2 })
print(st1)

class ReversedTuple(tuple):
    def __new__(cls, *args):
        new_instance = super().__new__(cls, reversed(args))
        return new_instance

rt1 = ReversedTuple(1, 2, 3)
print(rt1)
