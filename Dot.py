########################
## Team Members
## Name1:         
## Name2:
#########################

from tkinter import *
import random


class Dot:
    ##### TO COMPLETE












        
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

