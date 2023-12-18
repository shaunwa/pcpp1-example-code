class Meta1(type):
    def __init__(cls, name, bases, attrs):
        print(f'{name} has Meta1 as its metaclass')
        super().__init__(name, bases, attrs)

class Meta2(type):
    def __init__(cls, name, bases, attrs):
        print(f'{name} has Meta2 as its metaclass')
        super().__init__(name, bases, attrs)

class Meta3(Meta1, Meta2):
    def __init__(cls, name, bases, attrs):
        print(f'{name} really has Meta3 as its metaclass, but here are the other inits:')
        Meta1.__init__(cls, name, bases, attrs)
        Meta2.__init__(cls, name, bases, attrs)

class A(metaclass=Meta1):
    pass

class B(A):
    pass

class X(metaclass=Meta2):
    pass

class Y(X):
    pass

class C(metaclass=Meta3):
    pass