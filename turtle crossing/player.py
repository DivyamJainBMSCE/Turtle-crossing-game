from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")

    def move(self):
        new_y=self.ycor()+MOVE_DISTANCE
        self.goto(0,y=new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)



