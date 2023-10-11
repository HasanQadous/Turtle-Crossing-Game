from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-230,270)
        self.write(f"Score: {self.score}", align="Center", font=("Courier", 20,"normal"))

    def lap_completed(self):
        self.clear()
        self.goto(-230, 270)
        self.write(f"Score: {self.score }", align="Center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="Center", font=("Courier", 50, "normal"))
