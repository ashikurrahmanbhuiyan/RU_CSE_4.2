import turtle

# Recursive Koch curve function
def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch(t, length, depth - 1)
        t.left(60)
        koch(t, length, depth - 1)
        t.right(120)
        koch(t, length, depth - 1)
        t.left(60)
        koch(t, length, depth - 1)

# Set up screen
screen = turtle.Screen()
screen.bgcolor("gray")

# Create turtle
snowflake = turtle.Turtle()
snowflake.speed(0)
snowflake.color("cyan")
snowflake.pensize(2)
snowflake.penup()
snowflake.goto(-150, 90)
snowflake.pendown()

# Draw the 3 sides of the Koch snowflake
for _ in range(3):
    koch(snowflake, 300, 4)  # (turtle, length, recursion depth)
    snowflake.right(120)

# Finish
snowflake.hideturtle()
turtle.done()
