def class_restrictions(cls):
    return NoMultipleInheritance(cls.__name__, cls.__bases__, dict(cls.__dict__))

class MultipleInheritanceException(Exception):
    pass

class NoMultipleInheritance(type):
    def __new__(metacls, name, bases, attrs):
        if len(bases) > 1:
            raise MultipleInheritanceException('Classes may only inherit from 1 superclass!')
        return super().__new__(metacls, name, bases, attrs)

class Base1:
    pass

class Base2:
    pass

@class_restrictions
class MyClass(Base1):
    pass

def count_instances(cls):
    return InstanceCountingMetaclass(cls.__name__, cls.__bases__, dict(cls.__dict__))

class InstanceCountingMetaclass(type):
    number_of_classes = 0

    def __init__(cls, name, bases, attrs):
        cls.__class__.number_of_classes += 1
        super().__init__(name, bases, attrs)

# def create_instance_counting_metaclass():
#     number_of_classes = 0

#     class Metaclass(type):
#         def __init__(cls, name, bases, attrs):
#             nonlocal number_of_classes
#             number_of_classes += 1
#             super().__init__(name, bases, attrs)

#         def get_number_of_classes():
#             return number_of_classes
        
#     return Metaclass

# InstanceCountingMetaclass = create_instance_counting_metaclass()

@count_instances
class MyClass1:
    pass

@count_instances
class MyClass2:
    pass

@count_instances
class MyClass3:
    pass

print(InstanceCountingMetaclass.number_of_classes)