from turtle import Turtle,Screen
tinny_the_turle = Turtle()
tinny_the_turle.shape("turtle")
tinny_the_turle.color("red","gold")

def make_a_square():
    tinny_the_turle.forward(100)
    tinny_the_turle.left(90)

for _ in range(4):
    make_a_square()

screen = Screen()
screen.exitonclick()