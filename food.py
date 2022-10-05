from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.turtlesize(0.5, 0.5, 0.5)
        self.setposition(randrange(-320, 320, 20), randrange(-250, 250, 20))

    def refresh(self):
        self.setposition(randrange(-340, 340, 20), randrange(-300, 300, 20))