from tkinter import *

class SpaceShip:
    def __init__(self,canvas):
     self.canvas=canvas
     self._active = False
     self.image=PhotoImage(file="ship.png")
     self.xLoc=self.canvas.winfo_width()/2

    def activate(self):
         self.ship=self.canvas.create_image(self.xLoc,self.canvas.winfo_height()-40,anchor=CENTER,image=self.image)
         self._active = True
    
    def deactivate(self):
        self._active = False
        self.canvas.delete(self.ship)

    def is_active(self):
        return self._active
    
    def shift_left(self):
     if self.canvas.coords(self.ship)[0] > 15 + self.image.width()/2 and self._active:
      self.xLoc-=15
      self.canvas.move(self.ship,-15,0)
    def shift_right(self):
     if self.canvas.coords(self.ship)[0] < self.canvas.winfo_width() - 15 - self.image.width()/2 and self._active:
      self.xLoc+=15
      self.canvas.move(self.ship,15,0)


def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h) # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)


    #Initialize the ship
    ship=SpaceShip(canvas)
    ship.activate()
    
    
    ####### Tkinter binding mouse actions
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())

    root.mainloop() # wait until the window is closed
    

if __name__=="__main__":
    main()

