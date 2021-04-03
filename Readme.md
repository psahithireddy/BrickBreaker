# Readme

To start the game

 - pip3 install colorama
 - pip3 install numpy
 - run python3 game.py


## GAME GUIDE

### ABOUT THE GAME
There are bricks of various colours, each color has represents different block values, there are stone bricks which can't be broken , and there are exploding bricks.Goal of the game is to hit all the bricks, with ball, by moving the paddle.If ball misses the paddle and touches the ground life is lost.There are 5 lives.There are some powerups which are hidden inside bricks, if you grab powerup with paddle you will have some bonus functionality which helps you to break the bricks.There are 4 levels in this game. Last elevl has ufo, you need to kill ufo to win.Ufo drops bombs occasionally.If bomb hits the paddle you lose a life

If the bluebricks are hit you get 1 point , redbricks gives 2, greenbricks gives 3 and exploding bricks breaks all the nearby bricks , whereas stone bricks can't be broken.

You lose the powerup if you lose the current life or 20 seconds is passed.

### CONTROLS
 S -Shoot the ball
 A -move paddle to left
 D -move paddle to right
 Q -Quit the game
 
 -controls are not  case sensitive



## CLASSES
### Screen
   Used this class to create an object called  `the_screen` which has an attribute called grid, which is 2d array and basically our game screen.
### Element
   This class has two elements of the game, paddle and ball as its sub-classes ,the objects `the_paddle` and `the_ball` ,`bullets` ,`bomb` ,`brick`  are created using these subclasses.
   
### Powerup
   This class is used by all the 5 powerups, exploting its attributes to implement the functionality.
   The 5 powerups implemented are:
   ```
-- Expand Paddle
-- Shrink Paddle
-- Through Ball
-- Fast Ball
-- Paddle Grab
-- Fireball
-- Shooting paddle
```


## Object Oriented Concepts
This is a terminal based game written in python3 using oops concepts,inspired from the old classic brick breaker.

### Inheritance
1. Class `Brick`  is the parent class and Bluebrick , Redbrick, Greenbrick , Rockbrick and Explodingbrick inherit the properties of the 'Brick' class -  bricks.py 

2. Class `element` is the parent class and Paddle , Ball inherits properities of this class. - elements.py 

### Abstraction
Methods like `the_ball.get_x()`,`the_ball.get_y()`,`the_ball.shoot()`,
`the_screen.score()` abstract away the details and make the code more readable and organised.

### Encapsulation
 All the functionality is implemented in Class and object based approach 

### Polymorphism
In `element`, method `print_element` in parent class is overridden by childclass `Ball` -elements.py