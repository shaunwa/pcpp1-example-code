class InvalidAgeException(Exception):
    pass

class InvalidYearException(Exception):
    pass

def convert_to_int(string):
    return int(string)

def get_age():
    try:
        age_raw = input('Enter your age: ')
        age = convert_to_int(age_raw)
        return age
    except ValueError as e:
        raise InvalidAgeException(f'The age you entered ({age_raw}) is invalid!') from e

def get_year():
    try:
        year_raw = input('Enter a year: ')
        year = convert_to_int(year_raw)
        return year
    except ValueError:
        raise InvalidYearException(f'The year you entered ({year_raw}) is invalid!')

def get_user_info():
    try:
        year = get_year()
        age = get_age()
    except InvalidYearException:
        print('Invalid year!')
    except InvalidAgeException:
        print('Invalid age!')

get_user_info()