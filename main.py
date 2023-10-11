from turtle import Turtle,Screen
import time
from hasan import Hasan
from cars import Cars
import random
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

hasan = Hasan()
screen.listen()
screen.onkey(key="Up", fun=hasan.go_up)
screen.onkey(key="Down", fun=hasan.go_down)
screen.onkey(key="Right", fun=hasan.go_right)
screen.onkey(key="Left", fun=hasan.go_left)

game_is_on = True
scoreboard = Scoreboard()
cars = Cars()
speed = 5
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.make_cars()
    cars.move_car(speed)
    for car in cars.all_cars:
        if car.distance(hasan) < 28:
            game_is_on = False
            scoreboard.game_over()

    if hasan.ycor() > 290:
        scoreboard.score +=1
        scoreboard.lap_completed()
        hasan.goto(0, -280)
        speed += 2






















screen.exitonclick()