from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        data = open("data.txt")
        self.high_score = int(data.read())
        data.close()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.new_score()

    def new_score(self):
        self.clear()
        self.write("Score: {score} High Score: {high} ".format(score=self.score, high=self.high_score), align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            data = open("data.txt", mode="w")
            data.write("{high_score}".format(high_score=self.high_score))
            data.close()
        self.score = 0
        self.new_score()

    def increase_score(self):
        self.score += 1
        self.new_score()