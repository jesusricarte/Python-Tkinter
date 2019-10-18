from tkinter import *

canvas_width = 500
canvas_height = 150
class DrawPad:
   def __init__(self):
      self.w = Tk()
      self.w.title( "Painting using Ovals" )
      self.c = Canvas(self.w, 
                 width=canvas_width, 
                 height=canvas_height)
      self.c.pack(expand = YES, fill = BOTH)
      self.clearButton = Button(self.w,text = "Clear",fg="black",command=self.clear)
      self.clearButton.pack(side=BOTTOM)
      self.c.bind( "<B1-Motion>", self.paint )
      self.w.mainloop()


   def paint(self, event):
      python_green = "green"
      x1, y1 = ( event.x  ), ( event.y  )
      x2, y2 = ( event.x ), ( event.y  )
      self.c.create_oval( x1, y1, x2, y2, fill = python_green )

   def clear(self):
      self.c.delete("all")
DrawPad()

