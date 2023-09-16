from turtle import Screen
import time
from snakeMechanics import Snake
from foodMechanics import Food
from scoreboard import ScoreBoard

#Setting up the screen
sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

#Creating the snake object
snake = Snake()
food = Food()
new_score = ScoreBoard()

#Listen to keyboard inputs to control how the snake moves
sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

#Keep the snake moving until game gets over
game_running = True
while game_running:
    sc.update()
    time.sleep(0.1)
    snake.move()
    
    #Detecting whether food has been eaten
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        new_score.increase_score()
    
    #Detecting collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_running = False
        new_score.game_over()
        
    #Detecting collisions with the tail
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 1:
            game_running = False
            new_score.game_over()

#Exit the screen only on click
sc.exitonclick()