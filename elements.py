import input
import os
import time
from colorama import init, Fore, Back, Style
import numpy as np
import screen
import utils
import random

class element():
    #element is 2d array, can be ball or paddle
    def __init__(self, element, x , y):
        self.x_coordinate = x
        self.y_coordinate = y
        self._height=len(element)
        self._width=len(element[0])
        self._shape=element #shape of paddle and ball

    def change_x(self,x):
        #collision with left wall
        if self.x_coordinate<=2:
            self.x_coordinate=3
        #collision with right wall
        elif self.x_coordinate>=98-self._width:
            self.x_coordinate=97-self._width 
        else: 
            self.x_coordinate += x

    def change_y(self,y):
        if self.y_coordinate<=1:
            self.y_coordinate=1
        elif self.y_coordinate>=29:
            self._minus+=1    
        else: 
            self.y_coordinate+=y

    def get_y(self):
        return self.y_coordinate
    def get_x(self):
        return self.x_coordinate

    def print_element(self):
        #shrink paddle
        if utils.power1.active == 1:
            paddle2=[['=',"=","="],[' ','=',' ']]
            self.clear()
            utils.the_paddle._width=3
            utils.the_paddle._len=3
            self._shape=paddle2
        #expand paddle
        elif utils.power.active == 1:
            paddle1=[['=',"=",'=','=','=',"=","="],[' ',"=","=","=",'=','=',' ']]
            self.clear()
            utils.the_paddle._width=7
            utils.the_paddle._len=7
            self._shape=paddle1
        elif utils.power5.active == 1:
            paddle4=[['T','=','=',"=","T"],[' ','=','=','=',' ']]
            self.clear()
            utils.the_paddle._width=5
            utils.the_paddle._len=5
            self._shape=paddle4    
        else:
            paddle3=[['=','=','=',"=","="],[' ','=','=','=',' ']]
            self.clear()
            utils.the_paddle._width=5
            utils.the_paddle._len=5
            self._shape=paddle3    


        for i in range(self._width):
            for j in range(self._height):
                utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=self._shape[j][i]        

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                utils.the_screen._grid[j+self.y_coordinate][i+ self.x_coordinate]=" "

#polymorhpism
class Paddle(element):
    def __init__(self,ele,x,y,leng):
        self._len=leng
        super().__init__(ele,x,y)



class Ball(element):
    def __init__(self,ele,x,y,lives):
        self._currentlives=lives
        self.x_vel=0
        self.y_vel=1
        self.start=0
        super().__init__(ele,x,y)

    def xvel(self):
        return self.x_vel

    def yvel(self):
        return self.y_vel    

    def shoot(self):
        self.start=1

    def start(self):
        return self.start

    def resetlives(self):
        self._currentlives=5

    def declives(self,lif):
        self._currentlives-=lif        

    def getlives(self):
        return self._currentlives    

    def withwall(self):
        if self.x_coordinate<=1 or self.x_coordinate>=98:
            self.x_vel =self.x_vel*-1
        elif self.y_coordinate<=1:
            self.y_vel =self.y_vel*-1
            #with bottom wall
        elif self.y_coordinate>=29:
            self._currentlives-=1
            if self._currentlives>0:
            #start on paddle 
                self.x_vel=0
                self.y_vel=1 
                self.x_coordinate=95+self.x_vel
                self.x_coordinate=utils.the_paddle.get_x()+3
                self.y_coordinate=utils.the_paddle.get_y()-1
                self.start=0

    def withbrick(self):
        for i in range(30):
            if self.x_coordinate==utils.the_ball.get_x()+i and self.y_coordinate==utils.the_ball.get_y():            
                utils.the_screen._grid[self.y_coordinate][self.x_coordinate]="m"


    def withpaddle(self):
        #on first star
        for i in range(utils.the_paddle._len):
            if self.x_coordinate==utils.the_paddle.get_x()+i and self.y_coordinate==26:
                fallingbricks()
                self.y_vel*=-1
                if utils.the_paddle._len == 5:
                    self.x_vel+=(-2+i)
                elif utils.the_paddle._len == 3:
                    self.x_vel+=(-1+i)
                elif utils.the_paddle._len == 7:
                    self.x_vel+=(-3+i)
                if utils.power3.active==1:
                    utils.the_ball.start=0
                       
                #print("yes")

    def static_ball(self):
        
        self.x_coordinate=utils.the_paddle.get_x()+2
        self.y_coordinate=utils.the_paddle.get_y()-1
        for i in range(self._width):
            for j in range(self._height):
                utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=self._shape[j][i]            
              
    def print_element(self):
        if utils.power2.active==1:
            if self.x_vel>=0:
                self.x_vel+=1
            else:
                self.x_vel-=1
            utils.power2.active=2
                   
        self.x_coordinate +=self.x_vel
        if self.x_coordinate<1:
            self.x_coordinate=4+self.x_vel
        #collision with right wall
        elif self.x_coordinate>98:
            if self.x_vel>3:
                    self.x_vel=3
            elif self.x_vel<-3:
                    self.x_vel=-3
            self.x_coordinate=95+self.x_vel        
        #since we are going from botton to top
        self.y_coordinate -=self.y_vel
        if self.y_coordinate<1:
            self.y_coordinate=1-self.y_vel

        self.withwall()
        self.withpaddle()
        #self.withbrick()
        
        #if self.x_coordinate>=99:
            #print(self.x_vel)      
        utils.the_screen._grid[self.y_coordinate][self.x_coordinate]=self._shape[0][0]        


    

