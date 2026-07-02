from turtle import Screen,Turtle
import random as rd
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("C:/Users/sudogra/Desktop/projects/Learn Python/Day20_Build_The_Snake_Game_Part1/apple.gif")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.speed("fastest")
        x = rd.randint(-280,280)
        y = rd.randint(-280,280)
        self.goto(x,y)
    
    def hide_food(self):
        self.clear()
        self.hideturtle()
    # def create_food(self):
    #     return self.food    


        
    