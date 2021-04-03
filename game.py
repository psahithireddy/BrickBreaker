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

    def levelup():
        utils.sidebricks=[]
        utils.the_ball.start=0
        utils.the_ball.clear()
        utils.the_ball.static_ball()
        utils.the_ball.resetlives()
        global start1
        start1=time.time()
        #print(Back.RED+"HI")
        for j in utils.allbricks:
            for i in j:
                i.clear()
               
        utils.allbricks=utils.buildbricks()


    while(1):
        if utils.the_ball.getlives()==0 or utils.level>3 or utils.feltdown == 1:
            os.system('clear')
            os.system('aplay -q ./sound/gameover.wav&')
            print(Fore.RED+"GAME ENDED")
            print(Fore.YELLOW + "YOU LOST :(")
            print(Fore.GREEN+"YOUR SCORE",utils.the_screen.getscore())
            break

        inpt=input.input_to(inp)
        os.system('clear')
        #prints paddle and screen
        timed= utils.the_screen.gettime()
        if inpt == 'l' or inpt == "L" or timed > 400:
            utils.level+=1
            if utils.level <= 2:
                os.system('aplay -q ./sound/levelup.wav&')
            if utils.level==3:
                os.system('aplay -q ./sound/bombdrop.wav&')    
            levelup()
        #utils.render()
        utils.the_ball.clear()
        utils.the_paddle.print_element()
        if utils.level == 3:
            utils.the_ufo.clear()
            utils.the_ufo.print_element()
        if utils.level<= 3:    
            for j in utils.allbricks:
                for i in j:
                    i.clear()
                    i.print_element()
                    i.collisionballandbrick()
        # utils.redbrick.print_brick()
        # utils.greenbrick.print_brick()
        # utils.rockbrick1.print_brick()
        # utils.rockbrick2.print_brick()
        # utils.rockbrick3.print_brick()
        # utils.rockbrick4.print_brick()
        # utils.rockbrick5.print_brick()
        # utils.rockbrick6.print_brick() 
        # utils.rockbrick7.print_brick()
        # utils.expbricks1.print_brick()
        # utils.expbricks2.print_brick()
       
        if inpt == 's' or inpt =='S':
            os.system('aplay -q ./sound/mixkit-game-ball-tap-2073.wav&')
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
        if utils.level==0:
            utils.the_screen.settime(int(current-start))
        else:
            utils.the_screen.settime(int(current-start1))

        if utils.the_screen.gettime()%5 == 0 and utils.power5.active==1:
            utils.bullets.setshoot()
            starttime=time.time()
            utils.timrem=int(35-starttime)
            if utils.timrem<0:
                utils.timrem=0
        if utils.power5.active==1:    
            utils.bullets.clear()
            utils.bullets.print_element()    

        if utils.level == 3:
            if utils.the_screen.gettime()%10 == 0:
                utils.bomb.setshoot()  
            utils.bomb.clear()
            utils.bomb.print_element()
            for j in utils.allnbricks:
                for i in j:
                    i.clear()
                    i.print_element()
                    i.collisionballandbrick()     

        #powerups 
        if utils.level <= 2:
            utils.power.print_powerup()  
            utils.power1.print_powerup()
            utils.power2.print_powerup()
            utils.power3.print_powerup()
            utils.power4.print_powerup()
            utils.power5.print_powerup()
            if utils.level !=3:
                utils.power6.print_powerup()

        #win
        if utils.the_screen.getscore() >= 630 or utils.the_ufo.gethealth()<=0:
                os.system('clear')
                print(Fore.GREEN+"YOU WON :)")
                print(Fore.YELLOW+"YOUR SCORE : " , utils.the_screen.getscore())
                break

     
              
else:
    print("you are running a wrong file")    

