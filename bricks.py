import input
import os
from colorama import init, Fore, Back, Style
import numpy as np
import screen
import utils
import math
#-1 for non breakingbrick,1
class Bricks():
    def __init__(self,ele,val,x,y,count):
        self._element=ele
        self.x_pos=x
        self.y_pos=y
        self._count=count
        self._val=val
        self._ballgrid=[[self._val for i in range (self._count)]for j in range (1)]   
        self.hit=0  

    def print_brick(self):
        self.collision()
        for i in range(self._count):
                if self._ballgrid[0][i]=="m" and self._element!= "#":
                    utils.the_screen._grid[self.y_pos][self.x_pos+i]=" "
                else:
                    if self._element != "#":      
                        utils.the_screen._grid[self.y_pos][self.x_pos+i]=self._ballgrid[0][i]
                    else:    
                        utils.the_screen._grid[self.y_pos][self.x_pos+i]=self._element
                        self.hit=0

    def collision(self):

        for i in range (self._count):
            #collision
            if utils.the_ball.get_x() == self.x_pos+i and utils.the_ball.get_y() == self.y_pos:
                #if already broke or not
                if self._ballgrid[0][i]!="m": 
                    #velocity part
                    
                    if utils.the_ball.xvel()!=0:
                        _tan = math.atan(utils.the_ball.yvel()/utils.the_ball.xvel())
                        tan_deg=math.degrees(_tan)
                    else:
                        tan_deg=90
                    if  utils.power4.active==0:
                        if tan_deg<45 and tan_deg>-45 :
                            if i==self._count-1:
                                utils.the_ball.x_vel*=-1
                            elif self._ballgrid[0][i+1]=="m":
                                utils.the_ball.x_vel*=-1
                            else:
                                utils.the_ball.y_vel*=-1          
                        elif (tan_deg>135 and tan_deg<=180) or(tan_deg>=-180 and tan_deg<-135):
                            if i==0:
                                utils.the_ball.x_vel*=-1
                            elif self._ballgrid[0][i-1]=="m":
                                utils.the_ball.x_vel*=-1
                            else:
                                utils.the_ball.y_vel*=-1
                                
                        else:            
                            utils.the_ball.y_vel*=-1  
                    if  self._element=="B":
                        #print(Back.RED+"yes")
                        for j in range(self._count):
                            for a in range (-1,2):
                                for b in range (-1,2):
                                    if a==-1 and j==0:
                                        if utils.the_screen._grid[self.y_pos+b][self.x_pos+j+a] == "1":
                                            utils.bluebrick.decreasebrick(self.x_pos+j+a,self.y_pos+b,self.x_pos-28+j-1,tan_deg)
                                        elif utils.the_screen._grid[self.y_pos+b][self.x_pos+j+a] =="2":
                                                for f in range(2):
                                                    utils.greenbrick.decreasebrick(self.x_pos+j+a,self.y_pos+b,self.x_pos-27+j-1,tan_deg)
                                        elif utils.the_screen._grid[self.y_pos+b][self.x_pos+j+a] =="3":
                                                for f in range(3):
                                                    utils.redbrick.decreasebrick(self.x_pos+j+a,self.y_pos+b,self.x_pos-26+j-1,tan_deg) 

                                    elif a==1 and j==self._count-1:
                                        if utils.the_screen._grid[self.y_pos+b][self.x_pos+j+a] == "1":
                                            utils.bluebrick.decreasebrick(self.x_pos+j+a,self.y_pos+b,self.x_pos-28+j+1,tan_deg)
                                        elif utils.the_screen._grid[self.y_pos+b][self.x_pos+j+a] =="2":
                                                for f in range(2):
                                                    utils.greenbrick.decreasebrick(self.x_pos+j+a,self.y_pos+b,self.x_pos-27+j+1,tan_deg)
                                        elif utils.the_screen._grid[self.y_pos+b][self.x_pos+j+a] =="3":
                                                for f in range(3):
                                                    utils.redbrick.decreasebrick(self.x_pos+j+a,self.y_pos+b,self.x_pos-26+j+1,tan_deg)                    
                                    elif a!=1 and b!=0:
                                        if a!=-1 and b!=0:
                                            if utils.the_screen._grid[self.y_pos+b][self.x_pos+j+a] == "1":
                                                utils.bluebrick.decreasebrick(self.x_pos+j+a,self.y_pos+b,self.x_pos-28+j,tan_deg)
                                            elif utils.the_screen._grid[self.y_pos+b][self.x_pos+j+a] =="2":
                                                for f in range(2):
                                                    utils.greenbrick.decreasebrick(self.x_pos+j+a,self.y_pos+b,self.x_pos-27+j,tan_deg)
                                            elif utils.the_screen._grid[self.y_pos+b][self.x_pos+j+a] =="3":
                                                for f in range(3):
                                                    utils.redbrick.decreasebrick(self.x_pos+j+a,self.y_pos+b,self.x_pos-26+j,tan_deg)        
                                    elif a==0 and b==0:
                                        self.decreasebrick(self.x_pos+j+a,self.y_pos+b,j,tan_deg)        
                    else:
                        self.decreasebrick(self.x_pos+i,self.y_pos,i,tan_deg)    

                else:
                    if self._element !="#":
                        utils.the_screen._grid[self.y_pos][self.x_pos+i]=" "    
                        self._ballgrid[0][i]="m"
                    #else:
                        #utils.the_ball.y_vel*=-1



    def decreasebrick(self,x,y,i,tan_deg):
       
        if self._element == "#":
            utils.the_screen._grid[y][x]="#"
            self._ballgrid[0][i]="#"
            if utils.power4.active==0:
                if self.hit == 0:
                    if tan_deg<45 and tan_deg>-45:
                        utils.the_ball.x_vel*=-1
                    elif (tan_deg>135 and tan_deg<=180) or(tan_deg>=-180 and tan_deg<-135) :
                        utils.the_ball.x_vel*=-1
                    else:            
                        utils.the_ball.y_vel*=-1 
                    self.hit=1
           
            #print(Back.RED+"yes")
            
        else:
            #utils.the_ball.y_vel*=-1    
            if self._element == 1 and self._ballgrid[0][i] !="m":
                utils.the_screen.score(1)
                self._ballgrid[0][i]="m"
                
            elif self._element == 2 and self._ballgrid[0][i] !="m":
                self._ballgrid[0][i]-=1
                if self._ballgrid[0][i]==0:
                    self._ballgrid[0][i]="m"
                if i!=(31-27) and i!=(36-27)  and i!=(32-27) and i!=(38-27) :  
                    utils.the_screen.score(1)
                else:
                    self._ballgrid[0][i]=-1    
                   
                
            elif self._element == 3 and self._ballgrid[0][i] !="m":
                self._ballgrid[0][i]-=1
                if self._ballgrid[0][i]==0:
                    self._ballgrid[0][i]="m"
                if i!=(30-26) and i!=(40-26)and  i!=(28-26):  
                    utils.the_screen.score(1)
                else:
                    self._ballgrid[0][i]=-1  
            #for each B removes it   
            elif self._element == "B" and self._ballgrid[0][i] !="m":
                self._ballgrid[0][i]="m"           
        
            if self._ballgrid[0][i]!="m":         
                utils.the_screen._grid[y][x]=self._ballgrid[0][i]
            else:
                utils.the_screen._grid[y][x]=" "          
            
                
    
class Bluebricks(Bricks):

    def __init__(self,count,val):
        super().__init__(val,val,28,10,count)

class Greenbricks(Bricks):
    def __init__(self,count,val):
        super().__init__(val,val,27,8,count)

class Redbricks(Bricks):
    def __init__(self,count,val):
        super().__init__(val,val,26,6,count)  

class Rockbricks(Bricks):
    def __init__(self,count,x,y,val):
        super().__init__(val,-1,x,y,1) 

class Explodebricks(Bricks):
    def __init__(self,count,x,y):
        self.typeo=1
        super().__init__("B","B",x,y,count)



        
    

                            
        
        
                      



