from tkinter import *
import time
from Explosion import Explosion
from Counter import Counter
from Alien import *


########## global variable
game_over=False

######### Functions

def stop_game():
    global game_over
    game_over=True
    
def shoot(canvas,aliens,booms,ammunition,x,y):
    for a in aliens:
     if a.is_shot(x,y) and a.is_active():
        result="hit!"
        ammunition.increment(a.IPV)
        a.deactivate()
        booms.append(Explosion.add_explosion(canvas,booms,x,y,a.color,30))
    else:
        result="miss!"
        ammunition.increment(-3)
        booms.append(Explosion.add_explosion(canvas,booms,x,y,'white',30))
    print(x,y,result)
    ####### to complete




################
    
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space1.png")
        #my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
     
        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas)
        
        
        #Initialize list of Explosions
        booms=[]
        #Initialize list of Aliens
        aliens=[]
        #Initialize counter ammunition
        ammunition=Counter(canvas,10)

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(canvas,aliens,booms,ammunition,e.x,e.y))
        root.bind("<Escape>",lambda e:stop_game())

        
        ############################################
        ####### start simulation
        ############################################

        t=0  
        while True:
            if t%10 == 0 :
                Alien.add_alien(canvas,aliens)

            for alien in aliens:
                alien.next()

            for boom in booms:
                 boom.next()

        ### To complete
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t=t+1  




          
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

