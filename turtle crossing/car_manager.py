from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
NO_OF_CARS=[16,17,18]

class CarManager():
    def __init__(self):
        super().__init__()
        self.cars=[]
        self.create_cars()
        self.x_move=5

    def create_cars(self):
        for i in range(0, random.choice(NO_OF_CARS)):
            car=Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.goto(x=random.randint(-300, 300), y=random.randint(-270, 280))
            self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            new_x=car.xcor()-self.x_move
            car.goto(x=new_x,y=car.ycor())

    def refresh(self):
        for car in self.cars:
            if car.xcor()<-320:
                car.goto(x=300, y=random.randint(-270, 280))

    def increase_speed(self):
        self.x_move+= MOVE_INCREMENT





