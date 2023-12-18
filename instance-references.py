def instance_references(cls):
    instances = []

    def wrapper(*args, **kwargs):
        new_instance = cls(*args, **kwargs)
        instances.append(new_instance)
        new_instance.all_instances = instances
        return new_instance

    return wrapper

@instance_references
class VideoGameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def print_other_instances(self):
        for instance in [i for i in self.all_instances if i is not self]:
            print(instance)

    def __str__(self):
        return f'video game object at ({self.x}, {self.y})'

o1 = VideoGameObject(0, 1)
o2 = VideoGameObject(2, 3)
o3 = VideoGameObject(3, 8)

o1.print_other_instances()
o2.print_other_instances()