import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import  sys

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
# Get the canvas and root window
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

# Make the window resizable
root.resizable(True, True)  # Arguments are (width, height). True means resizable.

# Optional: Set initial position (for example, 100x100 pixels from top-left corner of the screen)
root.geometry('+100+100')


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_down, "Down")

game_is_on = True
play_again = True

while play_again :
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        #Detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        #Detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

    valid_input = False
    while not valid_input:
        answerFromUser = input("Would you like to play again? (Y/N): ").upper()
        if answerFromUser == "Y":
            scoreboard.clear()
            player.resetPlayer()
            car_manager.resetCarManager()
            game_is_on = True
            valid_input = True
            scoreboard.resetGame()
        elif answerFromUser == "N":
            print("Thank you for playing.")
            play_again = False
            valid_input = True
            screen.bye()  # Proper way to close the Turtle graphics window
            sys.exit()
        else:
            print("Please insert valid input: Y = Yes | N = No")

screen.exitonclick()
