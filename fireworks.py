from tkinter import *
import time,random
from Explosion import Explosion
from Missile import Missile

        
       
def main(): 
       
        ##### create a window, canvas 
        colors = ["red", "green", "blue", "yellow", "orange", "purple"]
        root = Tk() # instantiate a tkinter window
        
        my_image=PhotoImage(file="umass_campus.png")
        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h) # create a canvas width*height

        canvas.create_image(10,10,anchor=NW,image=my_image)
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Explosions
        booms=[]
        #Initialize list of Missiles
        missiles=[]
        

        
        ############################################
        ####### start simulation
        ############################################
        t=0  
        while True:
            if t%50 == 0 :
                color = random.choice(colors)
                x = random.randint(0,w)
                mHeight = random.randint(0,h)
                pixInc = random.randint(2,7)
                Missile.add_missile(canvas,missiles,mHeight,x,pixInc,color)


            for m in missiles:
                
                m.next()
                if m.is_active() == False:
                   Explosion.add_explosion(canvas,booms,canvas.coords(m.missile)[0]+4,canvas.coords(m.missile)[1]+12.5,'rainbow',80)
                   canvas.delete(m.missile)
                   missiles.pop(missiles.index(m))
                
            for b in booms:
                b.next()






        ### To complete
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t=t+1  






        

if __name__=="__main__":
    main()

