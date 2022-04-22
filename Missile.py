from curses.textpad import rectangle
from tkinter import *
import time,random

class Missile:
    def __init__(self,canvas,cHeight=0,pixelInc=5,color='orange',width=8,mHeight=25):
        self.canvas = canvas
        self.cHeight = cHeight
        self.pixelInc = pixelInc
        self.color = color
        self.width = width
        self.mHeight = mHeight
        self.__active = False

    def activate(self,x,y):
        self.x = x
        self.y = y
        self.missile=self.canvas.create_rectangle(x,y,x+self.width,y+self.mHeight,outline=self.color,fill=self.color)
        self.__active = True
    
    def deactivate(self):
        self.__active = False
    
    def is_active(self):
        return self.__active
    
    def next(self):
        self.mHeight = self.mHeight + 1
        if self.is_active() == True:
            self.canvas.move(self.missile,-self.pixelInc,0)
        if self.mHeight >= self.cHeight:
            self.deactivate()
    
    def add_missile(canvas,missiles,x,cMax=0,pInc=5,color='orange'):
      newMissile = Missile(canvas,x,pInc,color,cMax)
      newMissile.activate(x,cMax)
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
            Missile.add_missile(canvas,missiles,x,mHeight,pixInc,color)


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

