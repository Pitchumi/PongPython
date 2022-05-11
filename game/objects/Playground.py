import turtle

score_a = 0
score_b = 0
pen = turtle.Turtle()
screen = turtle.Screen()


def initialisation_pen():
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(""
              "Player A: 0\t"
              "Player B: 0",
              align="center",
              font=("Courier", 24, "normal")
              )


def initialisation_screen():
    screen.title("Pong Me If You Can")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)
    screen.listen()
    return screen


