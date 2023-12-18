class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise Exception('The amount of a deposit must be greater than 0')
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            raise Exception('Error withdrawing funds!')
    
    def print_balance(self):
        print(f'The account currently has {self.__balance} dollars')

class ExtraSpecialAccount(BankAccount):
    def tell_me_about_the_perks(self):
        print('Blah blah blah')

my_account = BankAccount()
my_account.deposit(5) # Needs to be positive!
my_account.withdraw(3) # Needs to be less than or equal to the balance
my_account.print_balance()

my_account.__balance = 1000000
my_account.print_balance()