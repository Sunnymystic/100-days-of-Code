#TODO: turtle should do random walk.
#TODO: Pen should be of thicker size.
#TODO: Each line should be of different color
#TODO: Increase the speed of turtle gradually as it moves.
from turtle import Turtle,Screen
import random

tim = Turtle()
tim.pensize(20)
color = ["red","blue","gold","pink","purple","magenta","black","#800020","olive","brown"]

directions = [0,90,180,270]
for i in range(1000):
    tim.pencolor(random.choice(color))
    tim.forward(25)
    tim.setheading(random.choice(directions))
    tim.speed("fastest")
screen = Screen()
screen.exitonclick() 
