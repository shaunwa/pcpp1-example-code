import re

class OddInt(int):
    def __new__(cls, value):
        if value % 2 == 0:
            adjusted_value = value + 1
        else:
            adjusted_value = value

        new_instance = super().__new__(cls, adjusted_value)
        return new_instance

    def __add__(self, other):
        return OddInt(int(self) + int(other))

with open('all-numbers-are-odd.py', 'r') as file:
    code = file.read()
    modified_code = re.sub(r'(\d+)', r'OddInt(\1)', code)
    exec(modified_code)