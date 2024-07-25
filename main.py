from turtle import Screen
from player import Player
from car import Car
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car = Car()
score = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for cur_car in car.all_cars:
        if cur_car.distance(player) < 20:
            score.game_over()
            game_is_on = False
    
    if player.ycor() > 300:
        score.increase_level()
        car.level_up()
        player.reset()
     
screen.exitonclick()