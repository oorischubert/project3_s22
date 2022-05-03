from tkinter import *
import math,time,random
from Dot import Dot
import numpy as np


class Explosion:
    #### to complete
    def __init__(self,canvas,color='rainbow',maxRad=80):
        self.color = color
        self.canvas = canvas
        self.maxRad = maxRad
        self.dots = 15
        self._active = False
        self.dotList = []
    
    def activate(self,x,y):
        self.x = x
        self.y = y
        self.currentRad = 0
        self._active = True

    def deactivate(self):
      for dot in self.dotList:
       self.canvas.delete(dot.dots)
      self._active = False

    def is_active(self):
      return self._active
    
    def next(self):
           self.currentRad += 1
           if self.is_active() == True:
            for ring in range(15):
              deg = random.randint(0,359)
              __x = math.cos(deg)*self.currentRad
              __y = math.sin(deg)*self.currentRad
              dot = Dot(self.canvas,__x+self.x,__y+self.y,self.color,True)
              self.dotList.append(dot)
            if self.currentRad >= self.maxRad:
                self.deactivate()

    def add_explosion(canvas,booms,x,y,radius = 80, color="rainbow"):
        boom = random.choice([Explosion(canvas, radius, color), Explosion_gravity(canvas,radius,color)])
        boom.activate(x, y)
        i = 0
        while True:
            l = len(booms)
            if l == 0 or l == i: break
            if (not booms[i].is_active()):
                booms.pop(i)
            else:
                i += 1
        booms.append(boom)



class Explosion_gravity(Explosion):
    def __init__(self,canvas,color='rainbow',maxRad=80):
     super().__init__(canvas)
     self.theta = np.random.randint(0,359, size=(15))
     self.speed = np.random.randint(1,6, size=(15))
     self.maxRad=maxRad
     self.color=color
    
    def next(self): #Change this!!!
           if self.is_active() == True:
             for i in range(len(self.theta)):
              newX = self.speed[i] * math.cos(self.theta[i]) * self.currentRad
              newY = self.speed[i] * math.sin(self.theta[i]) * self.currentRad  + ((.06/2)*self.currentRad**2)
              newDot = Dot(self.canvas,newX+self.x,newY+self.y,self.color,True)
              self.dotList.append(newDot)
             if self.currentRad >= self.maxRad:
                self.deactivate()
             self.currentRad += 1

    def add_explosion(canvas,booms,x,y,radius = 80, color="rainbow", pixInc = 5):
        boom = Explosion_gravity(canvas)
        boom.activate(x, y)
        i = 0
        while True:
            l = len(booms)
            if l == 0 or l == i: break
            if (not booms[i].is_active()):
                booms.pop(i)
            else:
                i += 1
        booms.append(boom)
      














        
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
        root.bind("<Up>",lambda e:Explosion_gravity.add_explosion(canvas,booms,e.x,e.y,'rainbow',80) )
        
        ############################################
        ####### start simulation
        ############################################
        
        while True:
            # scan booms list and execute next time step
            for boom in booms:
                boom.next()
                
            # check active status of list of booms (for debugging)
           # for b in booms:
                #print(b.is_active(),end=" ")
           # print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

