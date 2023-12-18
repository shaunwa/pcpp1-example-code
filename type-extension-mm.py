class VerboseInt(int):
    def __add__(self, other):
        print(f'I am being added to {other}')
        return super().__add__(other)

    def __sub__(self, other):
        print(f'Help! They are subtracting {other} from me!')
        return super().__sub__(other)

class DeepEqualDict(dict):
    def __eq__(self, other):
        if self.keys() != other.keys():
            return False

        for key in self:
            if self[key] != other[key]:
                return False

        return True

d1 = DeepEqualDict({ 'a': 1, 'b': 2, 'c': 3 })
d2 = DeepEqualDict({ 'a': 3, 'b': 2, 'c': 3 })

print(d1 == d2)