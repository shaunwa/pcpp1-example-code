from tkinter import Tk, Label, Message

app_font = 'Arial'

h1_size = 32
h2_size = 24
h3_size = 19
h4_size = 16
h5_size = 13
h6_size = 11

sizes = [
    h1_size,
    h2_size,
    h3_size,
    h4_size,
    h5_size,
    h6_size
]

root = Tk()
root.title('My First Tkinter Application!')
root.geometry('800x500')

for size in sizes:
    l = Label(root, text='Welcome to Tkinter', font=(app_font, size))
    l.pack()

m1 = Message(root, text='This is a message!', width=400)
m1.pack()

root.mainloop()
