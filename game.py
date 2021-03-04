import input
import os
import time

#utils has screen and elements
import utils
from colorama import Fore,Back,Style

#general info q to quit , a to left ,d to right (for paddle)
#this would be the main file , so check it 

if __name__ == "__main__":
    #get input
    inp= input.Get()
    start=time.time()
    prin=0
    while(1):
        if utils.the_ball.getlives()==0:
            os.system('clear')
            print(Fore.RED+"GAME ENDED")
            print(Fore.YELLOW + "YOU LOST :(")
            print(Fore.GREEN+"YOUR SCORE",utils.the_screen.getscore())
            break

        inpt=input.input_to(inp)
        os.system('clear')
        #prints paddle and screen

        #utils.check()
        utils.the_ball.clear()
        utils.the_paddle.print_element()
        utils.bluebrick.print_brick()
        utils.redbrick.print_brick()
        utils.greenbrick.print_brick()
        utils.rockbrick1.print_brick()
        utils.rockbrick2.print_brick()
        utils.rockbrick3.print_brick()
        utils.rockbrick4.print_brick()
        utils.rockbrick5.print_brick()
        utils.rockbrick6.print_brick()
        utils.rockbrick7.print_brick()
        utils.expbricks1.print_brick()
        utils.expbricks2.print_brick()
        #shoot the ball
      
        if inpt == 's' or inpt =='S':
            utils.the_ball.shoot()
        if utils.the_ball.start == 1:
            utils.the_ball.print_element()
        else:
            utils.the_ball.static_ball()        
        utils.the_screen.print_screen()
        #utils.the_screen1.print_screen()  
       
    

        #controls for game and paddle
        if inpt =='q' or inpt == "Q":
            os.system('clear')
            print(Fore.RED+"GAME TERMINATED")
            print(Fore.YELLOW+"YOUR SCORE : " , utils.the_screen.getscore())
            break
        elif inpt == 'a' or inpt == "A":
            utils.the_paddle.clear()
            utils.the_paddle.change_x(-1)

        elif inpt == 'd' or inpt == "D":
            utils.the_paddle.clear()
            utils.the_paddle.change_x(1)

        #time
        current=time.time()
        utils.the_screen._time=int(current-start) 

        #powerups 
        utils.power.print_powerup()  
        utils.power1.print_powerup()
        utils.power2.print_powerup()
        utils.power3.print_powerup()
        utils.power4.print_powerup()

        #win
        if utils.the_screen.getscore() >=230:
            os.system('clear')
            print(Fore.GREEN+"YOU WON :)")
            print(Fore.YELLOW+"YOUR SCORE : " , utils.the_screen.getscore())
            break

              
else:
    print("you are running a wrong file")    

