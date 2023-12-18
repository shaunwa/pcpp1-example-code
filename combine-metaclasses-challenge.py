class InstanceCounting(type):
    number_of_classes = 0

    def __init__(cls, name, bases, attrs):
        cls.__class__.number_of_classes += 1
        super().__init__(name, bases, attrs)

class MultipleInheritanceException(Exception):
    pass

class NoMultipleInheritance(type):
    def __new__(metacls, name, bases, attrs):
        if len(bases) > 1:
            raise MultipleInheritanceException('Classes may only inherit from 1 superclass!')
        return super().__new__(metacls, name, bases, attrs)

class CombinedMeta(InstanceCounting, NoMultipleInheritance):
    pass

class A(metaclass=CombinedMeta):
    pass

class B(metaclass=CombinedMeta):
    pass

class C(metaclass=CombinedMeta):
    pass

print(CombinedMeta.number_of_classes)

class D(A, B):
    pass