from turtle import Turtle


UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.shape('square')
        self.setheading(90)
        self.color('white')
        self.penup()
        self.teleport(coordinates[0], coordinates[1])

    def move_up(self):
        self.setheading(UP)
        if self.ycor() + 20 >= 310:
            self.fd(310 - self.ycor())
        else:
            self.fd(20)

    def move_down(self):
        self.setheading(DOWN)
        if self.ycor() - 20 <= -310:
            self.fd(310 + self.ycor())
        else:
            self.fd(20)
