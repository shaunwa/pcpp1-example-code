def instance_count(cls):
    cls.__number_of_instances = 0

    cls_init = cls.__init__

    def __new_init__(self, *args, **kwargs):
        cls.__number_of_instances += 1
        cls_init(self, *args, **kwargs)
    
    @classmethod
    def get_instance_count(cls):
        return cls.__number_of_instances

    cls.__init__ = __new_init__
    cls.get_instance_count = get_instance_count
    return cls

@instance_count
class Person:
    def __init__(self, name, age, hair_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
    
    @classmethod
    def create_from_string(cls, str): 
        name, age_raw, hair_color = str.split(', ')
        age = int(age_raw)
        new_instance = cls(name, age, hair_color)
        return new_instance
    
    def greet(self):
        print(f'Hello, my name is {self.name}')

    @classmethod
    def my_first_class_method(cls):
        print(f'Hello from the {cls.__name__} class! Here is a description of this class: {cls.description}')
        cls.description = 'I have already told you about the class, weren\'t you listening'

    @staticmethod
    def has_longer_name(person1, person2):
        return len(person1.name) > len(person2.name)

    def has_longer_name(self, other):
        return len(self.name) > len(other.name)

person1 = Person.create_from_string('Shaun, 123, brown')
print(person1.name)
print(person1.age)
print(person1.hair_color)