from tkinter import *

class increaseOvalEvent:
    def __init__(self):
        self.radius=50
        self.canvas_width=500
        self.canvas_height=500
        self.w = Tk()
        self.w.title("Resizing Oval")
        self.c= Canvas(self.w,width=self.canvas_width,height=self.canvas_height)
        self.c.pack()
        ov = self.c.create_oval(200-self.radius,150-self.radius,200+self.radius,150+self.radius,fill="red")
        self.c.bind("<Button-1>",self.increase)
        mainloop()
    def increase(self,event):
        self.radius+=5
        ov = self.c.create_oval(200-self.radius,150-self.radius,200+self.radius,150+self.radius,fill="red")
                
     
    
    
        

    


increaseOvalEvent()
