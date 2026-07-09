from turtle import Turtle
import random as rd


class Ball(Turtle):
    direction = None

    def __init__(self, paddle_controller):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 100)

        self.paddle_controller = paddle_controller if hasattr(paddle_controller, "move") else None
        self.paddles = paddle_controller.paddles if self.paddle_controller is not None else paddle_controller

    def hit_by_paddle(self):
        for paddle in self.paddles:
            if self.distance(paddle) < 45:
                return True
        return False
      
    def hit_by_walls(self):
        if -280.0 <= self.ycor() <= 280.0:
            return False
        else:
            return True     
        
    def move_straight(self):
        self.speed(1)
        if not self.hit_by_walls() and not self.hit_by_paddle():
            self.forward(5)
        else:
            if self.hit_by_paddle():
                if self.direction == "left":
                    self.direction = "right"
                else:
                    self.direction = "left"

                if self.paddle_controller is not None:
                    self.paddle_controller.move()

                self.setheading(180 - self.heading())
            else:
                self.setheading(self.heading() + 90)
            self.forward(5)

    def move(self):
        self.penup()
        # print("chale chalo!")
        self.direction = rd.choice(["left", "right"])
        # print(self.direction)
        if self.direction == "left":
            heading = 180 - rd.randint(15, 45)
        else:
            heading = rd.randint(15, 45)
        self.setheading(heading)
        # self.move_straight()


# MAX_SPEED = 15
# speed = min(speed + 0.5, MAX_SPEED)


        
            