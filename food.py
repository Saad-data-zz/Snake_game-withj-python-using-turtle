from turtle import Turtle
import random
# in the parantheses we have to mention the name where we inheritante from
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        #noramlly the is 20X20 of pixcel, we are taking 10X10 whichis 0.5X0.5
        self.shapesize(stretch_len = 0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        #calling the refresh method will randomly gives a new posiition to the food circle
        self.refresh()
        #for creatig the random position for the snake food circle


    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
