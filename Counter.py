from tkinter import *

class Counter:
  def __init__(self,canvas,initCount=0):
      self.canvas=canvas
      self.count = initCount
      self.counter = canvas.create_text(self.canvas.winfo_width()-70,20,text=self.count,fill='orange',font=('courier',25))

  def increment(self,inc):
       self.count = self.count + inc
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
 root.mainloop()


 while True:
     root.update()   # update the graphic (redraw)
     
if __name__=="__main__":
    main()



        
