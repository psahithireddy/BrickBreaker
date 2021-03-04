from screen import *
from elements import *
from colorama import Fore
from bricks import *
from powerups import * 



#the_screen1=Screen(30,100)
the_screen=Screen(30,100)
paddle=[['=','=','=',"=","="],[' ','=','=','=',' ']]
the_paddle=Paddle(paddle,3,26,5)
#expand paddle
power=Powerup("U",1,29,10)
#shrink paddle
power1=Powerup("V",2,30,10)
#fastball
power2=Powerup("W",3,31,10)
#paddlegrab
power3=Powerup("X",4,32,10)
#through ball
power4=Powerup("Y",5,33,10)

    


ball=[["O"]]

the_ball=Ball(ball,3,25,5)#same at paddle position

bluebrick=Bluebricks(50,1)

redbrick=Redbricks(54,3)

greenbrick=Greenbricks(52,2)

expbricks1=Explodebricks(6,40,9)
expbricks2=Explodebricks(6,60,7)
#bluebrick._ballgrid[0][10]="y"
rockbrick1=Rockbricks(5,28,6,'#')
rockbrick2=Rockbricks(5,32,8,'#')
rockbrick3=Rockbricks(5,38,8,'#')
rockbrick4=Rockbricks(5,31,8,'#')
rockbrick5=Rockbricks(5,36,8,'#')
rockbrick6=Rockbricks(5,30,6,'#')
rockbrick7=Rockbricks(5,40,6,'#')