from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed('fastest')
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.write(f"score={self.score} ", align="left", font=("Arial", 10, "normal"))
        self.hideturtle()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score={self.score} ", align="left", font=("Arial", 10, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("game over", align="left", font=("Arial", 10, "normal"))











