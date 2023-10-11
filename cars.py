from turtle import Turtle
import random
COLORS = ["blue","red","black","yellow","green","purple","orange","pink"]
class Cars:
    def __init__(self):
        self.all_cars = []

    def make_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(320, random_y)
            self.all_cars.append(new_car)

    def move_car(self, speed):
        for car in self.all_cars:
            car.backward(speed)





