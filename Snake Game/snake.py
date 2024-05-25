from turtle import Turtle
import time
STARTING_POSITIONS = [(-220, 0), (-240, 0), (-260, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.moving = False  # Initialize moving here
        self.last_move_time = time.time()
        self.move_cooldown = 0.1  # 100 ms cooldown between moves

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())



    def can_change_direction(self):
        if time.time() - self.last_move_time > self.move_cooldown:
            self.last_move_time = time.time()
            return True
        return False

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Changes the snake's direction to UP if allowed."""
        if self.head.heading() != DOWN and self.can_change_direction():
            self.head.setheading(UP)


    def down(self):
        """Changes the snake's direction to DOWN if allowed."""
        if self.head.heading() != UP and self.can_change_direction():
            self.head.setheading(DOWN)


    def left(self):
        """Changes the snake's direction to LEFT if allowed."""
        if self.head.heading() != RIGHT and self.can_change_direction():
            self.head.setheading(LEFT)


    def right(self):
        """Changes the snake's direction to RIGHT if allowed."""
        if self.head.heading() != LEFT and self.can_change_direction():
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move existing segments off-screen
        self.segments.clear()  # Clear the list of segments
        self.create_snake()  # Recreate the snake
        self.head = self.segments[0]  # Redefine the head
        self.head.setheading(RIGHT)