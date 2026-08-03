#TODO: turtle should do random walk.
#TODO: Pen should be of thicker size.
#TODO: Each line should be of different color
#TODO: Increase the speed of turtle gradually as it moves.
from turtle import Screen
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.pensize(20)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
    
   
directions = [0,90,180,270]
for i in range(1000):
    tim.pencolor(random_color())
    tim.forward(25)
    tim.setheading(random.choice(directions))
    tim.speed("fastest")
screen = Screen()
screen.exitonclick() 
