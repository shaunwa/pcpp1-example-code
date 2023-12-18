import tkinter as tk

root = tk.Tk()
root.title('Observable String Example')
root.geometry('500x500')

my_str = 'Hello!'
my_observable_str = tk.StringVar(value='Change the text here to see it reflected in the label!')

entry = tk.Entry(root, textvariable=my_observable_str)
entry.pack()

label = tk.Label(root, text=my_str, textvariable=my_observable_str)
label.pack()

root.mainloop()