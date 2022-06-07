# follow data._.pirates
# Import turtle package
import turtle


# Creating a turtle object(vr)
vr = turtle.Turtle()

#set the Back Ground color
turtle.Screen().bgcolor('black')
# set the pen size
turtle.pensize(4)
vr.speed (10)

# Defining a method to draw curve
def drawcurve():
    for i in range(200):
        # Defining step by step curve motion
        vr.right(1)
        vr. forward(1)
        


# Set the fill color to pink and border color to Red
vr.color('red', 'pink')
 # Start filling the color
vr.begin_fill()
vr.left(140)

 # Draw the left line
vr.forward(111.65)
# Draw the left curve
drawcurve()
vr.left(120)
drawcurve()
 # Draw the right line
vr.forward(111.65)
 # end_fill() : This method fills the polygon with the current fill color by closing it between the current position and the initial position.
vr.end_fill()
vr.penup()
vr.goto(77, -40)
vr.pendown()
vr.hideturtle()
turtle.done()