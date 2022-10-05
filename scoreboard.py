from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        file = open("hscore.txt")
        self.score = 0
        self.high_score = int(file.read())
        file.close()
        self.penup()
        self.color("white")
        self.setposition(0, 270)
        self.write(f"Score: {self.score} - High score: {self.high_score}", False, "center", font=("Courier", 20, "normal"))
        self.hideturtle()

    def update(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("hscore.txt", mode = "w")
            file.write(str(self.high_score))
            file.close()
        self.clear()
        self.write(f"Score: {self.score} - High score: {self.high_score}", False, "center", font=("Courier", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()


def game_over():
    over = Turtle()
    over.penup()
    over.color("white")
    over.hideturtle()
    over.write("GAME OVER", False, "center", font=("Courier", 30, "normal"))
