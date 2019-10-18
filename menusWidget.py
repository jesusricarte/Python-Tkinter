from tkinter import *

def fun():
    x=0

window = Tk()
window.title("Menu Bar Example")
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=fun)
filemenu.add_command(label="Open",command=fun)
filemenu.add_command(label="Save",command=fun)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)
menubar.add_cascade(label="File",menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index",command=fun)
helpmenu.add_command(label="About...",command=fun)
menubar.add_cascade(label="Help ",menu=helpmenu)

window.config(menu=menubar)
window.mainloop()
