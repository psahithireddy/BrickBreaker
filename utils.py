from screen import *
from elements import *
from colorama import Fore
from bricks import *
from powerups import * 
import random

remtime=0

sidebricks=[]
feltdown=0
level=0
allnbricks=[]
#the_screen1=Screen(30,100)
the_screen=Screen(30,100)
paddle=[['=','=','=',"=","="],[' ','=','=','=',' ']]
the_paddle=Paddle(paddle,3,26,5)
ufo1=[["@","@","@","@","@"],["|","U","U","U","|"]]
the_ufo = ufo(ufo1,3,4,5) 
bombstr=[["!"]]
bomb=Bomb(bombstr,3,4)
#expand paddle
power=Powerup("U",1,34,10)
#shrink paddle
power1=Powerup("V",2,30,10)
#fastball
power2=Powerup("W",3,35,10)
#paddlegrab
power3=Powerup("X",4,32,10)
#through ball
power4=Powerup("Y",5,31,10)

#shooting paddle
power5=Powerup("Z",6,38,10)
power6=Powerup("T",7,20,10)
ball=[["O"]]
the_ball=Ball(ball,3,25,5)#same at paddle position
thebull=[["^"]]
bullets=Bullets(thebull,3,5)
  
global allbricks  
testbrick = [["#"]]
brick1 = []
brick2 = []
brick3 = []
brick4 = []
rainbow = []
allbricks=[brick1,brick2,brick3,brick4,rainbow]
mylist=[1,2,3,np.inf]
for i in range(20,60):
    brick1.append(Brick(testbrick,i+5,10,random.choices(mylist,weights = [3,2,2,1], k = 1)[0]))
    brick2.append(Brick(testbrick,i+5,14,random.choices(mylist,weights = [2,3,2,2], k = 1)[0])) 
    brick3.append(Brick(testbrick,i+5,13,random.choices(mylist,weights = [1,2,3,1], k = 1)[0])) 
    brick4.append(Brick(testbrick,i+5,12,random.choices(mylist,weights = [3,2,3,1], k = 1)[0]))
    rainbow.append(RainbowBrick(testbrick,i+5,16,random.choices(mylist,weights = [3,2,3,1], k = 1)[0]))                  
   
expbricks1=Explodebricks(6,40,9)
expbricks2=Explodebricks(6,60,7)
#bluebrick._ballgrid[0][10]="y"

def buildbricks():

    if utils.level == 1:
        brick1 = []
        brick2 = []
        brick3 = []
        brick4 = []
        rainbow = []
        mylist=[1,2,3,np.inf]
        for i in range(20,60):
            brick1.append(Brick(testbrick,i+5,6,random.choices(mylist,weights = [3,2,2,1], k = 1)[0]))
            brick2.append(Brick(testbrick,i+5,7,random.choices(mylist,weights = [2,3,2,2], k = 1)[0])) 
            brick3.append(Brick(testbrick,i+5,8,random.choices(mylist,weights = [1,2,3,1], k = 1)[0])) 
            brick4.append(Brick(testbrick,i+5,9,random.choices(mylist,weights = [3,2,3,1], k = 1)[0]))
            rainbow.append(RainbowBrick(testbrick,i+5,10,random.choices(mylist,weights = [3,2,3,1], k = 1)[0]))
            rainbow.append(RainbowBrick(testbrick,i+5,5,random.choices(mylist,weights = [3,2,3,1], k = 1)[0]))
        allbricks=[brick1,brick2,brick3,brick4,rainbow] 
        return allbricks

    elif utils.level == 2:
        brick1 = []
        brick2 = []
        brick3 = []
        brick4 = []
        rainbow = []
        mylist=[1,2,3,np.inf]
        for i in range(20,70):
            brick1.append(Brick(testbrick,i+5,10,random.choices(mylist,weights = [3,2,2,1], k = 1)[0]))
            rainbow.append(RainbowBrick(testbrick,i+5,5,random.choices(mylist,weights = [3,2,3,1], k = 1)[0]))
        for i in range(30,60):    
            brick2.append(Brick(testbrick,i+5,7,random.choices(mylist,weights = [2,3,2,2], k = 1)[0])) 
        for i in range(40,50):    
            brick3.append(Brick(testbrick,i+5,8,random.choices(mylist,weights = [1,2,3,1], k = 1)[0])) 
            brick4.append(Brick(testbrick,i+5,9,random.choices(mylist,weights = [3,2,3,1], k = 1)[0]))
            
        allbricks=[brick1,brick2,brick3,brick4,rainbow] 
        return allbricks

    elif utils.level == 3:
        brick1 = []
        global brick6
        brick6=[]
        global brick7
        brick7=[]
        allbricks=[]
        for i in range(20,30):
            brick1.append(Brick(testbrick,i+5,10,np.inf))
        allbricks=[brick1]            
        return allbricks

        
