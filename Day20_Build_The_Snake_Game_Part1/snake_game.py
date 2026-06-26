#TODO: Create a snake body  -- Done
#TODO: Move the snake  -- Done
#TODO: Control the snake --- Done
#TODO: Detect colision with food -- Done
#TODO: Create a scoreboard -- Done
#TODO: Detect collision with wall -- Done
#TODO: Detect colliision with tail
#TODO: Every time snake eates food, increase the length of the snake by one.
#TODO: Every time snake eats food, its speed should get incresed.
#TODO: Vertical - left and right arrows; horizontal - up for left and down for right arrow

from turtle import Screen,Turtle
from snake import Snake
import random as rd
import time

def create_food():
    food = Turtle()
    food.shape("C:/Users/sudogra/Desktop/projects/Learn Python/Day20_Build_The_Snake_Game_Part1/apple.gif")
    food.shapesize(stretch_len=1,stretch_wid=1)
    x = rd.randint(-280,280)
    y = rd.randint(-280,280)
    food.goto(x,y)
    return food

def create_a_pen():
    pen = Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 100)
    return pen
  
def display_score(score,pen):
    pen.clear()
    pen.color("white")
    pen.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))
    return pen

def hide_score(pen):
    pen.clear()
    pen.hideturtle()
    
def display_game_over_and_final_score():
    pen = create_a_pen()
    pen.color("white")
    pen.write(f"Game Over ! Your Final Score: {score}", align="center", font=("Arial", 18, "bold"))
    
def has_eaten_food():
    head = snake.segments[0]
    if head.distance(food) < 15:
        return True
    else:
        return False

def has_hit_wall():
    head = snake.segments[0]
    if(head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280):
        return True
    else:
        return False    


def has_hit_tail():
    head = snake.segments[0]
    for segment in snake.segments[1:-1]:
        if head.distance(segment) < 10:
            return True
    return False

# def increase_snake_spped():
    
direction = "RIGHT"

def turn_left():
    global direction
    if direction != "RIGHT":
        snake.segments[0].setheading(180)
        direction = "LEFT"

def turn_right():
    global direction
    if direction != "LEFT":
        snake.segments[0].setheading(0)
        direction = "RIGHT"

def turn_up():
    global direction
    if direction != "DOWN":
        snake.segments[0].setheading(90)
        direction = "UP"

def turn_down():
    global direction
    if direction != "UP":
        snake.segments[0].setheading(270)
        direction = "DOWN"

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.addshape("C:/Users/sudogra/Desktop/projects/Learn Python/Day20_Build_The_Snake_Game_Part1/apple.gif")

pen = create_a_pen()
snake = Snake()

food = create_food()

game_is_on = True
score = 0
screen.listen()
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(turn_up, "Up")
screen.onkey(turn_down, "Down")



while game_is_on:
    screen.update()
    pen = display_score(score,pen)
    time.sleep(0.1)
    ### For straight movement
    for seg_num in range(len(snake.segments)-1,0,-1):
        new_x = snake.segments[seg_num - 1].xcor()
        new_y = snake.segments[seg_num -1].ycor()
        snake.segments[seg_num].goto(new_x,new_y)
    snake.segments[0].forward(10)
    ### To detect collision with the food
    if has_eaten_food():
        food.clear()
        food.hideturtle()
        score += 1
        food = create_food() 
        snake.increase_snake_size()
        # increase_snake_speed()   
    if (has_hit_wall() or has_hit_tail()) and len(snake.segments) > 3:
        game_is_on = False        
        screen.onkey(None, "Left")
        screen.onkey(None, "Right")
        screen.onkey(None, "Up")
        screen.onkey(None, "Down")
        hide_score(pen)
        display_game_over_and_final_score()

screen.exitonclick()