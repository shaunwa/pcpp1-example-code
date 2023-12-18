import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title('Styling Playground')
root.geometry('500x500')

selected_widget = tk.StringVar(value='label')
label_option = tk.Radiobutton(root, text='Label', value='label', variable=selected_widget)
label_option.pack()
button_option = tk.Radiobutton(root, text='Button', value='button', variable=selected_widget)
button_option.pack()
entry_option = tk.Radiobutton(root, text='Entry', value='entry', variable=selected_widget)
entry_option.pack()

foreground_entry = tk.Entry(root)
foreground_entry.pack()

background_entry = tk.Entry(root)
background_entry.pack()

new_widget = None

def create_widget_clicked():
    global new_widget

    if selected_widget.get() == 'label':
        widget_text = 'I am a label!'
        Widget = tk.Label
    elif selected_widget.get() == 'button':
        widget_text = 'I am a button!'
        Widget = tk.Button
    elif selected_widget.get() == 'entry':
        Widget = tk.Entry
    else:
        print('That is not an option!')
        return

    if new_widget is not None:
        new_widget.pack_forget()

    new_widget = Widget(root, text=widget_text, foreground=foreground_entry.get(), background=background_entry.get())
    new_widget.pack()

submit_button = tk.Button(root, text='Create Widget', command=create_widget_clicked)
submit_button.pack()

root.mainloop()