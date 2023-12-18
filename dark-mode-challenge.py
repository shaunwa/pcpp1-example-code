import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Dark Mode Demo')
root.geometry('500x500')

current_mode = 'light'
other_mode = 'dark'

style = ttk.Style()
style.theme_use('classic')

def activate_light_mode():
    style.configure('TButton', background='white', foreground='black')
    style.configure('TLabel', background='white', foreground='black')
    style.configure('TEntry', background='white', foreground='black')
    root.configure(background='white')

def activate_dark_mode():
    style.configure('TButton', background='black', foreground='white')
    style.configure('TLabel', background='black', foreground='white')
    style.configure('TEntry', background='black', foreground='white')
    root.configure(background='black')

activate_light_mode()

def toggle_mode():
    global current_mode, other_mode
    current_mode, other_mode = other_mode, current_mode
    mode_toggle_button.configure(text=f'Switch to {other_mode}')

    if current_mode == 'light':
        activate_light_mode()
    else:
        activate_dark_mode()


mode_toggle_button = ttk.Button(root, text=f'Switch to {other_mode}', command=toggle_mode)
mode_toggle_button.pack()

label_1 = ttk.Label(root, text='My Application')
label_1.pack()

entry_1 = ttk.Entry(root)
entry_1.pack()

button_1 = ttk.Button(root, text='Submit')
button_1.pack()

root.mainloop()