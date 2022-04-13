from tkinter import *
import math,time,random
from Dot import Dot


class Explosion:

    #### to complete
    def __init__(self,canvas,booms,x,y):
        self.canvas = canvas
        self.booms=booms
        self.x = x
        self.y = y
        self.rad = 80
        self.dots = 15
        self.add_explosion()
        
    
    def activate(self):
        x = self.x
        y = self.y
        rad = self.rad

    def deactivate(self):
      print('deac')

    def is_active(self):
      return True
    
    def add_explosion(self):
     dotList = []
     for rad in self.rad:
      if self.is_active() == True:
        for dots in self.dots:
            deg = random.randint(1,360)
            __x = math.cos(deg)*rad
            __y = math.sin(deg)*rad
            dotList.append(Dot(self.canvas,__x+self.x,__y+self.y,"rainbow",True))
















        
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root,width=w,height=h,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        #Initialize list of Explosions
        booms=[]
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Explosion.add_explosion(canvas,booms,e.x,e.y) )
        
        ############################################
        ####### start simulation
        ############################################
        
        while True:
            # scan booms list and execute next time step
            for boom in booms:
                boom.next()
                
            # check active status of list of booms (for debugging)
            for b in booms:
                print(b.is_active(),end=" ")
            print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

