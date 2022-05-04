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
  result='miss'
  shot = False
  if game_over != True:
   for a in aliens:
    if a.is_active():
     if a.is_shot(x,y):
        result="hit!"
        ammunition.increment(a.IPV)
        record[a.id] += 1
        Explosion.add_explosion(canvas,booms,x,y,a.color,30)
        shot = True
        a.deactivate()
        aliens.pop(aliens.index(a))
   if shot == False:
        result="miss!"
        ammunition.increment(-3)
        Explosion.add_explosion(canvas,booms,x,y,'white',30)
   print(x,y,result)
    ####### to complete




################
    
def main(): 
        global record 
        record = {Alien_red.id: 0, Alien_green.id: 0, Alien_blue.id: 0, Alien_mine.id: 0}
        recordStep=[]
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

            if t%5 == 0:
                Alien_red.add_alien(canvas,aliens)

            for alien in aliens:
                if alien.is_active:
                  alien.next()
                else:
                   alien.deactivate()
                   alien.pop(aliens.index(alien))
                

            for boom in booms:
              if boom.is_active:
                 boom.next()

            if ammunition.count <= 0:
                stop_game()

            if t%100==0:
               currentStep = (record[Alien_red.id],record[Alien_green.id],record[Alien_blue.id],record[Alien_mine.id])
               recordStep.append(currentStep)
            
            if game_over == True:
                ammunition.increment('reset')
                for b in booms: #clean screen of explosions
                   b.deactivate()
                canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,text='GAME OVER',fill='orange',font=('courier',50))
                file=open("game1.txt","w")
                for step in recordStep:
                  file.write(str(step[0])+" "+str(step[1])+" "+str(step[2])+" "+str(step[3])+"\n")
                file.close()
                break

        ### To complete
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t=t+1  




          
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

