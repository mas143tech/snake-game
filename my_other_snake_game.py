import turtle as s
import time

from food_class import Food
from score import Score
from snake_class import Snake

screen = s.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()


    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280:
        game_is_on=False
        score.game_over()
        print('Game Over')
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()
            print('Game Over')




screen.exitonclick()
