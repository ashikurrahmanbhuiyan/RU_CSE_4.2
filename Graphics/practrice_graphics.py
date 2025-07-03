# # Python program to draw star
# # using Turtle Programming
# import turtle
# star = turtle.Turtle()

# for i in range(3):
#     star.right(120)
#     star.forward(100)
    
# turtle.done()


# importing package
# import turtle
# turtle.speed(100)

# # Loop for pattern
# for i in range(1000):
  
#   # move the turtle forward by 
#   # 100+variable unit distance
#   # in the direction of head of
#   # turtle
#   turtle.forward(2*i)
  
#   # change the direction of turtle
#   # by 90 degrees to the left.
#   turtle.left(120)

# turtle.done()



# import turtle library
# import turtle             
# my_wn = turtle.Screen()
# turtle.speed(20)
# for i in range(30):
#    turtle.circle(5*i)
#    turtle.circle(-5*i)
#    turtle.left(i)
# turtle.exitonclick()





# import turtle library
import turtle             
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
turtle.speed(10000)
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)
turtle.done()