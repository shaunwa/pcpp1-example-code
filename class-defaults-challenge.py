def attr_defaults(defaults_dict):
    def decorator(cls):
        cls.__defaults = defaults_dict

        def new_getattribute(self, name):
            if object.__getattribute__(self, name) == None:
                if name in object.__getattribute__(self, '__class__').__defaults:
                    return object.__getattribute__(self, '__class__').__defaults[name]

            return object.__getattribute__(self, name)

        cls.__getattribute__ = new_getattribute
    
        @classmethod
        def change_default(cls, key, value):
            cls.__defaults[key] = value
        
        cls.change_default = change_default

        return cls
    
    return decorator


@attr_defaults({
    'title': 'N/A',
    'author': 'Unknown',
    'number_of_pages': 0,
    'price': 0,
})
class Book:
    def __init__(self, title=None, author=None, number_of_pages=None, price=None):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.price = price

book1 = Book()
print(f'The title is {book1.title}')
Book.change_default('title', 'Unknown')
print(f'The title is {book1.title}')
book1.title = 'Gone with the Wind'
Book.change_default('title', 'This book does not have a title entered!')
print(f'The title is {book1.title}')