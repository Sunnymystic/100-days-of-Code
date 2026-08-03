from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.take_score_to_the_top()

    def take_score_to_the_top(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-280,270)

    def display_message(self, is_game_on):
        self.clear()
        self.color("black")
        if is_game_on:
            self.write(f"Level : {self.level}", align= ALIGNMENT, font=FONT)
        else:
            self.goto(0,0)
            self.write("Game Over", align="center", font=("Arial", 18, "bold"))

