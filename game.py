import turtle
import time  # Import the time module

# Venster instellen
wn = turtle.Screen()
wn.title("Pong voor Billy")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("green")
paddle.shapesize(stretch_wid=6, stretch_len=1)
paddle.penup()
paddle.goto(-350, 0)

def paddle_up():
    y = paddle.ycor()
    if y < 250:
        y += 20
        paddle.sety(y)

def paddle_down():
    y = paddle.ycor()
    if y > -240:
        y -= 20
        paddle.sety(y)

# Score variabeley
score = 0
lives = 6

# Pen om de score weer te geven
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 ", align="right", font=("Courier", 24, "normal"))
pen.write("Levens: 6", align="left", font=("Courier", 24, "normal"))

def update_score():
    pen.clear()
    pen.write("Score: {} Levens: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

def game_over():
    pen.goto(0, 0)
    pen.write("Game Over", align="center", font=("Courier", 36, "normal"))

def reset_game():
    paddle.goto(-350, 0)
    ball.goto(0, 0)
    ball.dx = 0.1
    ball.dy = -0.15

def increase_ball_speed():
    ball.dx *= 1.5
    ball.dy *= 1.5
    ball.color("red")
    ball.shape("circle")

def smaller_paddle():
    paddle.shapesize(stretch_wid=4, stretch_len=1)

# Bal
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.15

# Toetsenbordbinding
wn.listen()
wn.onkeypress(paddle_up, "w")
wn.onkeypress(paddle_down, "s")

while True:
    wn.update()

    # Beweeg de bal
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Detecteer randen van het scherm
    if ball.xcor() > 300 or ball.xcor() < -300:
        ball.dx *= 1
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.dy *= -1
    if ball.xcor() > 300:
        ball.dx *= -1

    # Detecteer botsing met paddle
    if ball.dx < 0 and ball.xcor() < -350:  # ball beweegt naar links en zit bij de linker zijkant.
        if paddle.ycor() - 60 < ball.ycor() < paddle.ycor() + 60:  # bal 'raakt' de bal
            ball.dx *= -1.1  # beweeg de bal de andere kant uit (horizontaal)
            ball.dy *= 0.9  # beweeg de bal de andere kant uit (verticaal)
            score += 1
            if score % 5 == 0:  # Check if the score is a multiple of 5
                increase_ball_speed()
            if score % 10 == 0:  # Check if the score is a multiple of 5
                smaller_paddle()
            update_score()
        else:
            ball.dx = 0
            ball.dy = 0
            lives -= 1
            if lives <=0:
                game_over()
            else:
                reset_game()
                update_score()
                time.sleep(3)
