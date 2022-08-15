import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()

#screen sizing

screen.setup(width=600, height=600)
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
#changing the background color of screen

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

screen.bgcolor("Black")
screen.title("Snake Game")

game_is_on = True
while game_is_on:
    screen.update()
    #this will add delay in move
    time.sleep(0.1)

    snake.move()
#score = 0
    #Detect when teh snake touch's the food circle
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect the collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segment[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    #RULE:- If the head of the snake collide with any segment in the tail:
    #TRIGGER GAME OVER

    #segments[0].right(2)
#simple way of creating the square on the screen
# #Creating the square on the screen
# segment_1 = Turtle("square")
# #changing the color
# segment_1.color("yellow")
#
# #because we need 3 square blocks
# segment_2 = Turtle("square")
# segment_2.color("yellow")
# segment_2.goto(x=-20, y=0)
#
# segment_3 = Turtle("square")
# segment_3.color("yellow")
# segment_3.goto(x=-40, y=0)

screen.exitonclick()