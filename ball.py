from turtle import Turtle
from random import choice


HEADINGS = [5, 10, 170, 175, 185, 190, 350, 355]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('pink')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.initialize_the_ball()

    def initialize_the_ball(self):
        self.teleport(0, 0)
        self.setheading(choice(HEADINGS))

    def move_the_ball(self):
        self.fd(7)

    def collision_with_wall(self):
        if abs(self.ycor()) >= 350:
            self.bounce_with_wall()

        if self.xcor() >= 350:
            return 2
        elif self.xcor() <= -350:
            return 1
        else:
            return 0

    def bounce_with_wall(self):
        if abs(self.xcor()) >= 350:
            self.teleport(0, 0)
            self.setheading(choice(HEADINGS))
            self.move_the_ball()
        else:
            self.setheading(360 - self.heading())

    def collision_with_paddle(self, paddle):
        if (paddle.ycor() - 50 <= self.ycor() <= paddle.ycor() + 50
                and paddle.xcor() - 10 <= self.xcor() <= paddle.xcor() + 10):
            self.bounce_with_paddle()

    def bounce_with_paddle(self):
        self.setheading(180 - self.heading())
