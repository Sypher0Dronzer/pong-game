from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        x_cor=self.xcor()
        y_cor = self.ycor() + 20
        self.goto(x_cor, y_cor)

    def down(self):
        x_cor = self.xcor()
        y_cor = self.ycor() - 20
        self.goto(x_cor, y_cor)
