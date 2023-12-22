from cell import Cell

class Spreadsheet:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cells = [[Cell(self) for _ in range(columns)] for _ in range(rows)]

    def _get_cell_by_name(self, name):
        column = name[0]
        row = name[1]

        column_number = ord(column) - ord('A')
        row_number = int(row)

        return self.get_cell(row_number, column_number)

    def get_cell(self, row, column):
        return self.cells[row][column]

    def __getitem__(self, name):
        if isinstance(name, list):
            return [self._get_cell_by_name(cell_name) for cell_name in name]
        else:
            return self._get_cell_by_name(name)

    def __setitem__(self, name, value):
        self._get_cell_by_name(name).set_content(value)