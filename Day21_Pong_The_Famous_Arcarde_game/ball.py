from turtle import Turtle
import time
from scoreboard import Scoreboard

class Ball(Turtle):

    def __init__(self,l_paddle,r_paddle,scoreboard):
        super().__init__()
        self.speed(1)
        self.shape("circle")
        self.color("white")
        self.pencolor("white")
        self.x_move = 10
        self.y_move = 10
        self.penup()
        self.l_paddle = l_paddle
        self.r_paddle = r_paddle
        self.scoreboard = scoreboard
        

        # self.penup()
        # self.shapesize(stretch_len=1,stretch_wid=1)

    def hit_by_walls(self):
        if -280.0 <= self.ycor() <= 280.0:
            return False
        else:
            return True  
    
    def hit_by_r_paddle(self):  
    #Detect collision with r_paddle
        if self.distance(self.r_paddle) < 50 and self.xcor() > 330:
            self.increase_ball_speed()
            print(f"Current speed : {self.speed()}")
            return True
        return False

    def hit_by_l_paddle(self):  
    #Detect collision with r_paddle
        if self.distance(self.l_paddle) < 50 and self.xcor() < -330:
            self.increase_ball_speed()
            print(f"Current speed : {self.speed()}")
            return True
        return False
    
    def has_ball_gone_offscreen(self):
        if self.xcor() > 350 or self.xcor() < -350:
            self.speed(1)
            return True
        return False
    # def launch(self):
    #     self.setheading(-45)

    def reset_the_ball(self):
        self.goto(0,0)
        self.bounce_x()
        
    def bounce_y(self):
        self.y_move *= -1
        # self.x_move *= -1
        
    def bounce_x(self):
        # self.y_move *= -1
        self.x_move *= -1
    
    def left_misses(self):
        return self.xcor() < -340
        
    def right_misses(self):
        return self.xcor() > 340
    
    def move(self):
        time.sleep(0.1 * (0.9 ** (self.speed() - 1)))
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        if self.hit_by_walls():
            self.bounce_y()
        if self.hit_by_r_paddle() or self.hit_by_l_paddle():
            self.bounce_x()
        if self.has_ball_gone_offscreen():
            if self.left_misses():
                self.scoreboard.r_point()
            if self.right_misses():
                self.scoreboard.l_point()
            self.reset_the_ball()
            
    def increase_ball_speed(self):
        self.speed(min(15,self.speed() + 1))
          
            
            
        
            
    
   
            
            