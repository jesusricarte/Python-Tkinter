from tkinter import *

window = Tk()
window.title("Label Widget Example")
lblPrincipal = Label(window, text = " Principal ", fg = "red", bg = "light blue")
lblPrincipal.grid(padx = 120, pady= 15)
window.mainloop()
