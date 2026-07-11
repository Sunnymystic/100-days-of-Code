STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self,car_manager):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.shapesize(1.0,1.0)
        self.setheading(90)
        self.move_up = False
        self.car_manager = car_manager
    
    def move(self):
        if self.move_up and self.ycor() < FINISH_LINE_Y:
            self.sety(self.ycor() + 10)
        else:
            self.goto(0,-FINISH_LINE_Y)
            self.car_manager.increment_cars_speed()
            
    
    def go_up(self):
        self.move_up = True
        self.move()
        
    def stop_go_up(self):
        self.move_up = False
        
    def hit_by_car(self,car):
        if self.distance(car) < 15:
            return True
        return False
    