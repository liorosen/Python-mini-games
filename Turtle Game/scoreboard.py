from turtle import Turtle
import time
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
SMALLER_FONT = ("Courier", 18, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def write_text(self,text, y_offset):
        self.penup()
        self.goto(0, y_offset)  # Move to the specified vertical position
        self.write(text, align=ALIGNMENT, font=SMALLER_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
        time.sleep(2)
        self.write_text("Would you like to play again?", -40)
        self.write_text("Y = yes | N = no ", -60)

    def resetGame(self):
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()