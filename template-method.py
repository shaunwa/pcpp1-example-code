from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def notify(self, data):
        pass

class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def update(self, data):
        for o in self.observers:
            o.notify(data)

class Chatbot(ConcreteSubject):
    def handle_conversation(self):
        self.introduction()
        self.ask_for_user_id()
        self.ask_for_further_details()
        self.say_goodbye()

    def introduction(self):
        print('Hello, I can help you with whatever you need')

    @abstractmethod
    def ask_for_user_id(self):
        pass

    @abstractmethod
    def ask_for_further_details(self):
        pass

    @abstractmethod
    def say_goodbye(self):
        pass

class BankChatbot(Chatbot):
    def introduction(self):
        print('Hello, I can help you with your bank account needs!')

    def ask_for_user_id(self):
        print('To get started, I am going to need your user id. Please enter it now.')

    def ask_for_further_details(self):
        print('Thank you for that, I will also need your SSN')
    
    def say_goodbye(self):
        print('I was able to get everything settled, thank you for your time and have a nice day!')
    
class ResponseSaver(Observer):
    def __init__(self):
        self.responses = []

    def notify(self, data):
        self.responses.append(data)
    
    def print_responses(self):
        print('Here are the responses:')
        for r in self.responses:
            print(r)

bc = BankChatbot()
rs = ResponseSaver()

bc.subscribe(rs)
bc.handle_conversation()

rs.print_responses()
