from tkinter import *

class Counter:
  def __init__(self,canvas,initCount=0,createLives = False):
      self.canvas=canvas
      self.count = initCount
      self.counter = canvas.create_text(self.canvas.winfo_width()-70,20,text=self.count,fill='orange',font=('courier',25))
      self.createLives = createLives
      self.life = PhotoImage(file="ship.png").subsample(3,3)
      self.lives = []
      self.lifeCreator()

  def lifeCreator(self):
   if self.createLives == True:
    xLoc=10
    for i in range(3):
     self.ship=self.canvas.create_image(xLoc,10,anchor=NW,image=self.life)
     xLoc += self.life.width()
     self.lives.append(self.ship)
    
  def removeLife(self):
      if len(self.lives) > 0:
        lives = len(self.lives)-1
        self.canvas.delete(self.lives[lives])
        self.lives.pop(lives)

  def increment(self,inc):
       if inc == 'reset':
           self.canvas.itemconfig(self.counter, text=0)
       else:
        self.count += inc
        self.canvas.itemconfig(self.counter, text=self.count)
       
#########################



def main(): 
    
 root = Tk() # instantiate a tkinter window
        
 my_image=PhotoImage(file="umass_campus.png")
 w=my_image.width()
 h=my_image.height()
 canvas = Canvas(root, width=w,height=h) # create a canvas width*height

 canvas.create_image(10,10,anchor=NW,image=my_image)
 canvas.pack()
 root.update() 
 counter = Counter(canvas,initCount=10)
 root.bind("<Button-1>",lambda e:counter.increment(1))
 root.bind("<Escape>",lambda e:counter.removeLife()) #REMOVE!!!
 root.mainloop()


 while True:
     root.update()   # update the graphic (redraw)
     
if __name__=="__main__":
    main()



        
