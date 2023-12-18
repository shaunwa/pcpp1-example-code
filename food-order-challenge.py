from tkinter import Tk, Button, Entry, Text, Checkbutton, Radiobutton, Listbox, END, BooleanVar, StringVar, Label

root = Tk()
root.title('Food Ordering Application')

root.geometry('500x500')

first_name_label = Label(root, text="First Name:")
first_name_label.pack()

first_name_entry = Entry(root)
first_name_entry.pack()

message_text = Text(root, height=5, width=30)
message_text.pack()

hamburger_selected = BooleanVar()
hamburger_checkbutton = Checkbutton(root, text='Hamburger', variable=hamburger_selected)
hamburger_checkbutton.pack()

pizza_selected = BooleanVar()
pizza_checkbutton = Checkbutton(root, text='Pizza', variable=pizza_selected)
pizza_checkbutton.pack()

hair_color_label = Label(root, text='Select pick-up preference:')
hair_color_label.pack()

pick_up_preference = StringVar(root, 'pick-up')
pick_up_button = Radiobutton(root, text='Pick-up', value='pick-up', variable=pick_up_preference)
pick_up_button.pack()
delivery_button = Radiobutton(root, text='Delivery', value='delivery', variable=pick_up_preference)
delivery_button.pack()

def on_button_click():
    first_name = first_name_entry.get()
    message = message_text.get('1.0', END)
    pizza = pizza_selected.get()
    hamburger = hamburger_selected.get()
    pick_up_or_delivery = pick_up_preference.get()

    print('Here are the order details:')
    print(first_name)
    print(message)
    print(f'Pizza: {pizza}')
    print(f'Hamburger: {hamburger}')
    print(pick_up_or_delivery)

my_button = Button(root, text='Place Order', command=on_button_click)
my_button.pack()

root.mainloop()