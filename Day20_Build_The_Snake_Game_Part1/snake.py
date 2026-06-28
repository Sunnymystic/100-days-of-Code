from turtle import Screen,Turtle
import random as rd

class Snake:
    screen = None
    direction = "RIGHT"
    current_speed = 1
    
    @classmethod
    def set_screen(cls,screen):
        cls.screen = screen

    def __init__(self):
        self.starting_positions = [(0,0),(-20,0),(-40,0)]
        self.segments = []
        self.score = 0
        self.is_alive = True
        self.food = self.create_food()
        self.pen = self.create_a_pen()
    
        for position in self.starting_positions:
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
    
    def increase_snake_size(self):
        last_segment = self.segments[-1]
        self.create_new_segment((last_segment.xcor(), last_segment.ycor()))

    def create_food(self):
        food = Turtle()
        food.shape("C:/Users/sudogra/Desktop/projects/Learn Python/Day20_Build_The_Snake_Game_Part1/apple.gif")
        food.shapesize(stretch_len=1,stretch_wid=1)
        x = rd.randint(-280,280)
        y = rd.randint(-280,280)
        food.goto(x,y)
        return food

    def create_a_pen(self):
        pen = Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(0, 100)
        return pen
    
    def display_score(self):
        self.pen.clear()
        self.pen.color("white")
        self.pen.write(f"Score: {self.score}", align="center", font=("Arial", 18, "bold"))
        return self.pen

    def hide_score(self):
        self.pen.clear()
        self.pen.hideturtle()
        
    def display_game_over_and_final_score(self):
        self.pen.color("white")
        self.pen.write(f"Game Over ! Your Final Score: {self.score}", align="center", font=("Arial", 18, "bold"))
        
    def has_eaten_food(self):
        head = self.segments[0]
        if head.distance(self.food) < 15:
            return True
        else:
            return False

    def has_hit_wall(self):
        head = self.segments[0]
        if(head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280):
            return True
        else:
            return False    

    def has_hit_tail(self):
        head = self.segments[0]
        for segment in self.segments[2:]:
            if head.distance(segment) < 10:
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
        self.display_score()
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(10)
        ### To detect collision with the food
        if self.has_eaten_food():
            self.food.clear()
            self.food.hideturtle()
            self.score += 1 
            print(self.score)
            self.increase_snake_size()
            self.food = self.create_food()
            if self.current_speed < 10:
                self.increase_snake_speed()
                print(self.current_speed)  
        if (self.has_hit_wall() or self.has_hit_tail()) and len(self.segments) > 3:
            self.is_alive = False
            self.screen.onkey(None, "Left")
            self.screen.onkey(None, "Right")
            self.screen.onkey(None, "Up")
            self.screen.onkey(None, "Down")
            self.hide_score()
            self.display_game_over_and_final_score()
            return