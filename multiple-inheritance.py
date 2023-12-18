class Employee:
    def __init__(self, employee_id, name):
        print('Inside Employee __init__')
        self.employee_id = employee_id
        self.name = name

    def get_paid(self):
        print('Yay, it\'s pay day!')

    def print_details(self):
        print('Here are my employee details...')

class Customer:
    def __init__(self, customer_id, username):
        print('Inside Customer __init__')
        self.customer_id = customer_id
        self.username = username

    def spend_money(self):
        print('I really like this thing, I\'m going to buy it')

    def print_details(self):
        print('Here are my customer details...')

class EmployeeCustomer(Customer, Employee):
    # def __init__(self, employee_id, name, customer_id, username, hair_color):
    #     Employee.__init__(self, employee_id, name)
    #     Customer.__init__(self, customer_id, username)
    #     self.hair_color = hair_color

    def get_paid(self):
        super().get_paid()
        super().spend_money()

    def print_details(self):
        # Employee.print_details(self)
        # Customer.print_details(self)
        print(f'My name is: {self.name}, and my employee id is: {self.employee_id}')
        print(f'My username is: {self.username}, and my customer id is: {self.customer_id}')
        print(f'And finally, my hair color is {self.hair_color}')

# employee = Employee()
# customer = Customer()
ec = EmployeeCustomer('123', 'Shaun', 'abc', 'shaunwa', 'brown')

ec.print_details()
# ec.spend_money()