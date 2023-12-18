import html

class SanitizedString(str):
    def __new__(cls, value):
        if value != html.escape(value):
            raise TypeError('Attempted to create a SanitizedString with a potentially hazardous value')

        return super().__new__(cls, value)

def insert_value(value):
    if isinstance(value, SanitizedString):
        print('Inserting value...')
    else:
        raise Exception('You must insert a SanitizedString only into an HTML page!')

username = '<script></script>'

insert_value(username)
