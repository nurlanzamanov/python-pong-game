from random import choice
from turtle import Screen
from border import Border
from scoreboard import ScoreBoard
from ball import Ball, LEFT, RIGHT
from paddle import Paddle


screen = Screen()
screen.setup(700, 700)
screen.bgcolor('black')
screen.tracer(0)

p1_paddle = Paddle((-300, 20))
p2_paddle = Paddle((300, 20))

screen.listen()
screen.onkey(p1_paddle.move_up, 'w')
screen.onkey(p1_paddle.move_down, 's')
screen.onkey(p2_paddle.move_up, 'Up')
screen.onkey(p2_paddle.move_down, 'Down')


ball = Ball()
scoreboard = ScoreBoard()
scoreboard.show_score()

border = Border()
border.draw_outer_border()
border.draw_center_line()



def game_loop():
    ball.move_the_ball()

    side = ball.collision_with_wall()

    if side == 2:
        scoreboard.p1_score += 1
        scoreboard.show_score()
        ball.initialize_the_ball(RIGHT)
    elif side == 1:
        scoreboard.p2_score += 1
        scoreboard.show_score()
        ball.initialize_the_ball(LEFT)

    if scoreboard.who_wins():
        ball.ht()
        screen.update()
        return

    ball.collision_with_paddle(p1_paddle)
    ball.collision_with_paddle(p2_paddle)

    screen.update()
    screen.ontimer(game_loop, 16)


game_loop()
screen.mainloop()
