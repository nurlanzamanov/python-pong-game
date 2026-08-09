from turtle import Turtle


DOWN = 270


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor('white')
        self.width(5)

    def draw_outer_border(self):
        self.teleport(-350, 350)
        self.pendown()
        self.goto(-350, -350)
        self.goto(350, -350)
        self.goto(350, 350)
        self.goto(-350, 350)
        self.penup()

    def draw_center_line(self):
        self.teleport(0, 350)
        self.setheading(DOWN)

        while self.ycor() >= -350:
            self.pendown()
            self.fd(14)
            self.penup()
            self.fd(14)
