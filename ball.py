from turtle import Turtle
from random import choice


RIGHT = [5, 10, 350, 355]
LEFT = [170, 175, 185, 190]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('pink')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.initialize_the_ball(choice([LEFT, RIGHT]))

    def initialize_the_ball(self, direction):
        self.teleport(0, 0)
        self.setheading(choice(direction))

    def move_the_ball(self):
        self.fd(7)

    def collision_with_wall(self):
        if abs(self.ycor()) >= 340:
            self.bounce_with_wall()

        if self.xcor() >= 340:
            return 2
        elif self.xcor() <= -340:
            return 1
        else:
            return 0

    def bounce_with_wall(self):
        self.setheading(360 - self.heading())

    def collision_with_paddle(self, paddle):
        if paddle.ycor() - 50 <= self.ycor() <= paddle.ycor() + 50 and paddle.xcor() - 10 <= self.xcor() <= paddle.xcor() + 10:
            self.bounce_with_paddle(paddle)

    def bounce_with_paddle(self, paddle):
        if paddle.xcor() < 0 and 90 < self.heading() < 270:
            self.setheading(180 - self.heading())
        elif paddle.xcor() > 0 and (90 > self.heading()  or self.heading() > 270):
            self.setheading(180 - self.heading())

