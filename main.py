from turtle import Screen
from border import Border
from scoreboard import ScoreBoard
from ball import Ball
from paddle import Paddle


screen = Screen()
screen.setup(700, 700)
screen.bgcolor('black')
screen.tracer(0)

your_paddle = Paddle((300, 20))
rival_paddle = Paddle((-300, 20))

screen.listen()
screen.onkey(your_paddle.move_up, 'Up')
screen.onkey(your_paddle.move_down, 'Down')
screen.onkey(rival_paddle.move_up, 'w')
screen.onkey(rival_paddle.move_down, 's')

ball = Ball()
scoreboard = ScoreBoard()
scoreboard.show_score()

border = Border()
border.draw_outer_border()
border.draw_center_line()

ball.initialize_the_ball()


def game_loop():
    ball.move_the_ball()

    side = ball.collision_with_wall()

    if side == 2:
        scoreboard.rival_score += 1
        scoreboard.show_score()
        ball.initialize_the_ball()
    elif side == 1:
        scoreboard.your_score += 1
        scoreboard.show_score()
        ball.initialize_the_ball()

    if scoreboard.who_wins():
        screen.update()
        return

    ball.collision_with_paddle(your_paddle)
    ball.collision_with_paddle(rival_paddle)

    screen.update()
    screen.ontimer(game_loop, 16)


game_loop()
screen.mainloop()
