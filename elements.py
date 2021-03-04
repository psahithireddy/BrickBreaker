import input
import os
from colorama import init, Fore, Back, Style
import numpy as np
import screen
import utils


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


    


                                       

                

