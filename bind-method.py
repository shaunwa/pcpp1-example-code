import tkinter as tk

root = tk.Tk()
root.title('Observable Boolean Example')
root.geometry('500x500')

def on_button_click(event):
    print('Button 1 was clicked!')
    print(event)

# button_1 = tk.Button(root, text='Button 1', command=on_button_1_click)
my_button = tk.Button(root, text='My Button')
my_button.bind('<Button-1>', on_button_click)
my_button.bind('<Button-2>', on_button_click)
my_button.bind('<Button-3>', on_button_click)

my_button.pack()

def on_a_pressed_in_entry(event):
    dummy.focus_set()

def on_focus_in_entry(event):
    print('The entry has received the focus!')

def on_focus_out_entry(event):
    print('The entry has lost the focus!')

entry_1 = tk.Entry(root)
entry_1.bind('<Key-a>', on_a_pressed_in_entry)
entry_1.bind('<FocusIn>', on_focus_in_entry)
entry_1.bind('<FocusOut>', on_focus_out_entry)
entry_1.pack()

dummy = tk.Frame(root, height=0, width=0)
dummy.pack()

entry_2 = tk.Entry(root)
entry_2.pack()

root.mainloop()