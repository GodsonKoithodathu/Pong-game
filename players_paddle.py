from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cordinates):
        super().__init__()
        self.penup()
        self.goto(cordinates)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    # created function that will respond to the keyboards button in the game:
    def up(self):
        new_ycor = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_ycor)

    def down(self):
        new_ycor = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_ycor)
