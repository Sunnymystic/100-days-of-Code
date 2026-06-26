from turtle import Screen,Turtle
class Snake:
    starting_positions = [(0,0),(-20,0),(-40,0)]
    segments = []

    def __init__(self):
        for position in self.starting_positions:
            self.create_new_segment(position)

    def create_new_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.goto(position)
        segment.shape("square")
        segment.color("white")
        segment.pencolor("black")
        segment.speed("fastest")
        self.segments.append(segment)
    
    def increase_snake_size(self):
        last_segment = self.segments[-1]
        self.create_new_segment((last_segment.xcor(), last_segment.ycor()))
