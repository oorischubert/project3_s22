########################
## Team Members
## Name1:         
## Name2:
#########################

from tkinter import *
import random

colors = ["red", "green", "blue", "yellow", "white", "orange", "purple"]

class Dot:
    ##### TO COMPLETE
  def __init__(self,canvas,x,y,color,bool=False):
    self.canvas = canvas
    self.x = x
    self.y = y
    self.color = color
    self.finalColor = self.colorPicker()
    self.bool=bool
    canvas.create_oval(self.x-1,self.y-1,self.x+1,self.y+1,outline = self.finalColor, fill = self.finalColor)
   
#if inputted color is rainbow return random color from colors list else return what was inputed
  def colorPicker(self):
      if self.color == 'rainbow':
          return random.choice(colors)
      else:
          return self.color

    











        
#################################################################
#################################################################
def main(): 

     ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        canvas = Canvas(root,width=800,height=1000,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Dot(canvas,e.x,e.y,"rainbow",True))
        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

