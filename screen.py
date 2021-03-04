import input
import os
from colorama import  Fore, Back, Style
import numpy as np
import utils

class Screen():
    def __init__(self,height,width):
        self._height=height
        self._width=width
        self._grid=np.array([[" "for i in range(self._width)] for j in range(self._height)])
        self.upperwall()
        self.lowerwall()
        self.sidewalls()
        self._score=0
        self._time=0
        self.poweru=" "
        
        #print(self._grid.shape)
    def score(self,s):
        self._score +=s

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
        print(Fore.GREEN + "LIVES",utils.the_ball._currentlives ,"           ","SCORE:",self._score,"                   ","TIME:",self._time)
        print("POWERUP: ",self.poweru)
        for i in range(self._height):
            k=[]
            for j in range(self._width):
                if self._grid[i][j]=="1":
                    k.append(Back.BLUE+ self._grid[i][j] + Style.RESET_ALL)
                elif self._grid[i][j]=="2":
                    k.append(Back.GREEN+ self._grid[i][j] + Style.RESET_ALL)
                elif self._grid[i][j]=="3":    
                    k.append(Back.RED+ self._grid[i][j] + Style.RESET_ALL)
                #elif self._grid[i][j]=="U" or self._grid[i][j]=="V" or self._grid[i][j]=="W" or self._grid[i][j]=="X" or self._grid[i][j]=="Y": 
                    #k.append(Back.YELLOW+ self._grid[i][j] + Style.RESET_ALL)    
                elif self._grid[i][j]=="#":
                    k.append(Back.WHITE+ self._grid[i][j] + Style.RESET_ALL)                          
                else:
                    k.append(Fore.BLUE + self._grid[i][j] + Style.RESET_ALL)
                     
            print(Fore.BLUE+''.join(k)+Style.RESET_ALL)

#s1=Screen(30,100)
#s1.print_screen      
