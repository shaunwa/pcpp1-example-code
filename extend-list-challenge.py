class HistoryList(list):
    def __init__(self, items, *args, **kwargs):
        self.history_items = [f'List was created with items {", ".join([str(x) for x in items])}']
        super().__init__(items, *args, **kwargs)

    def append(self, item):
        self.history_items.append(f'{item} was appended')
        super().append(item)

    def remove(self, item):
        self.history_items.append(f'{item} was removed')
        super().remove(item)
    
    def print_history(self):
        for item in self.history_items:
            print(item)

hl1 = HistoryList([1, 2, 3])
hl1.append(4)
hl1.append(5)
hl1.append(6)
hl1.append(7)
hl1.remove(2)
hl1.remove(4)
hl1.remove(6)
hl1.print_history()