class Brick(element):
    def __init__(self,element,x,y,strength):
        super().__init__(element,x,y)     
        self.strength = strength

    def print_element(self):
        for i in range(self._width):
            for j in range(self._height):
                # utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=self._shape[j][i]
                if ((self.x_coordinate,self.y_coordinate) in utils.sidebricks) and self.strength > 0:
                    utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=" "
                    self.strength=0
                else:     
                    if self.strength > 0:
                        if self.strength == 1:
                            utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=( Fore.BLUE + self._shape[j][i])  
                        if self.strength == 2:
                            utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=( Fore.GREEN + self._shape[j][i])  
                        if self.strength == 3:
                            utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=( Fore.RED + self._shape[j][i])  
                        if self.strength == np.inf:
                            utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=( Fore.WHITE + self._shape[j][i])  
                    else:
                        utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=' '  

    def collisionballandbrick(self):
        if utils.the_ball.y_coordinate == self.y_coordinate and utils.the_ball.x_coordinate == self.x_coordinate :
            if self.strength > 0:
                utils.the_ball.y_vel *= -1
                if self.strength != np.inf:
                    utils.the_screen.score(1)
                self.strength -= 1
                if utils.power6.active==1:
                    utils.the_screen.score(10)
                    xco=self.x_coordinate
                    yco=self.y_coordinate
                    templist=[(xco-1,yco+1),(xco-1,yco),(xco,yco),(xco+1,yco),(xco+1,yco+1),(xco-1,yco-1),(xco+1,yco-1),(xco,yco+1),(xco,yco-1)]
                    for i in templist:
                        utils.sidebricks.append(i)



class RainbowBrick(element):
    def __init__(self,element,x,y,strength):
        super().__init__(element,x,y)     
        self.strength = strength
        self.collided = 0

    def print_element(self):
        for i in range(self._width):
            for j in range(self._height):
                # utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=self._shape[j][i]
                if (self.x_coordinate,self.y_coordinate) in utils.sidebricks and self.strength >0:
                    utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=" "
                    self.strength=0
                else: 
                    if self.collided==0:
                        self.strength=random.randint(1,3)       
                    if self.strength > 0:
                        if self.strength == 1:
                            utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=( Fore.BLUE + self._shape[j][i])  
                        if self.strength == 2:
                            utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=( Fore.GREEN + self._shape[j][i])  
                        if self.strength == 3:
                            utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=( Fore.RED + self._shape[j][i])  
                        if self.strength == np.inf:
                            utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=( Fore.WHITE + self._shape[j][i])  
                    else:
                        utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=' '  

    def collisionballandbrick(self):
        if (utils.the_ball.y_coordinate == self.y_coordinate and utils.the_ball.x_coordinate == self.x_coordinate) or (utils.bullets.y_coordinate == self.y_coordinate and utils.bullets.x_coordinate == self.x_coordinate):
            if (utils.bullets.y_coordinate == self.y_coordinate and utils.bullets.x_coordinate == self.x_coordinate):
                utils.bullets.y_vel=0
                utils.bullets._shape=" "
            if self.strength > 0:
                self.collided=1
                utils.the_ball.y_vel *= -1
                if self.strength != np.inf:
                    utils.the_screen.score(1)
                self.strength -= 1
                if utils.power6.active==1:
                    utils.the_screen.score(10)
                    xco=self.x_coordinate
                    yco=self.y_coordinate
                    templist=[(xco-1,yco+1),(xco-1,yco),(xco,yco),(xco+1,yco),(xco+1,yco+1),(xco-1,yco-1),(xco+1,yco-1),(xco,yco+1),(xco,yco-1)]
                    for i in templist:
                        utils.sidebricks.append(i)

                


