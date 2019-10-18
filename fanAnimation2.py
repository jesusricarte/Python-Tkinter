from tkinter import *
import random

class fan_animation:
    def __init__(self):
        
        self.window = Tk()
        self.window.title("LGBTQ Fan")
        self.frame0=Frame(self.window)
        self.frame0.grid(row=0,column=0,sticky=N)
        Label(self.frame0, text="Left-click the fan to increase speed or right-click it to reduce speed.\nUse \"s\" to stop and \"r\" to resume.\nYou can also use the buttons below. ").grid(row=0,column=0)
        self.frame1=Frame(self.window)
        self.frame1.grid(row=2,column=0,sticky=S)
        self.speed=100
        self.myCanvas = Canvas(self.window, bg ="white", height = 300, width=300)
        self.coord = 10, 10, 300, 300
        self.s1=0
        self.s2=90
        self.s3=180
        self.s4=270
        self.state= True
        self.colors=['red','purple','blue','green','yellow', 'orange']
        self.cInx=0
        self.c1=self.colors[0]
        self.c2=self.colors[1]
        self.c3=self.colors[2]
        self.c4=self.colors[3]
        
        self.addSpeed = Button(self.frame1, text = "Add speed", fg="black",command=self.faster)
        self.addSpeed.grid(row=1,column=0)
        self.subSpeed = Button(self.frame1, text = "Reduce speed", fg="black",command=self.slower)
        self.subSpeed.grid(row=1,column=1)
        self.addSpeed = Button(self.frame1, text = "Pause", fg="black",command=self.pause)
        self.addSpeed.grid(row=1,column=3)
        self.subSpeed = Button(self.frame1, text = "Resume", fg="black",command=self.resume)
        self.subSpeed.grid(row=1,column=4)
        self.myCanvas.bind("<Button-1>",self.fasterEv)
        self.myCanvas.bind("<Button-3>",self.slowerEv)
        self.window.bind("s",self.pauseEv)
        self.window.bind("r",self.resumeEv)
        self.window.bind("<space>",self.ranCol)
        self.update_angles()
        self.myCanvas.grid(row=1,column=0)
        self.window.mainloop()


    def update_angles(self):
        if(self.state):
            self.s1+=10
            self.s2+=10
            self.s3+=10
            self.s4+=10
          
            self.myCanvas.delete("c")

            self.c1=self.colors[random.randint(0,5)]
            self.c2=self.colors[random.randint(0,5)]
            self.c3=self.colors[random.randint(0,5)]
            self.c4=self.colors[random.randint(0,5)]

            arc = self.myCanvas.create_arc(self.coord, start=self.s1, extent=30, fill=self.c1, tags="c")
            arv2 = self.myCanvas.create_arc(self.coord, start = self.s2, extent = 30, fill=self.c2,tags = "c")
            arv3 = self.myCanvas.create_arc(self.coord, start = self.s3, extent = 30, fill=self.c3,tags = "c")
            arv3 = self.myCanvas.create_arc(self.coord, start = self.s4, extent = 30, fill=self.c4,tags = "c")
            
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

    def pauseEv(self,event):
        self.state=False
        

    def resumeEv(self,event):
        if(self.state==False):
            self.state=True
            self.update_angles()
    def pause(self):
        self.state=False

    def resume(self):
        if(self.state==False):
            self.state=True
            self.update_angles()

    def ranCol(self,event):
        
        self.c1=self.colors[random.randint(0,5)]
        self.c2=self.colors[random.randint(0,5)]
        self.c3=self.colors[random.randint(0,5)]
        self.c4=self.colors[random.randint(0,5)]
    
    
      
        
fan_animation()
