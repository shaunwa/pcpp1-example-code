from abc import ABC, abstractmethod

class Animal(ABC):
    def feed(self):
        print('Nom nom nom')

    @abstractmethod
    def make_sound(self):
        pass

    @classmethod
    @abstractmethod
    def describe(cls):
        pass

    @staticmethod
    @abstractmethod
    def eat(a1, a2):
        pass

class Mammal(Animal):
    @abstractmethod
    def regulate_body_temp(self):
        pass

class Fish(Animal):
    @abstractmethod
    def defend(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Bark bark!')

    def regulate_body_temp(self):
        print('The dog grows fur and shivers')

    @classmethod
    def describe(cls):
        print(f'This is the {cls.__name__} class')

    @staticmethod
    def eat(a1, a2):
        print(f'The {a1.__class__} eats the {a2.__class__}')

class Cat(Animal):
    def make_sound(self):
        print('Meow')

    @classmethod
    def describe(cls):
        print(f'This is the {cls.__name__} class')

    @staticmethod
    def eat(a1, a2):
        print(f'The {a1.__class__} eats the {a2.__class__}')

class Elephant(Animal):
    def make_sound(self):
        print('Trrrrrumpet')

    @classmethod
    def describe(cls):
        print(f'This is the {cls.__name__} class')

    @staticmethod
    def eat(a1, a2):
        print(f'The {a1.__class__} eats the {a2.__class__}')

dog = Dog()
# dog.make_sound()
cat = Cat()
# cat.make_sound()
# elephant = Elephant()
# elephant.make_sound()

Dog.eat(dog, cat)