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

class MessagesListUI(Observer):
    def notify(self, data):
        print(f'Received new message: {data}, displaying in interface!')
    
class IncomingMessageHandler(ConcreteSubject):
    def new_message(self, text):
        self.update(text)
    
ml = MessagesListUI()
imh = IncomingMessageHandler()
imh.subscribe(ml)

imh.new_message('Hello, are you there?')
imh.new_message('Anyone out there?')