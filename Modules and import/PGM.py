try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("panel")
mainWindow.geometry('640x480+8+4')

label = tkinter.Label(mainWindow, text="mahalo")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)            # BOTH = X, Y
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)
button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()