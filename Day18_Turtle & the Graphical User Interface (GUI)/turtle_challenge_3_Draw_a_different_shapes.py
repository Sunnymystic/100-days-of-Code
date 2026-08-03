#Draw a triangle,square,pentagon,hexagon,heptagon,octagon,nonagon and decagon.
from turtle import Turtle,Screen

tim = Turtle()

def make_a_shape(angle,time,color):
    for _ in range(time):
        tim.pencolor(color)
        tim.left(angle)
        tim.forward(100)

angle_time_and_color = {}
color = ["red","blue","gold","pink","purple","magenta","black","burgundy"] 
for i in range(3, 11):
    angle = 360 / (i)
    angle_time_and_color[angle] = [i, color[i-3]]
    
for angle,time_and_color in angle_time_and_color.items():
    make_a_shape(angle,time_and_color[0],time_and_color[1])

screen = Screen()
screen.exitonclick() 
   