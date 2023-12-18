class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.status = 'available'

class Library:
    def __init__(self):
        self.books = []

    def __iter__(self):
        return iter(self.books)

    def __getitem__(self, key_or_index):
        if type(key_or_index) is str:
            key = key_or_index
            book = next((book for book in self.books if book.title == key), None)
            if book is None:
                raise KeyError('Library does not contain a book with that title!')
            return book
        elif type(key_or_index) is int:
            index = key_or_index
            if index >= len(self.books):
                raise IndexError('Library does not have that many books')
            book = self.books[index]
            return book
        else:
            raise TypeError(f'Library cannot be accessed with a key of type {type(key_or_index)}')

    def __contains__(self, value):
        if isinstance(value, str):
            book = next((book for book in self.books if book.title == value), None)
            return book is not None

    def add_book(self, book):
        self.books.append(book)

my_library = Library()

my_library.add_book(Book('Pride and Prejudice', 'Jane Austen', 279))
my_library.add_book(Book('War and Peace', 'Leo Tolstoy', 1400))
my_library.add_book(Book('The Great Gatsby', 'F. Scott Fitzgerald', 150))

my_library['War and Peace'] # Make this happen!
my_library['Go Dog Go']

print(my_library[0].title) # This should be 'Pride and Prejudice'
my_library[10]
