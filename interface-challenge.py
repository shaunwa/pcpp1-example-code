import tkinter as tk

root = tk.Tk()
root.title('Interface Challenge')
root.geometry('500x500')

top_left = tk.Frame(root)
top_left.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

label = tk.Label(top_left, text='Hello!')
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

top_right = tk.Frame(root)
top_right.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)

entry_1 = tk.Entry(top_right)
entry_1.pack(fill=tk.X)
entry_2 = tk.Entry(top_right)
entry_2.pack(fill=tk.X)
button_1 = tk.Button(top_right, text='Submit')
button_1.pack(fill=tk.X)

bottom_left = tk.Frame(root)
bottom_left.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)

text_area = tk.Text(bottom_left)
text_area.pack(fill=tk.BOTH)

bottom_right = tk.Frame(root)
bottom_right.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)
bottom_right.rowconfigure(0, weight=1)
bottom_right.rowconfigure(1, weight=1)
bottom_right.columnconfigure(0, weight=1)
bottom_right.columnconfigure(1, weight=1)

button_tl = tk.Button(bottom_right, text='Top Left')
button_tl.grid(row=0, column=0, sticky='nsew')
button_tr = tk.Button(bottom_right, text='Top Right')
button_tr.grid(row=0, column=1, sticky='nsew')
button_bl = tk.Button(bottom_right, text='Bottom Left')
button_bl.grid(row=1, column=0, sticky='nsew')
button_br = tk.Button(bottom_right, text='Bottom Right')
button_br.grid(row=1, column=1, sticky='nsew')

# my_frame = tk.Frame(root)
# my_frame.pack()

# button_1 = tk.Button(my_frame)

# button_2 = tk.Button(root, text='Hello')
# button_2.place(relx=0, rely=0, relheight=0.75, relwidth=0.5)

root.mainloop()