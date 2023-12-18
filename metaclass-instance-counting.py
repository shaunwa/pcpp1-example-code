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

class MyClass1(metaclass=InstanceCountingMetaclass):
    pass

class MyClass2(metaclass=InstanceCountingMetaclass):
    pass

InstanceCountingMetaclass.number_of_classes = 100

class MyClass3(metaclass=InstanceCountingMetaclass):
    pass

print(InstanceCountingMetaclass.number_of_classes)