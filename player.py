STARTING_POSITION = (0, -280)
#how much distance should turtle should move
MOVE_DISTANCE = 10
#where the finish line on the y-axis
FINISH_LINE_Y = 200

from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # self.move_to_starting_position()
        #we can use above method instead of self.goto(STARTING_POSIION) to remove repetation of code
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_to_starting_position(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
