from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import sys

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Get the canvas and root window
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

# Make the window resizable
root.resizable(True, True)  # Arguments are (width, height). True means resizable.

# Optional: Set initial position (for example, 100x100 pixels from top-left corner of the screen)
root.geometry('+100+100')


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
play_again = True

while play_again :
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #Detect collision with wall.
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        #Detect collision with tail.
        for segment in snake.segments[2:]:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    valid_input = False
    while not valid_input:
        answerFromUser = input("Would you like to play again? (Y/N): ").upper()
        if answerFromUser == "Y":
            scoreboard.clear()
            snake.reset()
            game_is_on = True
            valid_input = True
            scoreboard.resetScore()
        elif answerFromUser == "N":
            scoreboard.resetScore()
            print("Thank you for playing.")
            play_again = False
            valid_input = True
            screen.bye()  # Proper way to close the Turtle graphics window
            sys.exit()
        else:
            print("Please insert valid input: Y = Yes | N = No")

screen.exitonclick()
