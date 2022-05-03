from tkinter import *
import time
from Alien import *
from Explosion import Explosion
from SpaceShip import SpaceShip
from Counter import Counter
from Missile import Missile


        
########## global variable
game_over=False

######### Function
def stop_game(canvas,counter):
    global game_over
    game_over=True
    counter.increment('reset')
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,text='GAME OVER',fill='orange',font=('courier',50))

def shoot(canvas,color,aliens,booms,counter,xStart,xEnd,yStart,yEnd):
  if game_over != True:
   shot = False
   for a in aliens:
    if a.is_active():
     if a.is_shot((xStart+xEnd)/2,yStart) or a.is_shot((xStart),yEnd) or a.is_shot((xEnd),yEnd):
        counter.increment(a.IPV)
        if color == 'alien':
            record[a.id] += 1
            Explosion.add_explosion(canvas,booms,(xStart+xEnd)/2,(yStart+yEnd)/2,a.color,30) 
        else:
            Explosion.add_explosion(canvas,booms,(xStart+xEnd)/2,(yStart+yEnd)/2,'rainbow',50) 
        a.deactivate()
        aliens.pop(aliens.index(a))
        return True
   if shot == False:
        return False
    

    
def main():
    ##### Dictionary
    global record 
    record = {Alien_red.id: 0, Alien_green.id: 0, Alien_blue.id: 0}
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)
    aliens=[]
    missiles=[]
    booms=[]
    counter = Counter(canvas,createLives=True)
    ship=SpaceShip(canvas)
    ship.activate()
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())
    root.bind("<Up>",lambda e:Missile.add_missile(canvas,missiles,ship.xLoc,ship.image.height(),0,5,'orange',stop=game_over))  
    root.bind("<Escape>",lambda e:stop_game(canvas,counter)) 

    #### to complete

    t=0  
    while True:

        if t%10 == 0:
            Alien_red.add_alien(canvas,aliens)

        for alien in aliens:
            if alien.is_active:
                 alien.next()
            else:
                alien.deactivate()
                aliens.pop(aliens.index(alien))

        for m in missiles:
                __coords = canvas.coords(m.missile)
                m.next()
                if m.is_active():
                 if shoot(canvas,'alien',aliens,booms,counter,__coords[0],__coords[0]+m.mWidth,__coords[1],__coords[1]+m.mHeight):
                     m.deactivate()
                     missiles.pop(missiles.index(m))
        
        for boom in booms:
              if boom.is_active:
                 boom.next()

        if shoot(canvas,'rainbow',aliens,booms,counter,ship.xLoc-ship.image.width()/2,ship.xLoc+ship.image.width()/2,canvas.winfo_height()-ship.image.height(),canvas.winfo_height()-ship.image.height()/2):
                  if len(counter.lives) >= 1:
                   counter.removeLife()
                  
        if len(counter.lives) == 0: #cleaning up screen by explosions and missiles when game ends
            for m in missiles:
                m.deactivate()
            for b in booms:
                b.deactivate()
            stop_game(canvas,counter)
            
        if game_over == True:
                print(record)
                break

        root.update()   # update the graphic (redraw)
        time.sleep(0.01)  # wait 0.01 second  
        t=t+1

    root.mainloop()
if __name__=="__main__":
    main()

