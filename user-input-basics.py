from tkinter import Tk, Button, Entry, Text, Checkbutton, Radiobutton, Listbox, END, BooleanVar, StringVar, Label

root = Tk()
root.title('User Input Basics')

root.geometry('500x500')

# def validate_names(enter):
#     if len(first_name_str.get()) >= 2 and len(last_name_str.get()) >= 2:
#         validation_label.pack_forget()
#     else:
#         validation_label.pack()

first_name_entry = Entry(root)
first_name_entry.insert(0, 'Enter your name:')
first_name_entry.pack()

description_text = Text(root, height=5, width=30)
description_text.pack()

likes_coffee = BooleanVar()
likes_coffee_checkbutton = Checkbutton(root, text='Likes coffee?', variable=likes_coffee)
likes_coffee_checkbutton.pack()

hair_color_label = Label(root, text='Select hair color:')
hair_color_label.pack()

selected_hair_color = StringVar(root, 'brown')
brown_hair_button = Radiobutton(root, text='Brown', value='brown', variable=selected_hair_color)
brown_hair_button.pack()
blonde_hair_button = Radiobutton(root, text='Blonde', value='blonde', variable=selected_hair_color)
blonde_hair_button.pack()
black_hair_button = Radiobutton(root, text='Black', value='black', variable=selected_hair_color)
black_hair_button.pack()

favorite_food_listbox = Listbox(root)
favorite_food_listbox.insert(END, 'Pizza')
favorite_food_listbox.insert(END, 'Hamburgers')
favorite_food_listbox.insert(END, 'Steak')
favorite_food_listbox.insert(END, 'Salad')
favorite_food_listbox.pack()

def on_button_click():
    first_name = first_name_entry.get()
    description = description_text.get('1.0', END)
    print(f'Hello {first_name}!')
    print(description)

    print(likes_coffee.get())

    if likes_coffee.get():
        print('This person likes coffee!')
    else:
        print('This person doesn\'t like coffee')

    print(f'This person has {selected_hair_color.get()} hair')

my_button = Button(root, text='Click me!', command=on_button_click)
my_button.pack()

root.mainloop()