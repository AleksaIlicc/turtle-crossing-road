import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

score=Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("gray")
screen.listen()

player=Player()
screen.onkeypress(player.up,"Up")
car_manager=CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    if player.ycor()>290: #next level
        player.reset_position()
        score.increase_score()
        car_manager.level_up()
    for car in car_manager.all_cars:    #collision with cars
       if player.distance(car)<22:
           game_is_on=False
           score.game_over()
        

        
screen.exitonclick()
        
    
