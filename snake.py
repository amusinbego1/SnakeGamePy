from turtle import Turtle


class Snake:
    def __init__(self):
        self.squares = []
        self.SCREEN_WIDTH = 700
        self.TURTLE_SIZE = 20
        self.SCREEN_HEIGHT = 600
        x = 0
        for i in range(0, 3):
            self.squares.append(Turtle(shape="square"))
            self.squares[i].penup()
            self.squares[i].fillcolor("WHITE")
            self.squares[i].setx(x)
            x -= 20
        self.head_pos = self.squares[0].position()
        self.end_pos = self.squares[2].position()

    def move(self):
        def exceeds():
            if self.squares[0].xcor() >= self.SCREEN_WIDTH / 2 + self.TURTLE_SIZE/2:
                self.squares[0].setx(-self.SCREEN_WIDTH / 2 + self.TURTLE_SIZE/2)
            elif self.squares[0].xcor() <= -self.SCREEN_WIDTH / 2 - self.TURTLE_SIZE/2:
                self.squares[0].setx(self.SCREEN_WIDTH / 2 - self.TURTLE_SIZE/2)
            elif self.squares[0].ycor() >= self.SCREEN_HEIGHT / 2 + self.TURTLE_SIZE/2:
                self.squares[0].sety(-self.SCREEN_HEIGHT / 2 + self.TURTLE_SIZE/2)
            elif self.squares[0].ycor() <= -self.SCREEN_HEIGHT / 2 - self.TURTLE_SIZE/2:
                self.squares[0].sety(self.SCREEN_HEIGHT / 2 - self.TURTLE_SIZE/2)

        self.end_pos = self.squares[len(self.squares) - 1].position()
        for i in range(len(self.squares) - 1, 0, -1):
            self.squares[i].setposition(self.squares[i-1].position())
        self.squares[0].forward(self.TURTLE_SIZE)
        self.head_pos = self.squares[0].position()
        exceeds()

    def give_head(self):
        return self.squares[0]

    def rig(self):
        if self.squares[0].heading() != 180:
            self.squares[0].setheading(0)

    def lef(self):
        if self.squares[0].heading() != 0:
            self.squares[0].setheading(180)

    def uup(self):
        if self.squares[0].heading() != 270:
            self.squares[0].setheading(90)

    def doown(self):
        if self.squares[0].heading() != 90:
            self.squares[0].setheading(270)

    def add_on_size(self):
        self.squares.append(Turtle(shape="square"))
        self.squares[len(self.squares) - 1].penup()
        self.squares[len(self.squares) - 1].fillcolor("white")
        self.squares[len(self.squares) - 1].setposition(self.end_pos)

    def bite(self):
        for x in self.squares[1:]:
            if self.give_head().distance(x) < self.TURTLE_SIZE-2:
                x.fillcolor("red")
                return True
        return False

