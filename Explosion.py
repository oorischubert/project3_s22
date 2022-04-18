from tkinter import *
import math,time,random
from Dot import Dot


class Explosion:
    dotList = []
    #### to complete
    def __init__(self,canvas,booms,x,y):
        self.tag="explosion"
        self.canvas = canvas
        self.booms=booms
        self.x = x
        self.y = y
        self.maxRad = 80
        self.currentRad = 0
        self.dots = 15
        self.__active = False
        self.dotList = []
        self.activate()
        
      
        
    
    def activate(self):
        self.__active = True

    def deactivate(self):
      for dot in self.dotList:
       self.canvas.delete(dot)
      self.__active = False
      print('deactivated')

    def is_active(self):
      return self.__active
    
    def next(self):
           self.currentRad = self.currentRad + 1
           if self.is_active() == True:
            for ring in range(15):
              deg = random.randint(1,360)
              __x = math.cos(deg)*self.currentRad
              __y = math.sin(deg)*self.currentRad
              dot = Dot(self.canvas,__x+self.x,__y+self.y,"rainbow",True)
              self.dotList.append(dot)
            if self.currentRad >= self.maxRad:
                self.deactivate()
               
                
   
    def add_explosion(canvas,booms,x,y,color,radius):
      newExp = Explosion(canvas,booms,x,y)
      booms.append(newExp)
      















        
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
        root.bind("<Button-1>",lambda e:Explosion.add_explosion(canvas,booms,e.x,e.y,'rainbow',80) )
        
        ############################################
        ####### start simulation
        ############################################
        
        while True:
            # scan booms list and execute next time step
            for boom in booms:
                boom.next()
                
            # check active status of list of booms (for debugging)
            for b in booms:
                if b.is_active() == False:
                    booms.pop(booms.index(b))
                print(b.is_active(),end=" ")
            print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

