# import tkinter
#
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
# tkinter._test()
#
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("panel")
mainWindow.geometry('640x480')

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow.mainloop()
