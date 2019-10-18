from tkinter import *


class fan_animation:
    def __init__(self):

        self.window = Tk()
        self.window.title("Fan")
        self.frame0=Frame(self.window)
        self.frame0.grid(row=0,column=0,sticky=N)
        Label(self.frame0, text="Left-click the fan to increase speed or right-click it to reduce speed.\nYou can also use the buttons below.").grid(row=0,column=0)
        self.frame1=Frame(self.window)
        self.frame1.grid(row=2,column=0,sticky=S)
        self.speed=100
        self.myCanvas = Canvas(self.window, bg ="white", height = 300, width=300)
        self.coord = 10, 10, 300, 300
        self.s1=0
        self.s2=120
        self.s3=240
        self.addSpeed = Button(self.frame1, text = "Add speed", fg="black",command=self.faster)
        self.addSpeed.grid(row=1,column=0)
        self.subSpeed = Button(self.frame1, text = "Reduce speed", fg="black",command=self.slower)
        self.subSpeed.grid(row=1,column=1)
        self.myCanvas.bind("<Button-1>",self.fasterEv)
        self.myCanvas.bind("<Button-3>",self.slowerEv)
        self.update_angles()
        self.myCanvas.grid(row=1,column=0)
        self.window.mainloop()


    def update_angles(self):
        self.s1+=10
        self.s2+=10
        self.s3+=10
        self.myCanvas.delete("f1")
        self.myCanvas.delete("f2")
        self.myCanvas.delete("f3")

        arc = self.myCanvas.create_arc(self.coord, start=self.s1, extent=30, fill="red", tags="f1")
        arv2 = self.myCanvas.create_arc(self.coord, start = self.s2, extent = 30, fill="red",tags = "f2")
        arv3 = self.myCanvas.create_arc(self.coord, start = self.s3, extent = 30, fill="red",tags = "f3")
        self.window.after(self.speed,self.update_angles)

    def faster(self):
        if(self.speed-10>0):
            self.speed-=10

    def slower(self):
        self.speed+=10

    def fasterEv(self,event):
        if(self.speed-10>0):
            self.speed-=10

    def slowerEv(self,event):
        self.speed+=10

        
        
fan_animation()
