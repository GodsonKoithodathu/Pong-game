from turtle import Turtle, Screen
from players_paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

# setting the screen for the game:
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.tracer(0)

# creating different objects from their respective class:
ball = Ball()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
score = ScoreBoard()

# making the screen listen to the keyboards button:
screen.listen()
screen.onkey(fun=right_paddle.up, key='Up')
screen.onkey(fun=right_paddle.down, key='Down')
screen.onkey(fun=left_paddle.up, key='w')
screen.onkey(fun=left_paddle.down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # code for bouncing the ball if it hits the y- coordinates:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # code for checking whether the ball is hitting the paddle or not if yes then ball should bounce:
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if the ball is missed by the right side player then reset the ball pos and start with opposite player:
    if ball.xcor() > 380:
        ball.missed_ball()
        score.l_point()

    # if the ball is missed by the left side player then reset the ball pos and start with opposite player:
    if ball.xcor() < -380:
        ball.missed_ball()
        score.r_point()

screen.exitonclick()
