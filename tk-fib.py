from tkinter import Tk, Label

root = Tk()
root.title('Fibonacci Application')
root.geometry('400x400')

a = 1
b = 1

la = Label(root, text=a)
la.pack()
lb = Label(root, text=b)
lb.pack()

def update():
    global a, b

    a, b = b, a + b

    la.config(text=a)
    lb.config(text=b)

    root.after(1000, update)

root.after(1000, update)

root.mainloop()