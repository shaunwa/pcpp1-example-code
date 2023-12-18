import tkinter as tk

root = tk.Tk()
root.title('Pie Chart Example')
root.geometry('800x800')

x_coords = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y_coords = [50, 80, 45, 60, 75, 30, 95, 60, 90, 75]

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

c = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
c.pack()

total_sales = sum(sales)
current_angle = 0

for i in range(len(categories)):
    proportion = sales[i] / total_sales
    c.create_arc(
        5,
        5,
        CANVAS_WIDTH - 5,
        CANVAS_HEIGHT - 5,
        start=current_angle,
        extent=proportion*360,
        fill=slice_colors[i])
    current_angle += proportion * 360

root.mainloop()