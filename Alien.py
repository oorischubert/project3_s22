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

    
    def activate(self):
        self.aLoc = 0
        self._active = True
        self.x=random.randint(0,self.canvas.winfo_width()-self.aWidth)
        self.y=0
        self.rect = self.canvas.create_rectangle(self.x,self.y,self.x+self.aWidth,self.y+self.aHeight,outline=self.color,fill=self.color)
    
    def deactivate(self):
        self._active=False
        self.canvas.delete(self.rect) #necessary?
    
    def is_active(self):
        return self._active
    
    def next(self):
        self.aLoc += self.pixInc
        if self.aLoc >= self.canvas.winfo_height() + self.aHeight/2:
            self.deactivate()
        if self._active == True:
            self.canvas.move(self.rect,0,self.pixInc)
     
        
################################################################
################################################################

class Alien_red(Alien):
    id='red'
    def __init__(self,canvas):
        super().__init__(canvas) #init parent class!
        self.image=PhotoImage(file="alien_red.png")  # keep a reference (avoid garbage collector)
        self.width=self.image.width()
        self.height=self.image.height()
        self.IPV=2
        self.canvas=canvas
        self.aWidth=self.width
        self.aHeight=self.height
        self.color = 'red'
    
    def activate(self):
        self.aLoc = 0
        self.x=random.randint(0+self.width/2,self.canvas.winfo_width()-self.width/2)
        self.y=0
        self.rect=self.canvas.create_image(self.x,self.y,anchor=CENTER,image=self.image)
        self._active = True

    def is_shot(self,x0,y0):
        _coords = self.canvas.coords(self.rect)
        if (_coords[0]-self.width/2<= x0 <= _coords[0]+self.width/2) and (_coords[1]-self.height/2 <= y0 <= _coords[1]+self.height/2):
            return True
        else:
            return False

    def add_alien(canvas,aliens):
      alien = random.choice([Alien_red(canvas),Alien_green(canvas),Alien_blue(canvas),Alien_mine(canvas)])
      alien.activate()
      i = 0
      while True:
            l = len(aliens)
            if l == 0 or l == i: break
            if (not aliens[i].is_active()):
                aliens.pop(i)
            else:
                i += 1
      aliens.append(alien)
###############################################################
###############################################################

class Alien_green(Alien_red):
   id='green'
   def __init__(self,canvas):
        Alien.__init__(self,canvas)
        super().__init__(self)
        self.canvas=canvas
        self.image=PhotoImage(file="alien_green.png")
        self.color = 'green'
        self.IPV = 4
    

   def next(self):
      self.aLoc += self.pixInc
      if self.aLoc >= self.canvas.winfo_height() + self.aHeight/2:
            self.deactivate()
      if self._active == True:
            wiggle=random.randint(-5,5)
            _coords = self.canvas.coords(self.rect)
            if _coords[0] + wiggle <= 0 + self.width/2 or _coords[0] + wiggle >= self.canvas.winfo_width() - self.width/2:
             wiggle=0
            self.canvas.move(self.rect,wiggle,self.pixInc)




    # to complete



###############################################################
###############################################################
                


class Alien_blue(Alien_red):
    id='blue'
    def __init__(self,canvas):
        Alien.__init__(self,canvas)
        super().__init__(self)
        self.canvas=canvas
        self.image=PhotoImage(file="alien_blue.png")
        self.color = 'blue'
        self.angle=random.randint(-160,-20)
        self.bouncer=1
        self.IPV = 3


    def next(self):
        self.aLoc += self.pixInc
        if self.aLoc >= self.canvas.winfo_height() + self.aHeight/2:
            self.deactivate()
        if self._active == True:
            _coords = self.canvas.coords(self.rect)
            if _coords[0] <= 0 + self.width/2 or _coords[0] >= self.canvas.winfo_width() - self.width/2:
              self.bouncer = self.bouncer*-1
            self.canvas.move(self.rect,self.bouncer*self.pixInc*math.sin(self.angle),self.pixInc)

class Alien_mine(Alien_red):
   id='yellow'
   def __init__(self,canvas):
        Alien.__init__(self,canvas)
        super().__init__(self)
        self.teleTick = 0
        self.canvas=canvas
        self.image=PhotoImage(file="alienship.png")
        self.color='yellow'
        self.IPV = 5

   def next(self):
      self.aLoc += self.pixInc
      self.teleTick += self.pixInc
      if self.aLoc >= self.canvas.winfo_height() + self.aHeight/2:
            self.deactivate()
      if self._active == True:
            if self.teleTick >=100:
             wiggle=random.choice([-75,75])
             self.teleTick=0
            else:
              wiggle=0
            _coords = self.canvas.coords(self.rect)
            if _coords[0] + wiggle <= 0 + self.width/2 or _coords[0] + wiggle >= self.canvas.winfo_width() - self.width/2:
             wiggle=0
            self.canvas.move(self.rect,wiggle,self.pixInc)
            
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
        #alien=Alien(canvas)
        #alien=Alien_red(canvas)
        #alien=Alien_green(canvas)
        #alien=Alien_blue(canvas)
        alien=Alien_mine(canvas)

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

