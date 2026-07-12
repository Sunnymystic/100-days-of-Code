COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random as rd

class CarManager():
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def generate_the_cars(self):
        # if len(self.cars) < MAX_CARS:
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(280,rd.randint(-240,260))
        car.color(rd.choice(COLORS))
        car.setheading(180)
        car.speed(STARTING_MOVE_DISTANCE)
        self.cars.append(car)
        self.remove_offscreen_cars()
        return self.cars
    
    def move(self,car):
        car.setx(car.xcor() - self.speed)
        
    def remove_offscreen_cars(self):
        for car in self.cars:
            if car.xcor() > 280:
                self.cars.remove(car)
    
    def increment_cars_speed(self):
        self.speed += MOVE_INCREMENT
        print(self.speed)
            
            
    
            
        
        

        
    
            
        
