class InstanceTracker:
    def __init__(self, cls):
        self.instances = []
        self.cls = cls

    def __call__(self, *args, **kwargs):
        new_instance = self.cls(*args, **kwargs)
        self.instances.append(new_instance)
        new_instance.instances = self.instances
        return new_instance

@InstanceTracker
class Person:
    def __init__(self, name):
        self.name = name

    def greet_everyone(self):
        for other in [i for i in self.instances if i.name != self.name]:
            print(f'Hello {other.name}')

p1 = Person('A')
p2 = Person('B')
p3 = Person('C')

p1.greet_everyone()

p4 = Person('D')
p5 = Person('E')

p1.greet_everyone()