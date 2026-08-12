import os
import time
from csv import DictWriter
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0

    def show_score(self):
        self.teleport(-12, 300)
        self.pencolor('white')
        self.clear()
        self.write(f'Player 1: {self.p1_score}      Player 2: {self.p2_score}', align='center', font=('Courier', 12, 'bold') )

    def who_wins(self):
        if self.p1_score == 20:
            self.game_over('Player 1')
            self.save_max_score('Player 1')
            return True
        elif self.p2_score == 20:
            self.game_over('Player 2')
            self.save_max_score('Player 2')
            return True

        return False

    def game_over(self, player):
        self.teleport(0, 20)
        self.write('GAME OVER', align='center', font=('Courier', 20, 'bold'))

        self.teleport(0, -10)

        if player == 'Player 2':
            self.write('Player 2 won', align='center', font=('Courier', 16, 'bold'))
        else:
            self.write('Player 1 won', align='center', font=('Courier', 16, 'bold'))

    def save_max_score(self, player):

        file_exists = os.path.exists('max_score.csv') and os.path.getsize('max_score.csv') > 0

        with open('max_score.csv', 'a', newline='') as file:
            writer = DictWriter(file, fieldnames=['Date', 'Winner'])

            if not file_exists:
                writer.writeheader()
            writer.writerow({'Date': time.strftime('%d.%m.%y %H:%M:%S'), 'Winner': player})
