# There is going to be a little popup that will ask us to bet 
# who will win the race. Pop up should have OK and Cancel buttons.
#once the race is over print the line : You lose. The green turtle is the winner.

from turtle import Turtle,Screen
import random as rd

def turtle_setup(object,shape,color,coord):
    object.penup()
    object.shape(shape)
    object.fillcolor(color)
    object.goto(x=coord[0],y=coord[1])
    object.pendown()
    object.name = color  
    return object

def winner_turtle():
    for turtle in turtles:
        if turtle.xcor() >= 230:
            return turtle.name.lower()

    
red = Turtle()
blue = Turtle()
orange = Turtle()
purple = Turtle()
magenta = Turtle()
turtles = []
screen = Screen()
screen.setup(width=500,height=400)  # Allows to set the width and height of the screen
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)

# speed = [range(1,20)]
# print(speed)

turtles.append(turtle_setup(red,"turtle","red",(-240,50)))
turtles.append(turtle_setup(blue,"turtle","blue",(-240,100)))
turtles.append(turtle_setup(orange,"turtle","orange",(-240,0)))
turtles.append(turtle_setup(purple,"turtle","purple",(-240,-50)))
turtles.append(turtle_setup(magenta,"turtle","magenta",(-240,-100)))
while red.xcor() < 230 and blue.xcor() < 230 and orange.xcor() < 230 and purple.xcor() < 230 and magenta.xcor() < 230:
    
    red.forward(rd.randint(1,10))
    blue.forward(rd.randint(1,10))
    orange.forward(rd.randint(1,10))
    purple.forward(rd.randint(1,10))
    magenta.forward(rd.randint(1,10))
screen.bye()
winner = winner_turtle()
if user_bet == winner:
    print("You guessed it right!")
else:
    print(f"You guessed it wrong! The winner was {winner.capitalize()}")


