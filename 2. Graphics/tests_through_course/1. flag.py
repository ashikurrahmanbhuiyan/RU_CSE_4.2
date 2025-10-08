import turtle

screen = turtle.Screen()
screen.setup(width=800, height=480)
screen.bgcolor("green")
screen.title("Flag of Bangladesh")

flag = turtle.Turtle()
flag.speed(0)
flag.hideturtle()
flag.penup()


flag.goto(0,-90)
flag.color("red")
flag.begin_fill()
flag.circle(120)
flag.end_fill()


turtle.done()
