import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Canvas Basics')
root.geometry('800x800')
root.resizable(False, False)

canvas = tk.Canvas(root, width=800, height=800, bg='white')
canvas.pack()

canvas.create_rectangle(200, 200, 300, 300, fill='blue', outline='black', width=4)
canvas.create_oval(400, 400, 600, 750, fill='red', outline='yellow', width=10)
canvas.create_line(250, 250, 500, 575, fill='green', width=8)

canvas.create_text(400, 400, text='Hello Tkinter Canvas!', fill='purple', font=('Times New Roman', 20))

with Image.open('flamingoes.jpg') as img_raw:
    resized_image = img_raw.resize((200, 200))
    img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=img, anchor=tk.NW)

toolbar_frame = tk.Frame(root)
button_1 = tk.Button(toolbar_frame, text='Click me!')
button_1.pack()
button_2 = tk.Button(toolbar_frame, text='Click me!')
button_2.pack()
button_3 = tk.Button(toolbar_frame, text='Click me!')
button_3.pack()
entry_1 = tk.Entry(toolbar_frame)
entry_1.pack()

canvas.create_window(600, 200, window=toolbar_frame)

root.mainloop()