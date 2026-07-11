import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
cars = []


carmanager = CarManager()
player = Player(carmanager)
screen.listen()
screen.onkeypress(player.go_up,"q")
screen.onkeyrelease(player.stop_go_up,"q")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1 * (0.9 ** (carmanager.speed() - 1)))
    screen.update()
    if counter == 6 : 
        cars = carmanager.generate_the_cars()
    for car in cars:
        carmanager.move(car)
        if player.hit_by_car(car):
            game_is_on = False
            message = Turtle()
            message.write("Game Over!", align= ALIGNMENT, font=FONT)
            break
    counter += 1
    if counter == 7:
        counter = 1
        
    
screen.exitonclick()