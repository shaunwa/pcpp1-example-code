import tkinter as tk

root = tk.Tk()
root.title('Line Chart Example')
root.geometry('800x800')

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
MARGIN = 100
CHART_WIDTH = CANVAS_WIDTH - 2*MARGIN
CHART_HEIGHT = CANVAS_HEIGHT - 2*MARGIN

x_coords = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y_coords = [50, 80, 45, 60, 75, 30, 95, 60, 90, 75]

c = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
c.pack()

# Draw the x axis
c.create_line(
    MARGIN,
    CANVAS_HEIGHT - MARGIN,
    CANVAS_WIDTH - MARGIN,
    CANVAS_HEIGHT - MARGIN,
    fill='black',
    width=3)

# Draw the y axis
c.create_line(
    MARGIN,
    MARGIN,
    MARGIN,
    CANVAS_HEIGHT - MARGIN,
    fill='black',
    width=3)

max_x = max(x_coords)
max_y = max(y_coords)

for i in range(len(x_coords) - 1):
    start_normalized_x = x_coords[i] / max_x
    start_normalized_y = y_coords[i] / max_y
    start_canvas_x = MARGIN + start_normalized_x * CHART_WIDTH
    start_canvas_y = CANVAS_HEIGHT - MARGIN - start_normalized_y * CHART_HEIGHT

    end_normalized_x = x_coords[i + 1] / max_x
    end_normalized_y = y_coords[i + 1] / max_y
    end_canvas_x = MARGIN + end_normalized_x * CHART_WIDTH
    end_canvas_y = CANVAS_HEIGHT - MARGIN - end_normalized_y * CHART_HEIGHT

    c.create_line(
        start_canvas_x,
        start_canvas_y,
        end_canvas_x,
        end_canvas_y,
        fill='black'
    )

# Your code goes here

root.mainloop()