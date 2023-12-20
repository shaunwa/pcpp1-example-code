import tkinter as tk
from tkinter import ttk
import requests

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root

        self.expense_list = ttk.Treeview(root, columns=('id', 'name', 'date', 'category', 'amount'), show='headings')
        self.expense_list.grid(row=0, column=0, columnspan=4)
        self.expense_list.config(selectmode='browse')

        for col in self.expense_list['columns']:
            self.expense_list.heading(col, text=col)

        tk.Button(root, text='Delete', command=self.delete_expense).grid(row=1, column=3)

        self.name_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.amount_var = tk.StringVar()

        tk.Entry(root, textvariable=self.name_var).grid(row=2, column=0)
        tk.Entry(root, textvariable=self.date_var).grid(row=2, column=1)
        tk.Entry(root, textvariable=self.category_var).grid(row=2, column=2)
        tk.Entry(root, textvariable=self.amount_var).grid(row=2, column=3)

        tk.Button(root, text='Add Expense', command=self.add_expense).grid(row=3, column=3)

        self.load_expenses()

    def load_expenses(self):
        response = requests.get('http://localhost:8000/expenses')
        for expense in response.json():
            self.expense_list.insert('', tk.END, values=(expense[0], expense[1], expense[2], expense[3], expense[4]))

    def add_expense(self):
        new_expense = {
            'name': self.name_var.get(),
            'date': self.date_var.get(),
            'category': self.category_var.get(),
            'amount': self.amount_var.get(),
        }

        response = requests.post('http://localhost:8000/expenses', json=new_expense)
        expense = response.json()

        self.expense_list.insert('', tk.END, values=(expense['id'], expense['name'], expense['date'], expense['category'], expense['amount']))

        self.name_var.set('')
        self.date_var.set('')
        self.category_var.set('')
        self.amount_var.set('')

    def delete_expense(self):
        selected_item = self.expense_list.selection()[0]
        expense_id = self.expense_list.item(selected_item)['values'][0]
        response = requests.delete(f'http://localhost:8000/expenses/{expense_id}')
        self.expense_list.delete(selected_item)

if __name__ == '__main__':
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()