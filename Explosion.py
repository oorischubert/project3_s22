from tkinter import *
import math,time,random
from Dot import Dot


class Explosion:
    dotList = []
    #### to complete
    def __init__(self,canvas,color='rainbow',maxRad=80):
        self.color = color
        self.canvas = canvas
        self.maxRad = maxRad
        self.dots = 15
        self.__active = False
        self.dotList = []
    
    def activate(self,x,y):
        self.x = x
        self.y = y
        self.currentRad = 0
        self.__active = True

    def deactivate(self):
      self.canvas.delete(str(self)[19:30])
      print(self)
      self.__active = False
      print('deactivated')

    def is_active(self):
      return self.__active
    
    def next(self):
           self.currentRad = self.currentRad + 1
           if self.is_active() == True:
            for ring in range(15):
              deg = random.randint(1,360)
              __x = math.cos(deg*math.pi/180)*self.currentRad
              __y = math.sin(deg*math.pi/180)*self.currentRad
              dot = Dot(self.canvas,__x+self.x,__y+self.y,self.color,True)
              self.dotList.append(dot)
            if self.currentRad >= self.maxRad:
                self.deactivate()
               
                
   
    def add_explosion(canvas,booms,x,y,color,radius):
      for b in booms:
            if b.is_active() != True:
                booms.pop(booms.index(b))
      newExp = Explosion(canvas,color,radius)
      newExp.activate(x,y)
      newExp.next
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
                print(b.is_active(),end=" ")
            print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

