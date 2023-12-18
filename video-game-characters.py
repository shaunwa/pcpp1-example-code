class Character:
    def __init__(self, walking_behavior, attack_behavior, talking_behavior):
        self.walking_behavior = walking_behavior
        self.attack_behavior = attack_behavior
        self.talking_behavior = talking_behavior

    def walk(self):
        self.walking_behavior.perform()

    def attack(self):
        self.attack_behavior.perform()

    def talk(self):
        self.talking_behavior.perform()


class Walk:
    def perform(self):
        print('Walking...')

class RideOnHorse:
    def perform(self):
        print('Galloping sounds...')

class RideOnMotorcycle:
    def perform(self):
        print('Vrooooomm!')

class Sword:
    def perform(self):
        print('Character swings a sword!')
    
class BowAndArrow:
    def perform(self):
        print('Character shoots an arrow!')

class Challenge:
    def perform(self):
        print('I challenge you to a duel!')
    
class Growl:
    def perform(self):
        print('Grrrrr!')

char1 = Character(RideOnMotorcycle(), BowAndArrow(), Growl())
char2 = Character(RideOnHorse(), Sword(), Challenge())

char1.attack()
char2.attack()

char1.walking_behavior = Walk()

char1.walk()