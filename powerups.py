import input            #fix bg powerups and ball trajectory by 1 :)
import os
from colorama import init, Fore, Back, Style
import numpy as np
import screen
import utils
import math
import time

class Powerup():
    def __init__(self,ele,types,x,y):
        self._icon=ele
        self._type=types
        self.active=0
        self.x_pos=x
        self.y_pos=y
        self.hit=0 #grabbed 
        self.vel=0
        self.x_vel=0
        self.deactive=0
        self.pypos=y
        self.inlife=0
        self.starttime=0
        self.currenttime=0
    def clear(self):
        utils.the_screen._grid[self.y_pos][self.x_pos]=" " 
        #print(Back.GREEN,self.pypos)   

    def withwall(self):
        if self.x_coordinate+self.x_vel<=1 or self.x_coordinate+self.x_vel>=98:
            self.x_vel =self.x_vel*-1
        elif self.y_coordinate+self.y_vel<=1:
            self.y_vel =self.y_vel*-1
            #with bottom wall
    

    def print_powerup(self):
        self.currenttime=time.time()
        self.ballcollision()
        self.pypos=self.y_pos
        self.y_pos+=self.vel
        #self.x_pos+=self.x_vel
        self.paddlecollision()
        if self.hit==1 or self.hit==2:
            utils.remtime= 35 - int(self.currenttime - self.starttime)
            pos=27
            if self.inlife == utils.the_ball.getlives() and self.currenttime - self.starttime <= 35 :
                if self.hit==1:
                    #utils.the_screen.score(10)
                    self.powerupact(self._type)
                self.hit=2    
            else:
                #utils.the_screen.score(-5)
                self.powerupdeact(self._type)
                self.hit=3
        else:
            pos=29   
        if self.y_pos<pos :
            utils.the_screen._grid[self.pypos][self.x_pos]=" " 
            utils.the_screen._grid[self.y_pos][self.x_pos]=self._icon
            if self.y_pos==28:
                utils.the_screen._grid[self.y_pos][self.x_pos]=" "

    def ballcollision(self):
        if utils.the_ball.get_x()==self.x_pos and utils.the_ball.get_y()==self.y_pos:
            self.y_pos-=5
            self.vel=1
            self.x_vel=utils.the_ball.x_vel
            self.x_pos+=self.x_vel
            

    def paddlecollision(self):
        for i in range(5):
            if self.x_pos==utils.the_paddle.get_x()+i and self.y_pos==utils.the_paddle.get_y():
                #activate powerup based on type
                #get current life
                os.system('aplay -q ./sound/powerclaim.wav&')
                self.starttime=time.time()
                self.inlife=utils.the_ball.getlives()
                self.hit=1
                self._icon=" "
             
    def powerupact(self,typee):
        self.active=1
        if typee==1:
            utils.the_screen.poweru="EXPAND PADDLE"
        elif typee==2:
            utils.the_screen.poweru="SHRINK PADDLE"
        elif typee==3:
            utils.the_screen.poweru="FAST BALL"
        elif typee==4:
            utils.the_screen.poweru="PADDLE GRAB"
        elif typee==5:
            utils.the_screen.poweru="THROUGH BALL"
        elif typee==6:        
            utils.the_screen.poweru="SHOOTING PADDLE"
        elif typee==7:
            utils.the_screen.poweru="FIREBALL"

    def powerupdeact(self,typee):
        utils.remtime=0
        self.active=0
        self.deactive=1
        utils.the_screen.poweru=" "    


    def powersdown(self):
        if self.active==0:
            self.y_pos+=1


       