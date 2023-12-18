class Engine:
    def __init__(self, hp):
        self.hp = hp
    
    def start(self):
        print('Starting the engine...')

class GasolineEngine(Engine):
    def __init__(self, hp, number_of_cylinders):
        super().__init__(hp)
        self.number_of_cylinders = number_of_cylinders

    def start(self):
        super().start()
        print('Vroom!')

class ElectricEngine(Engine):
    def start(self):
        super().start()
        print('...Silence...')

class Wheels:
    def __init__(self, diameter, psi):
        self.diameter = diameter
        self.psi = psi
    
    def inflate(self):
        print('Inflating the tires...')

class Body:
    def __init__(self, color, number_of_doors):
        self.color = color
        self.number_of_doors = number_of_doors
    
    def paint(self, color):
        print(f'Changing the color to {color}...')
        self.color = color

class GasolineCarInheritance(GasolineEngine, Wheels, Body):
    def __init__(self, hp, number_of_cylinders, diameter, psi, color, number_of_doors, make, model):
        GasolineEngine.__init__(self, hp, number_of_cylinders)
        Wheels.__init__(self, diameter, psi)
        Body.__init__(self, color, number_of_doors)
        self.make = make
        self.model = model

    def lock_doors(self):
        print('Locking the doors...')

class ElectricCarInheritance(ElectricEngine, Wheels, Body):
    def __init__(self, hp, diameter, psi, color, number_of_doors, make, model):
        ElectricEngine.__init__(self, hp)
        Wheels.__init__(self, diameter, psi)
        Body.__init__(self, color, number_of_doors)
        self.make = make
        self.model = model

    def lock_doors(self):
        print('Locking the doors...')

class Car:
    def __init__(self, engine, wheels, color, number_of_doors, make, model): 
        self.engine = engine
        self.wheels = Wheels(diameter, psi)
        self.body = Body(color, number_of_doors)
        self.make = make
        self.model = model
    
    def start(self):
        self.engine.start()
        self.lock_doors()

    def lock_doors(self):
        print('Locking the doors...')

my_car = Car(ElectricEngine(100), 15, 35, 'red', 4, 'chevrolet', 'camaro')
my_car.start()
