import tkinter as tk

root = tk.Tk()
root.title('Bar Chart Example')
root.geometry('800x800')

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
MARGIN = 100
CHART_WIDTH = CANVAS_WIDTH - 2*MARGIN
CHART_HEIGHT = CANVAS_HEIGHT - 2*MARGIN
BETWEEN_BAR_SPACING = 10

c = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
c.pack()

categories = ['Electronics', 'Clothing', 'Books', 'Sports', 'Food']
sales = [100, 200, 150, 230, 145]
bar_colors = ['red', 'yellow', 'green', 'blue', 'purple']

bar_width = (
    CHART_WIDTH
    - (len(categories) + 1)
    * BETWEEN_BAR_SPACING) / len(categories)

max_bar_value = max(sales)

for i in range(len(categories)):
    left_x = MARGIN + (i + 1) * BETWEEN_BAR_SPACING + i * bar_width
    right_x = left_x + bar_width

    bottom_y = CANVAS_HEIGHT - MARGIN
    bar_height = sales[i] / max_bar_value * CHART_HEIGHT
    top_y = bottom_y - bar_height

    c.create_rectangle(
        left_x,
        top_y,
        right_x,
        bottom_y,
        fill=bar_colors[i]
    )

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


root.mainloop()