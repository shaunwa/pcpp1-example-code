class Book:
    def __init__(self,
                 title='Untitled',
                 author='Unknown',
                 num_pages=0):
        self.title = title
        self.author = author
        self.num_pages = num_pages

        self.status = 'available'


class Library:
    def __init__(self):
        self.books = []

    def __iter__(self):
        return iter(self.books)

    def __contains__(self, value):
        if isinstance(value, str):
            book = next(
                (book for book in self.books if book.title == value),
                None,
            )
            return book is not None

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
    
    def check_in(self, title):
        book = next(
            (book for book in self.books if book.title == title),
            None,
        )

        if book is not None:
            book.status = 'available'

    def check_out(self, title):
        book = next(
            (book for book in self.books if book.title == title),
            None,
        )

        if book is not None:
            book.status = 'checked-out'


my_library = Library()

book_1 = Book(
    title='Pride and Prejudice',
    author='Jane Austen',
    num_pages=279
)

my_library.add_book(book_1)
my_library.add_book(
    Book(
        'War and Peace',
        'Leo Tolstoy',
        1400,
    )
)
my_library.add_book(
    Book(
        'The Great Gatsby',
        'F. Scott Fitzgerald',
        150,
    )
)

for book in my_library:
    print(book.title)

if 'War and Peace' in my_library:
    print('I have a lot of reading to do!')