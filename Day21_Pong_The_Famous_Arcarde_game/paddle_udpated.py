from turtle import Turtle

STARTING_POSITION = [(-530.0, 0.0),(530.0,0.0)]

class Paddle:
    
    @classmethod
    def set_screen(cls,screen):
        cls.screen = screen

    def __init__(self):
        self.paddles = []
        self.create_paddle()
        # self.head = self.segments[0]
        self.move_up = False
        self.move_down = False
    
    def create_paddle(self):    
        for position in STARTING_POSITION:
            self.paddles.append(self.create_new_paddle(position))

    def go_up(self):
        self.move_up = True
        move()
        
    def stop_go_up(self):
        self.move_up = False
        
            
    def go_down(self):
        self.move_down = True
        move()
    
    def stop_go_down(self):
        self.move_down = False
        
        
    def bind_keys(self):
        self.screen.listen()
        self.screen.onkeypress(go_up,"q")
        self.screen.onkeyrelease(stop_go_up,"q")
        self.screen.onkeypress(go_down,"a")
        self.screen.onkeyrelease(stop_go_down,"a")
        

    def create_new_paddle(self, position):
        paddle = Turtle()
        paddle.penup()
        paddle.goto(position)
        paddle.shape("square")
        paddle.shapesize(3, 1)
        paddle.color("white")
        paddle.pencolor("white")
        self.paddles.append(paddle)
        
    def move(self):
        while self.paddle.ycor() <= 320 and self.paddle.ycor() >= -320:
            if move_up:
                paddle
              
    
    # def move(self):
    #     ### For straight movement
          
    #         # for seg_num in range(len(self.segments)-1,0,-1):
    #         #     new_y = self.segments[seg_num-1].ycor()
    #         #     self.segments[seg_num].goto(new_x,new_y)
    #         # self.head.forward(20)
            
    #     # print(self.head)
    #     # print(f"self.segments[0] {self.segments[0]}")
    #     # print(f"self.segments[2] {self.segments[2]}")
    #     # print(f"Dimensions of 1st segment : {self.head.xcor()},{self.head.ycor()}")
    #     # print(f"Dimensions of 2nd segment : {self.segments[1].xcor()},{self.segments[1].ycor()}")
    #     # print(f"Dimensions of 3rd segment : {self.segments[2].xcor()},{self.segments[2].ycor()}")
        
        
            
        
        