from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.penup()
        self.move_speed=0.1

    def start(self):
        self.move_speed=0.1
        self.setpos(0, 0)
        self.x_bounce()

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.move_speed *= 0.9
        self.x_move *= -1
