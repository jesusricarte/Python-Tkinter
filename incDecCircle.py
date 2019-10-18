from tkinter import *
class EnlargeShrinkCircle:
    def __init__(self):
        self.radius = 50

        window = Tk()
        window.title("Control Circle Demo")
        self.canvas = Canvas(window, bg= "white", width=400,height=300)
        self.canvas.pack()
        self.canvas.create_oval(200 - self.radius, 150 - self.radius,200+self.radius,150+self.radius,tags="oval")
        self.canvas.bind("<Button-1>",self.increaseCircle)
        self.canvas.bind("<Button-3>",self.decreaseCircle)

        window.mainloop()


    def increaseCircle(self,event):
        self.canvas.delete("oval")
        if self.radius < 150:
            self.radius += 2
        self.canvas.create_oval(200-self.radius,150-self.radius,200+self.radius,150+self.radius,tags="oval")

    def decreaseCircle(self,event):
        self.canvas.delete("oval")
        if self.radius > 2:
            self.radius -=2
        self.canvas.create_oval(200-self.radius,150-self.radius,200+self.radius,150+self.radius, tags="oval")

EnlargeShrinkCircle()
