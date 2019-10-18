from tkinter import *
window = Tk()
window.title("Frame Widget")
frame = Frame(window)
frame.pack()

bottomframe = Frame(window)
bottomframe.pack(side = BOTTOM)

yellowbutton = Button(frame, text = "yellow",fg = "yellow")
yellowbutton.pack(side = TOP)

redbutton = Button(frame, text = "Red",fg = "red")
redbutton.pack(side = LEFT)

greenbutton = Button(frame, text = "Brown",fg = "brown")
greenbutton.pack(side = LEFT)

bluebutton = Button(frame, text = "Blue",fg = "blue")
bluebutton.pack(side = RIGHT)

bluebutton = Button(bottomframe, text = "Black",fg = "black")
bluebutton.pack(side = BOTTOM)

window.mainloop()

