from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # created function that will move the ball:
    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    # Ball bounce when it will hit the y- coordinate:
    def bounce_y(self):
        self.y_move *= -1

    # ball will bounce when the ball hits the players paddles:
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # this code is for resting the ball to center and change the direction of the ball to opposite player:
    def missed_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
