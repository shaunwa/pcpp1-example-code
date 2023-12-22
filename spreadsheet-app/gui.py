import tkinter as tk
from spreadsheet import Spreadsheet
from functools import partial

class SpreadsheetApp:
    def __init__(self, rows, columns):
        self.root = tk.Tk()
        self.root.title(f'{rows}x{columns} Spreadsheet')
        self.root.geometry(f'{rows * 128}x{columns * 32}')
        self.entries = {}
        self.spreadsheet = Spreadsheet(rows, columns)
        self.setup_grid(rows, columns)

    def setup_grid(self, rows, columns):
        for col in range(1, columns + 1):
            label = tk.Label(self.root, text=chr(ord('A') + col-1)) 
            label.grid(row=0, column=col, sticky='nsew')

        for row in range(1, rows + 1):
            label = tk.Label(self.root, text=row-1) 
            label.grid(row=row, column=0, sticky='nsew')

        for row in range(rows):
            for col in range(columns):
                cell_id = (row, col)
                entry = tk.Entry(self.root)
                entry.bind('<FocusIn>', partial(self.on_focus_in, entry, row, col))
                entry.bind('<FocusOut>', partial(self.on_focus_out, entry, row, col))
                entry.grid(row=row+1, column=col+1, sticky='nsew')
                entry.insert(0, 0)

                cell = self.spreadsheet.get_cell(row, col)
                cell.on_change(partial(self.reload_value_for_cell, cell, row, col))

                self.entries[cell_id] = entry

                self.root.grid_columnconfigure(col+1, weight=1)

            self.root.grid_rowconfigure(row+1, weight=1)

    def on_focus_in(self, entry, row, column, event):
        entry.delete(0, tk.END)
        entry.insert(0, self.spreadsheet.get_cell(row, column).get_content())

    def on_focus_out(self, entry, row, column, event):
        cell = self.spreadsheet.get_cell(row, column)
        cell.set_content(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, cell.get_value())

    def reload_values(self):
        for key, entry in self.entries.items():
            row, column = key
            cell = self.spreadsheet.get_cell(row, column)
            entry.delete(0, tk.END)
            entry.insert(0, cell.get_value())

    def reload_value_for_cell(self, cell, row, column):
        entry = self.entries[(row, column)]
        entry.delete(0, tk.END)
        entry.insert(0, cell.get_value())

    def start(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = SpreadsheetApp(rows=12, columns=12)
    app.start()