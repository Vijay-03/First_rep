import math

try:
    import tkinter
except ImportError:       # python 2
    import Tkinter as tkinter


def circle(page, radius, g, h, color="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())                                            # gives the local variables in the function


def plot(page, x, y):
    page.create_line(x, -y, x+1, -y+1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Circle")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

circle(canvas, 100, 100, 100, color="green")
circle(canvas, 100, 100, -100, color="red")
circle(canvas, 100, -100, 100, color="blue")
circle(canvas, 100, -100, -100, color="yellow")
circle(canvas, 10, 30, 30, "violet")
circle(canvas, 10, -30, 30, "black")
circle(canvas, 10, 30, -30, "orange")
circle(canvas, 10, -30, -30, "grey")
circle(canvas, 30, 0, 0, "indigo")

mainWindow.mainloop()
