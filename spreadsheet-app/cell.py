import re

def is_sum_formula(value):
    return value.startswith('SUM(')

def is_product_formula(value):
    return value.startswith('PRODUCT(')

def is_formula(value):
    return is_sum_formula(value) or is_product_formula(value)

def get_cell_names_from_formula(formula):
    match = re.search(r'\(([^)]+)\)', formula)
    if match:
        items = match.group(1)
        return items.split(', ')
    return []

class Cell:
    def __init__(self, spreadsheet):
        self.spreadsheet = spreadsheet
        self.__raw_content = '0'
        self.__upstream_cells = set()
        self.__downstream_cells = set()
        self.__change_subscribers = set()

    def set_content(self, value):
        self.__raw_content = value

        for cell in self.__upstream_cells:
            cell.remove_downstream(self)

        if is_formula(self.__raw_content):
            new_upstreams = self.spreadsheet[get_cell_names_from_formula(self.__raw_content)]
            self.__upstream_cells = set(new_upstreams)

            for cell in self.__upstream_cells:
                cell.add_downstream(self)

        for cell in self.__downstream_cells:
            cell.notify_upstream_change()
    
    def get_content(self):
        return self.__raw_content

    def get_value(self):
        if is_formula(self.__raw_content):
            if is_sum_formula(self.__raw_content):
                total = 0
                for cell in self.__upstream_cells:
                    total += cell.get_value()
                return total
            if is_product_formula(self.__raw_content):
                product = 0
                for cell in self.__upstream_cells:
                    product *= cell.get_value()
                return product
        else:
            try:
                return float(self.__raw_content)
            except ValueError:
                return 'ERR'

    def add_downstream(self, cell):
        self.__downstream_cells.add(cell)

    def remove_downstream(self, cell):
        self.__downstream_cells.discard(cell)

    def on_change(self, notify_change):
        self.__change_subscribers.add(notify_change)

    def notify_upstream_change(self):
        for func in self.__change_subscribers:
            func()

        for cell in self.__downstream_cells:
            cell.notify_upstream_change()