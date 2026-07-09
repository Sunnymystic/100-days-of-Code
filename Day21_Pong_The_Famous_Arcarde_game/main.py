from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

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


Paddle.set_screen(screen)
paddle = Paddle()
ball = Ball(paddle)
paddle.ball = ball

divide_the_screen()
ball.move()
screen.update()


# ball = Ball()
# scoreboard = Scoreboard()


def game_loop():
# if not paddle.is_game_on:
#     return

    paddle.bind_keys()
    ball.move_straight()

    # if paddle.is_game_on:
    screen.update()
    screen.ontimer(game_loop, 20)

screen.listen()
game_loop()
screen.mainloop()
# screen.exitonclick()
