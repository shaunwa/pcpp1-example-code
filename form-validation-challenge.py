import tkinter as tk

root = tk.Tk()
root.title('Form Validation Challenge')
root.geometry('500x500')

first_name_str = tk.StringVar()
last_name_str = tk.StringVar()

def validate_first_name(event):
    if len(first_name_str.get()) < 2:
        validation_label.pack()
    else:
        validation_label.pack_forget()

def validate_last_name(event):
    if len(last_name_str.get()) < 2:
        validation_label.pack()
    else:
        validation_label.pack_forget()

entry_1 = tk.Entry(root, textvariable=first_name_str)
entry_1.bind('<FocusOut>', validate_first_name)
entry_1.pack()

entry_2 = tk.Entry(root, textvariable=last_name_str)
entry_2.bind('<FocusOut>', validate_last_name)
entry_2.pack()

my_button = tk.Button(root, text='My Button')
my_button.pack()

validation_label = tk.Label(root, text='The values for your inputs are invalid!')

root.mainloop()