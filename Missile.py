from curses.textpad import rectangle
from tkinter import *
import time,random

class Missile:
    def __init__(self,canvas,cHeight=0,pixelInc=5,color='orange'):
        self.canvas = canvas
        self.cHeight = cHeight
        self.pixelInc = pixelInc
        self.color = color
        self.width = 8
        self.mHeight = 2.5
        self.__active = False

    def activate(self,y,x):
        self.x = x
        self.y = y
        self.missile=self.canvas.create_rectangle(x,800,x+2.5,800-self.width,outline=self.color,fill=self.color)
        self.__active = True
    
    def deactivate(self):
        #need to delete!
        self.canvas.delete(str(self)[19:30])
        print(self)
        self.__active = False
    
    def is_active(self):
        return self.__active
    
    def next(self):
        self.mHeight = self.mHeight + self.pixelInc
        if self.mHeight >= self.cHeight:
            self.deactivate()
        if self.is_active() == True:
            self.canvas.move(self.missile,0,-self.pixelInc)
    
    def add_missile(canvas,missiles,x,cMax=0,pInc=5,color='orange'):
      for m in missiles:
            if m.is_active() != True:
                missiles.pop(missiles.index(m))
      newMissile = Missile(canvas,cMax,pInc,color)
      newMissile.activate(cMax,x)
      newMissile.next()
      missiles.append(newMissile)






###################################################
###################################################

        
def main(): 
       
        ##### create a window, canvas and ball object
        colors = ["red", "green", "blue", "yellow", "orange", "purple"]
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Missiles
        missiles=[]
        
        
        ############################################
        ####### start simulation
        ############################################
        t=0                # initialize time clock       
        while True:
            time.sleep(0.5)
            color = random.choice(colors)
            x = random.randint(0,w)
            mHeight = random.randint(0,h)
            pixInc = random.randint(2,7)
            Missile.add_missile(canvas,missiles,mHeight,x,pixInc,color)


            for m in missiles:
                m.next()
                



           ##### To complete






     

            # check active status of list of booms (for debugging)
            for m in missiles:
                print(m.is_active(),end=" ")
            print()
            
            # update the graphic and wait time        
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t=t+1      # increment time
       
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

