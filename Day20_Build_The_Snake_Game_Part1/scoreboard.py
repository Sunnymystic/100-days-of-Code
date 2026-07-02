from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.take_score_to_the_top()

    def take_score_to_the_top(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

    def display_score(self, is_snake_alive):
        self.clear()
        self.color("white")
        if is_snake_alive:
            self.write(f"Score : {self.score}", align= ALIGNMENT, font=FONT)
        else:
            self.write(f"Game Over ! Your Final Score: {self.score}", align="center", font=("Arial", 18, "bold"))
