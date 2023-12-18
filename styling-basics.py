import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title('Styling Basics')
root.geometry('500x500')

my_entry = tk.Entry(root)
my_entry.pack(padx=10, pady=10)

def entry_activated(event):
    my_entry.configure(highlightthickness=10, highlightcolor='green')
    my_entry.pack_configure(padx=0, pady=0)

my_entry.bind('<FocusIn>', entry_activated)

def entry_deactivated(event):
    my_entry.configure(highlightthickness=0)
    my_entry.pack_configure(padx=10, pady=10)

my_entry.bind('<FocusOut>', entry_deactivated)

# relief_types = [
#     tk.FLAT,
#     tk.GROOVE,
#     tk.RAISED,
#     tk.RIDGE,
#     tk.SOLID,
#     tk.SUNKEN,
# ]

# for relief_type in relief_types:
#     try:
#         my_label = tk.Label(root, text=relief_type, relief=relief_type, borderwidth=4, highlightbackground='red', highlightthickness=2)
#         my_label.pack()
#     except tk.TclError:
#         print(f'This OS does not support the {relief_type} relief type for the button widget')

# for font in font.families():
#     font_label = tk.Label(root, text=font, font=(font, 16))
#     font_label.pack()

root.mainloop()