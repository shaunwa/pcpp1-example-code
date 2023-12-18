import tkinter as tk

root = tk.Tk()
root.title('Canvas Challenge ')
root.geometry('800x800')
root.resizable(False, False)

canvas = tk.Canvas(root, width=800, height=800, bg='white')
canvas.pack()

selected_shape = 'circle'

def select_circle():
    global selected_shape
    selected_shape = 'circle'

def select_square():
    global selected_shape
    selected_shape = 'square'

def select_line():
    global selected_shape
    selected_shape = 'line'

shape_selection_frame = tk.Frame(root)
circle_button = tk.Button(shape_selection_frame, text='Circle', command=select_circle)
circle_button.pack()
square_button = tk.Button(shape_selection_frame, text='Square', command=select_square)
square_button.pack()
line_button = tk.Button(shape_selection_frame, text='Line', command=select_line)
line_button.pack()

canvas.create_window(800, 0, anchor=tk.NE, window=shape_selection_frame)

def handle_canvas_click(event):
    if selected_shape == 'circle':
        canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill='black')
    elif selected_shape == 'square':
        canvas.create_rectangle(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill='black')
    elif selected_shape == 'line':
        canvas.create_line(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill='black')

canvas.bind('<Button-1>', handle_canvas_click)

root.mainloop()