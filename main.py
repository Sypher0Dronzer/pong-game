from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score=Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=l_paddle.up, key="w")
game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)#to increase speed each time it hits the paddle
    screen.update()
    ball.move()
    # To detect the boll collision with the top and bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # to detect the ball and paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    # Tod detect when the paddle misses
    elif ball.xcor() > 370:
        ball.start()
        score.l_point()
    elif ball.xcor() < -370:
        ball.start()
        score.r_point()
screen.exitonclick()
