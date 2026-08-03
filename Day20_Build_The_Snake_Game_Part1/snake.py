from turtle import Screen,Turtle
from food import Food
import random as rd

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

class Snake:
    screen = None
    direction = "RIGHT"
    current_speed = 1
    
    @classmethod
    def set_screen(cls,screen):
        cls.screen = screen

    def __init__(self,food,scoreboard):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.is_alive = True
        self.scoreboard = scoreboard
        self.food = food

    def create_snake(self):    
        for position in STARTING_POSITION:
            self.create_new_segment(position)
        self.bind_keys()
    
    def bind_keys(self):
        self.screen.listen()
        self.screen.onkey(self.turn_left, "Left")
        self.screen.onkey(self.turn_right, "Right")
        self.screen.onkey(self.turn_up, "Up")
        self.screen.onkey(self.turn_down, "Down")    

    def create_new_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.goto(position)
        segment.shape("square")
        segment.color("white")
        segment.pencolor("black")
        segment.speed(self.current_speed)
        self.segments.append(segment)
    
    def has_eaten_food(self):
        if self.head.distance(self.food) < 15:
            return True
        else:
            return False
    
    def increase_snake_size(self):
        last_segment = self.segments[-1]
        self.create_new_segment((last_segment.xcor(), last_segment.ycor()))
        
    def has_hit_wall(self):
        if(self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280):
            return True
        else:
            return False    

    def has_hit_tail(self):
        
        for segment in self.segments[2:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def increase_snake_speed(self):
        self.current_speed += 1

    def turn_left(self):
        if self.direction != "RIGHT":
            self.segments[0].setheading(180)
            self.direction = "LEFT"

    def turn_right(self):
        if self.direction != "LEFT":
            self.segments[0].setheading(0)
            self.direction = "RIGHT"

    def turn_up(self):
        if self.direction != "DOWN":
            self.segments[0].setheading(90)
            self.direction = "UP"

    def turn_down(self):
        if self.direction != "UP":
            self.segments[0].setheading(270)
            self.direction = "DOWN"

    def move(self):
        ### For straight movement
        self.scoreboard.display_score(self.is_alive)
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(10)
        ### To detect collision with the food
        if self.has_eaten_food():
            self.food.clear()
            self.food.hide_food()
            self.scoreboard.score += 1 
            print(self.scoreboard.score)
            self.increase_snake_size()
            if self.current_speed < 10:
                self.increase_snake_speed()
                print(self.current_speed)
            self.food = Food()  
        if (self.has_hit_wall() or (self.has_hit_tail()) and len(self.segments) > 3):
            self.is_alive = False
            self.screen.onkey(None, "Left")
            self.screen.onkey(None, "Right")
            self.screen.onkey(None, "Up")
            self.screen.onkey(None, "Down")
            self.food.hide_food()
            self.scoreboard.display_score(self.is_alive)
            return