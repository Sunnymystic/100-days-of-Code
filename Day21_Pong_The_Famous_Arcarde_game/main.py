from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

def divide_the_screen():
    divider = Turtle()
    divider.hideturtle()
    divider.color("white")
    divider.pencolor("white")
    divider.setheading(90)
    divider.pensize(5)
    divider.penup()
    divider.goto(0,-280)
    for _ in range(-280,320,40):
        divider.pendown()
        divider.forward(20)
        divider.penup()
        divider.forward(20)

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard = Scoreboard()
ball = Ball(l_paddle,r_paddle,scoreboard)

# ball.launch()

divide_the_screen()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeyrelease(r_paddle.stop_go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeyrelease(r_paddle.stop_go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeyrelease(l_paddle.stop_go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")
screen.onkeyrelease(l_paddle.stop_go_down,"s")

game_is_on = True
while game_is_on:
    # paddle.bind_keys()
    # ball.move_straight()
    screen.update()
    ball.move()
    

screen.exitonclick()