class ufo(element):
    def __init__(self,ele,x,y,leng):
        self._len=leng
        self.health=30
        super().__init__(ele,x,y)

    def gethealth(self):
        return self.health


        
    def withball(self):
        #on first star
        for i in range(utils.the_ufo._len):
            if self.x_coordinate+i==utils.the_ball.get_x() and utils.the_ball.get_y()==5:
                #print(Back.WHITE + "hit")
                utils.the_ball.y_vel*=-1
                self.health-=1
                if self.health == 25:
                    mylist=[1,2,3]
                    for i in range(10,80):
                        utils.brick6.append(Brick(utils.testbrick,i+5,10,random.choices(mylist,weights = [2,3,2], k = 1)[0]))
                    utils.allnbricks.append(utils.brick6)
                if self.health == 20:
                    mylist=[1,2,3]
                    for i in range(10,80):
                        utils.brick7.append(Brick(utils.testbrick,i+5,11,random.choices(mylist,weights = [2,2,2], k = 1)[0]))
                    utils.allnbricks.append(utils.brick7)    
            #produce bricks
                    
                # if utils.the_paddle._len == 5:
                #     self.x_vel+=(-2+i)
                # elif utils.the_paddle._len == 3:
                #     self.x_vel+=(-1+i)
                # elif utils.the_paddle._len == 7:
                #     self.x_vel+=(-3+i)
                # if utils.power3.active==1:
                #     utils.the_ball.start=0
    def print_element(self):
        self.withball()
        self.x_coordinate = utils.the_paddle.get_x()
        for i in range(self._width):
            for j in range(self._height):
                utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=self._shape[j][i]   

class Bomb(element):
    def __init__(self,element,x,y):
        super().__init__(element,x,y)   

    def setshoot(self):
        self.x_coordinate=utils.the_ufo.get_x()
        self.y_coordinate=utils.the_ufo.get_y()
        self.x_vel=0
        self.y_vel=1
             

    def print_element(self):
        self.y_coordinate+=self.y_vel
        self.with_paddle()
        for i in range(self._width):
            for j in range(self._height):
                if self.y_coordinate <=26:
                    utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=self._shape[j][i]
                else:    
                    self.y_vel=0
                    utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=" "     
    def with_paddle(self):
        for i in range(utils.the_paddle._len):
            if self.x_coordinate==utils.the_paddle.get_x()+i and self.y_coordinate ==26:
                os.system('aplay -q ./boss.mp3&')
                utils.the_ball.declives(1)
                
class Bullets(element):
    def __init__(self,element,x,y):
        self.y_vel=0
        super().__init__(element,x,y)   

    def setshoot(self):
        self.x_coordinate=utils.the_paddle.get_x()
        self.y_coordinate=utils.the_paddle.get_y()
        self.x_vel=0
        self.y_vel=1
             

    def print_element(self):
        self.y_coordinate-=self.y_vel
        
        for i in range(self._width):
            for j in range(self._height):
                if self.y_coordinate <=26 and self.y_coordinate >1:
                    utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=self._shape[j][i]
                else:    
                    self.y_vel=0
                    utils.the_screen._grid[j+self.y_coordinate][i+self.x_coordinate]=" "     
                 




def fallingbricks():
    timeup = utils.the_screen.gettime()     
    for j in utils.allbricks:
        for i in j:
            i.clear()
            if i.y_coordinate >= 25 or i.y_coordinate <=0:
                utils.feltdown=1
            else:
                
                if timeup > 10 and utils.level==0:
                    i.y_coordinate+=1  
                elif  timeup > 15 and utils.level==1:
                    i.y_coordinate+=1
                elif  timeup > 20 and utils.level==2:
                    i.y_coordinate+=1
                   
                #should see for level3
                elif timeup > 25 and utils.level ==3:
                    i.y_coordinate+=1
    if (timeup > 10 and utils.level==0) or (timeup > 15 and utils.level==1) or (timeup > 20 and utils.level==2) or(timeup > 25 and utils.level ==3):
        utils.sidebricks=[]
        utils.power.powersdown()   
        utils.power1.powersdown()
        utils.power2.powersdown() 
        utils.power3.powersdown() 
        utils.power4.powersdown()
        utils.power5.powersdown()
        utils.power6.powersdown()        
    if utils.level == 3 and timeup > 25:
        for j in utils.allnbricks:
            for i in j:
                i.clear()
                if i.y_coordinate >= 25 or i.y_coordinate <=0:
                    utils.feltdown=1
                else:
                    i.y_coordinate+=1                    


