from turtle import Turtle

class Hasan(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def go_up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(),new_y)

    def go_down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 15
            self.goto(self.xcor(),new_y)

    def go_left(self):
        if self.xcor() > -280:
            new_x = self.xcor() - 15
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < 280:
            new_x = self.xcor() + 15
            self.goto(new_x, self.ycor())