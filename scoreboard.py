from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter=1
        self.penup()
        self.hideturtle()
        self.goto(-210,230)
        self.color("white")
        self.write_level()
    def increase_score(self):
        self.undo()
        self.counter+=1
        self.write_level()
    def write_level(self):
        self.write(f"Level: {self.counter}",align="center",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)