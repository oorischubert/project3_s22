from tkinter import *
import math,time,random
from Dot import Dot

#just a test file

class Explosion:
    dotList = []
    #### to complete
    def __init__(self,canvas,booms,x,y):
        self.canvas = canvas
        self.booms=booms
        self.x = x
        self.y = y
        self.rad = 80
        self.dots = 15
       
        
        
    
    def activate(self):
        x = self.x
        y = self.y
        rad = self.rad

    def deactivate(self):
      print('deac')

    def is_active(self):
      return True
    
    def next(self):
        if self.is_active() == True:
            self.rad = self.rad+1
    
    def add_explosion(canvas,x,y):
      for rad in range(80):
        time.sleep(0.03)
        for ring in range(15):
            deg = random.randint(1,360)
            __x = math.cos(deg)*rad
            __y = math.sin(deg)*rad
            Dot(canvas,__x+x,__y+y,"rainbow",True)
            
















        
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
        root.bind("<Button-1>",lambda e:Explosion.add_explosion(canvas,e.x,e.y) )
        
        ############################################
        ####### start simulation
        ############################################
        
        while True:
            
            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()
