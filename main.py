from turtle import Screen, Turtle
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Scoreboard, game_over


scrn = Screen()
scrn.setup(720, 620)
scrn.bgcolor("black")
scrn.title("Snake Game")
tezina = 0.1
unos = scrn.textinput("Difficulty level", "Choose difficulty ('hard', 'normal', 'easy'): ")
if unos.lower() == "hard":
    tezina = 0.07
elif unos.lower() == "easy":
    tezina = 0.13
scrn.tracer(0)
skor = Scoreboard()

zmija = Snake()
scrn.update()
scrn.listen()

scrn.onkey(zmija.rig, "Right")
scrn.onkey(zmija.lef, "Left")
scrn.onkey(zmija.uup, "Up")
scrn.onkey(zmija.doown, "Down")

should_continue = True
hrana = Food()
while should_continue:
    zmija.move()
    scrn.update()
    sleep(tezina)
    if zmija.give_head().distance(hrana) < 15:
        hrana.refresh()
        zmija.add_on_size()
        skor.update()
    if zmija.bite():
        scrn.update()
        should_continue = False

game_over()
scrn.exitonclick()