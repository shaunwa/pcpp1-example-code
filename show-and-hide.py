import tkinter as tk

root = tk.Tk()
root.title('Observable Boolean Example')
root.geometry('500x500')

show_entry = tk.BooleanVar(value=True)

def toggle_entry():
    if show_entry.get():
        entry.pack()
    else:
        entry.pack_forget()

check_button = tk.Checkbutton(root, variable=show_entry, text='Show Entry?', command=toggle_entry)
check_button.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()