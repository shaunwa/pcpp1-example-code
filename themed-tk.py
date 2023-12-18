import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)

style = ttk.Style()
style.configure('TButton', background='red', foreground='green')

def change_theme(theme_name):
    print(f'Switching to the {theme_name} theme')
    style.theme_use(theme_name)
    style.configure('TButton', background='red', foreground='green')
    style.configure('Error.TLabel', background='pink', foreground='white')
    style.configure('Success.TLabel', background='green', foreground='white')

for theme_name in style.theme_names():
    button = ttk.Button(root, text=theme_name, command=lambda x=theme_name: change_theme(x))
    button.pack()

style.configure('Error.TLabel', background='pink', foreground='white')
style.configure('Success.TLabel', background='green', foreground='white')

label_1 = ttk.Label(root, text='An error has occurred!', style='Error.TLabel')
label_1.pack()

label_2 = ttk.Label(root, text='Successfully loaded some data!', style='Success.TLabel')
label_2.pack()

root.mainloop()