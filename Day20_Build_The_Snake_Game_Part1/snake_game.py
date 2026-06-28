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

import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.addshape("C:/Users/sudogra/Desktop/projects/Learn Python/Day20_Build_The_Snake_Game_Part1/apple.gif")

#pen = create_a_pen()
Snake.set_screen(screen)
snake = Snake()

#food = create_food()

def game_loop():
    if snake.is_alive:
        snake.move()
        screen.update()
        delay = max(40, 100 - (snake.current_speed - 1) * 8)
        screen.ontimer(game_loop, delay)

screen.listen()
game_loop()
screen.mainloop()