import tkinter

class fanAnimation():
    def __init__(self):

        window = tkinter.Tk()
        window.title("Make Pie using Arc")

        myCanvas = tkinter.Canvas(window, bg ="white", height = 300, width=300)

        coord = 10, 10, 300, 300
        chan = 0
        
        arc = myCanvas.create_arc(coord, start=chan+0, extent=150, fill="red", tags="freshman")
        arv2 = myCanvas.create_arc(coord, start = chan+150, extent = 120, fill="blue",tags = "Junior")
        arv3 = myCanvas.create_arc(coord, start = chan+270, extent = 90, fill="green",tags = "senior")
        
        myCanvas.pack()
        window.mainloop()


fanAnimation()

