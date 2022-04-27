from tkinter import *
import math
import time, random

class Alien:
    def __init__(self,canvas,pixInc=4,color='yellow',aWidth=50,aHeight=50,IPV=1): #IPV = Intrinsic Point Value (will be used for gaming)
        self.canvas=canvas
        self.pixInc=pixInc
        self.color=color
        self.aWidth=aWidth
        self.aHeight=aHeight
        self.IPV=IPV
        self._active = False
        self.aLoc = 0 #alien location on y axis
        self.rect = self.canvas.create_rectangle(self.x,self.y,self.x+self.aWidth,self.y+self.aHeight,outline=self.color,fill=self.color)
    
    def activate(self):
        self.x=random.randint(0,self.canvas.winfo_width())
        self.y=0
        self._active = True
    
    def deactivate(self):
        self.canvas.delete(self.rect) #necessary?
        self._active=False
    
    def next(self):
        self.aLoc = self.aLoc + self.pixInc
        if self.aLoc >= self.canvas.winfo_height():
            self.deactivate()
        if self._active() == True:
            self.canvas.move(self.rect,0,self.pixInc)

    def is_shot(self,x0,y0):
        if (self.x <= x0 <= self.x+self.aWidth) and (self.y <= y0 <= self.y+self.aHeight):
            return True
        else:
            return False
        
################################################################
################################################################

class Alien_red(Alien):
    def __init__(self,c):
        super().__init__() #init parent class!
        self.image=PhotoImage(file="alien_red.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()
        # constructor to complete

    # to complete
        


###############################################################
###############################################################

class Alien_green(Alien_red):

    # to complete


###############################################################
###############################################################
                


class Alien_blue(Alien_red):


    # to complete




###############################################################
################################################################
def shoot(alien,x,y):
    if alien.is_shot(x,y):
        result="hit!"
    else:
        result="miss!"
    print(x,y,result)


    
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (neede to capture w and h for canvas)
        

        #Initialize alien
        alien=Alien(canvas)
        #alien=Alien_red(canvas)
        #alien=Alien_green(canvas)
        #alien=Alien_blue(canvas)

        alien.activate()
        

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(alien,e.x,e.y))

        
        ############################################
        ####### start simulation
        ############################################
        #t=0               # time clock
        while True:

            if (not alien.is_active()):
                alien.activate()
              
            alien.next() # next time step
                    
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second (simulation
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

