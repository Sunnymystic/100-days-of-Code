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
scoreboard = Scoreboard()
player = Player(carmanager,scoreboard)

screen.listen()
screen.onkeypress(player.go_up,"q")
screen.onkeyrelease(player.stop_go_up,"q")

is_game_on = True
counter = 0
while is_game_on:
    time.sleep(1/carmanager.speed)
    print(1/carmanager.speed)
    screen.update()
    scoreboard.display_message(is_game_on)
    if counter == 6 : 
        cars = carmanager.generate_the_cars()
    for car in cars:
        carmanager.move(car)
        if player.hit_by_car(car):
            is_game_on = False
            message = Turtle()
            scoreboard.display_message(is_game_on)
            break
    counter += 1
    if counter == 7:
        counter = 1
        
    
screen.exitonclick()