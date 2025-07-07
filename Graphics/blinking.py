import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Blinking Stars in the Night Sky")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic updates

# Create turtle for drawing stars
star_turtle = turtle.Turtle()
star_turtle.hideturtle()
star_turtle.penup()
star_turtle.speed(0)
star_turtle.color("white")

# Generate random star positions
num_stars = 50
stars = [(random.randint(-390, 390), random.randint(-290, 290)) for _ in range(num_stars)]

def draw_star(x, y, size=5):
    star_turtle.goto(x, y)
    star_turtle.dot(size, "white")

def clear_star(x, y, size=6):
    star_turtle.goto(x, y)
    star_turtle.dot(size, "black")

# Main blinking loop
try:
    while True:
        for x, y in stars:
            if random.random() < 0.5:
                draw_star(x, y)
            else:
                clear_star(x, y)
        screen.update()
        time.sleep(0.3)
except turtle.Terminator:
    print("Exited.")
