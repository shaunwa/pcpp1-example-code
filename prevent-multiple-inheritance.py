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

class MyClass(Base1, Base2, metaclass=NoMultipleInheritance):
    pass