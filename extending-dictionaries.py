class UppercaseKeyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dict_items = list(self.items())
        for key, value in dict_items:
            self[key] = value
            if key.upper() != key:
                del self[key]

    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)

d1 = UppercaseKeyDict({ 'name': "shaun", 'a': 1, 'b': 2, 'c': 3 })
print(d1)

d1['d'] = 4
print(d1)