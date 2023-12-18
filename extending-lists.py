class MaxSizeList(list):
    def __init__(self, max_size, *args, **kwargs):
        self._max_size = max_size
        super().__init__(*args, **kwargs)
        del self[max_size:]

    def append(self, item):
        if len(self) < self._max_size:
            super().append(item)

my_list = MaxSizeList(5, [1, 2, 3, 4, 5, 6, 7, 8])
my_list.append(100)
print(my_list)

class ListExtended(list):
    def sum(self):
        total = 0
        for x in self:
            total += x
        return total
    
    def mean(self):
        return self.sum() / len(self)

    def append_unique(self, item):
        if item not in self:
            self.append(item)

l1 = ListExtended([1, 2, 3, 4, 5])
l1.append_unique(6)
l1.append_unique(2)

print(l1)
