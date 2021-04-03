import input
import os
from colorama import  Fore, Back, Style
import numpy as np
import utils

class Screen():
    def __init__(self,height,width):
        self._height=height
        self._width=width
        self._grid=[[" "for i in range(self._width)] for j in range(self._height)]
        self.upperwall()
        self.lowerwall()
        self.sidewalls()
        self._score=0
        self._time=0
        self.poweru=" "
        
        #print(self._grid.shape)

    def clear(self):
        self._grid=[[" "for i in range(self._width)] for j in range(self._height)] 
    def score(self,s):
        self._score +=s

    def gettime(self):
        return self._time

    def settime(self,tim):
        self._time=tim

    def getscore(self):
        return self._score 

    def getpixel(self,x,y):
        return self._grid[y][x]            

    def upperwall(self):
        for i in range(self._width):
            self._grid[0][i]="#"
    def lowerwall(self):
        for i in range(self._width):
            self._grid[self._height-1][i]="#"

    def sidewalls(self):
        for i in range(self._height):
            self._grid[i][0]="#"
            self._grid[i][self._width-1]="#"  

    def print_screen(self):
        print (Fore.YELLOW + "CONTROLS  : q-quit a-left d-right s-shoot")
        print(Fore.WHITE+"Powerups are lost if life is lost or 15 seconds are passed")
        print(Fore.GREEN + "LIVES",utils.the_ball._currentlives ,"           ","SCORE:",self._score,"                   ","TIME:",self.gettime())
        print("POWERUP: ",self.poweru,"             ","TIME REMAINING : ",utils.remtime)
        print("LEVEL: ",utils.level)
        if utils.level==3:
            print("UFO HEALTH : ",utils.the_ufo.gethealth())        
        for i in range(self._height):
            k=[]
            for j in range(self._width):
                k.append(Fore.BLUE + self._grid[i][j] + Style.RESET_ALL)
                     
            print(Fore.BLUE+''.join(k)+Style.RESET_ALL)

#s1=Screen(30,100)
#s1.print_screen      
