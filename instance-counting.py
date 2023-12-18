def count_instances(cls):
    number_of_instances = 0

    class Wrapper(cls):
        def __init__(self, *args, **kwargs):
            nonlocal number_of_instances
            super().__init__(*args, **kwargs)
            number_of_instances += 1
            print(f'There are now {number_of_instances} instances of {cls.__name__}')
    
    return Wrapper

@count_instances
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

@count_instances
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

e1 = Enemy(1, 2)
e2 = Enemy(0, 5)
e3 = Enemy(3, 8)

p1 = Player(1, 2)
p2 = Player(0, 5)
p3 = Player(3, 8)