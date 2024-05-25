from turtle import Turtle
import time
import snake
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
SMALLER_FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = 0
        with open("scores.txt" , mode="r") as data:
            self.highScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}" , align=ALIGNMENT, font=FONT)

    def write_text(self,text, y_offset):
        self.penup()
        self.goto(0, y_offset)  # Move to the specified vertical position
        self.write(text, align=ALIGNMENT, font=SMALLER_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        time.sleep(2)
        self. write_text("Would you like to play again?", -40)
        self.write_text("Y = yes | N = no ", -60)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def resetScore(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("scores.txt" , mode= "w") as data :
                data.write(f"{self.highScore}")
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()