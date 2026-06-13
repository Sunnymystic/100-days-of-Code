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


turtles = []
race_is_one = False
colors = ["red","blue","orange","purple","magenta"]

screen = Screen()
screen.setup(width=500,height=400)  # Allows to set the width and height of the screen
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)

if user_bet : 
    race_is_on = True
    
for i in range(len(colors)):
    new_turtle = Turtle()
    if i % 2 == 0:
        turtles.append(turtle_setup(new_turtle,"turtle",colors[i],(-240,i//2*50)))
    else:
        turtles.append(turtle_setup(new_turtle,"turtle",colors[i],(-240,i//-2*50)))
    
while race_is_on:
    for turtle in turtles:
        if turtle.xcor() < 230:
            turtle.penup()
            turtle.forward(rd.randint(1,10))
            turtle.pendown()
        else:
            race_is_on = False
screen.bye()
winner = winner_turtle()
if user_bet == winner:
    print("You guessed it right!")
else:
    print(f"You guessed it wrong! The winner was {winner.capitalize()}")


