#which tells in which level we are currently and gameover sequence
FONT = ("courier", 24, "normal")

from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level= 1
        self.goto(-280, 250)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"level: {self.level}",align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center", font=FONT)

