import time
from csv import DictWriter
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.rival_score = 0
        self.your_score = 0

    def show_score(self):
        self.teleport(-12, 300)
        self.pencolor('white')
        self.clear()
        self.write(
            f'Rival`s score: {self.rival_score}  Your score: {self.your_score}',
            align='center',
            font=('Courier', 12, 'bold')
        )

    def who_wins(self):
        if self.your_score == 20:
            self.game_over(2)
            self.save_max_score(2)
            return True
        elif self.rival_score == 20:
            self.game_over(1)
            self.save_max_score(1)
            return True

        return False

    def game_over(self, player):
        self.teleport(0, 20)
        self.write(
            'GAME OVER',
            align='center',
            font=('Courier', 20, 'bold')
        )

        self.teleport(0, -10)

        if player == 2:
            self.write(
                'Player 2 won',
                align='center',
                font=('Courier', 16, 'bold')
            )
        else:
            self.write(
                'Player 1 won',
                align='center',
                font=('Courier', 16, 'bold')
            )

    def save_max_score(self, player):
        with open('max_score.csv', 'w') as file:
            writer = DictWriter(file, fieldnames=['Date', 'Winner'])
            writer.writeheader()
            writer.writerow({
                'Date': time.strftime('%d.%m.%y %H:%M:%S'),
                'Winner': player
            })
