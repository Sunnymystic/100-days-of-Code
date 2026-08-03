#Below commented code is to extract the colours from an image.
# import colorgram
# def extrat_rgb_from_paintings():
#     colors = colorgram.extract("dh_painting.jpg", 30)
#     return colors

# colors = extrat_rgb_from_paintings()
# color_list = []
# rgb_tuples = [(c.rgb.r,c.rgb.g,c.rgb.b) for c in colors]
# print(rgb_tuples)

# dot 20 in size and spaced around 50 spaces
#10 by 10 square


from turtle import Screen
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

color_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

def get_color():
    color = random.choice(color_list)
    return color


screen = Screen()
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.left(135)
tim.pendown()

def move():
    for i in range(10):
        tim.speed("fastest")
        tim.dot(20,get_color())
        if i < 9:
            tim.penup()
            tim.forward(50)
            tim.pendown()

def back_to_position():
    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.left(90)
    tim.forward(450)
    tim.right(180)
    tim.pendown()
 

for _ in range(10):
    move()
    back_to_position()
    
tim.hideturtle()

screen.exitonclick()     

