import tkinter as tk

root = tk.Tk()
root.title('Organizing Widgets')
root.geometry('500x500')
root.rowconfigure(3, minsize=100)
root.columnconfigure(3, minsize=100)

button_1 = tk.Button(root, text='Button 1')
button_2 = tk.Button(root, text='Button 2')
button_3 = tk.Button(root, text='Button 3')
button_4 = tk.Button(root, text='Button 4')
button_5 = tk.Button(root, text='Button 5')

button_1.grid(row=0, column=0, columnspan=2, sticky='nsew')
button_2.grid(row=1, column=0)
button_3.grid(row=1, column=1)
button_4.grid(row=5, column=5)
button_5.grid(row=4, column=4)

root.mainloop()