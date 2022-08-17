
# Snake Game Using Turtle Module on Python 

Snake game reminds me my childhood, first cell phone was Nokia 3310. And this game is really additive. The snake in the Snake game is basically controlled using the four direction key relative to the direction it is headed in. The player’s objective in the game is to achieve maximum points as possible by collecting food or fruits. The player loses once the snake hits the wall or hits itself.
## Libraries Required:
So, we will be creating a Python-based-game using the following modules:

- Turtle: It is a pre-installed python library that enables users to create shapes and pictures by providing them a virtual canvas.
- Time: This function is used to count the number of seconds elapsed since the epoch.
- Random: This function is used to generate random numbers in Python by using random module.
## Support
Using PyCharm application which is specially made for Python programs.

Also, VSCode can be used for this program. Install Python3 from extensions of VSCode. Then, save the program in the form of your_filename.py

## How Code Works:
Below is the step-by-step Approach to create a Snake Game using Turtle module:
1. IMPORTING LIBRARIES: We will be importing modules into the program and giving values for the game.
https://github.com/Saad-data/Snake_game-withj-python-using-turtle/blob/main/Screen%20Shot%202022-08-17%20at%2013.57.45.png

2. SETUP SCREEN & DIRECTION KEYS: Now, we will be creating the display of the game and the direction keys for the snake, i.e, the window screen for the game.
https://github.com/Saad-data/Snake_game-withj-python-using-turtle/blob/main/image%202%20Screen%2B%20keys%20for%20snake%20directions.png

3. SNAKE BODY,MOVEMENT OF SEGMENTS AND EXTENT : We have created the separate module for the snake body and snake segments movement (named as: snake.py). Each time snake bit the food the size of the snake extent, this function is also available in this module. So that our main.py will be as simple as possible.
https://github.com/Saad-data/Snake_game-withj-python-using-turtle/blob/main/snake%20module-1.png
https://github.com/Saad-data/Snake_game-withj-python-using-turtle/blob/main/snake%20module-2.png

4. CREATING FOOD AND RANDOMISE LOCATION: Similarly we have created the food module for snake which contains the shape and color and random location of the food.
https://github.com/Saad-data/Snake_game-withj-python-using-turtle/blob/main/food%20module.png

5. DISPLAY SCOREBOARD, INCREASE SCORE AND GAMEOVER DISPLAY: In the same manner we also created the scoreboard to update the score on the bases of collecting each food piece. After the food is eaten, the score will be counted.
https://github.com/Saad-data/Snake_game-withj-python-using-turtle/blob/main/scoreboard%20module.png

6. HITTING TO WALL, FOOD, TIME DELAY AND BITTING HIMSELF: The main.py contain the while loop which keep the game runing untill the condition is fulfilled. And it also contain all the functions like collision to wall, Collision to snake body (himself), hitting the food circle and time delay of snake speed. 
https://github.com/Saad-data/Snake_game-withj-python-using-turtle/blob/main/main%20(snake%20touch%20food%2C%20hitting%20to%20wall%2C%20hitting%20himself.png
## FAQ

#### What is the set size of the Screen in the game?

Answer: The screen size is 600 x 600 pixels, syntax: screen.setup(width=600, height=600).
It's important to understand the screen coordinates, which will help you understand the snake movement.
https://github.com/Saad-data/Snake_game-withj-python-using-turtle/blob/main/screen%20cordinates.png

#### What is the size of each segment of Snake?

Answer: The sie of each segemnt is same as the size each pixel in the turtle 20X20. So each segment of snake is 20X20, We can allocate any shape we want to pixel in the snake the shape is square. And the food is the shape of pixel in circle.


## Feedback

If you have any feedback, please reach out to us at syedsaad047@gmail.com

