from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        # self.pencolor("white")
        self.penup()
        self.goto(position)
        self.move_up = False
        self.move_down = False
    
    def go_up(self):
        self.move_up = True
        self.move()
        
    def stop_go_up(self):
        self.move_up = False
        
    def go_down(self):
        self.move_down = True
        self.move()
    
    def stop_go_down(self):
        self.move_down = False
        

    def move(self):
        if self.move_up and self.ycor() < 240.0:
            self.sety(self.ycor() + 20)
            # print(self.ycor())
        if self.move_down and self.ycor() > -240.0:
            self.sety(self.ycor() - 20)
            # print(self.paddles[i].ycor())