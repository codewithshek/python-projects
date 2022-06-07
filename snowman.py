# follow data._.pirates
import turtle
turtle.speed(2)
turtle.setup(800, 700)
turtle.bgcolor("black")
# Blue Background
turtle.penup()
turtle.goto(0, -320)
turtle.pendown()
turtle.color("#c1f8b5")
turtle.begin_fill()
turtle.circle(320)
turtle.end_fill()
 
# Bottom of body
turtle.penup()
turtle.goto(0, -280)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(110)
turtle.end_fill()
 
# Middle of body
turtle.penup()
turtle.goto(0, -110)
turtle.pendown()
turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()
 
# Head of Snowman
turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()
 
# Function to draw 1 small black circle
def black_circle():
	turtle.color("black")
	turtle.begin_fill()
	turtle.circle(10)
	turtle.end_fill()
 
# Eyes
x = -20
for i in range(2):
	turtle.penup()
	turtle.goto(x, 110)
	turtle.pendown()
	black_circle()
	x = x + 40
 
# Buttons
y = 0
for i in range(5):
	turtle.penup()
	turtle.goto(0, y)
	turtle.pendown()
	black_circle()
	y = y - 55
 
# Mouth
turtle.penup()
turtle.goto(0,70)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(17)
turtle.end_fill()
 
turtle.penup()
turtle.goto(0,75)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(17)
turtle.end_fill()
 
# Right Arm
turtle.penup()
turtle.goto(75, 0)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
turtle.left(40)
for i in range(2):
	turtle.forward(75)
	turtle.left(90)
	turtle.forward(7)
	turtle.left(90)
turtle.end_fill()
 
# Right Finger 1
turtle.penup()
turtle.goto(115, 38)
turtle.pendown()
turtle.begin_fill()
turtle.left(40)
for i in range(2):
	turtle.forward(25)
	turtle.left(90)
	turtle.forward(5)
	turtle.left(90)
turtle.end_fill()
 
# Right Finger 2
turtle.begin_fill()
turtle.right(100)
for i in range(2):
	turtle.forward(25)
	turtle.left(90)
	turtle.forward(5)
	turtle.left(90)
turtle.end_fill()
 
# Left Arm
turtle.penup()
turtle.goto(-130, 50)
turtle.pendown()
turtle.begin_fill()
turtle.right(10)
for i in range(2):
	turtle.forward(75)
	turtle.right(90)
	turtle.forward(7)
	turtle.right(90)
turtle.end_fill()
 
# Left Finger 1
turtle.penup()
turtle.goto(-112, 58)
turtle.pendown()
turtle.begin_fill()
turtle.right(40)
for i in range(2):
	turtle.forward(25)
	turtle.right(90)
	turtle.forward(5)
	turtle.right(90)
turtle.end_fill()
 
# Left Finger 2
turtle.begin_fill()
turtle.right(100)
turtle.penup()
turtle.goto(-108, 31)
turtle.pendown()
for i in range(2):
	turtle.forward(25)
	turtle.right(90)
	turtle.forward(5)
	turtle.right(90)
turtle.end_fill()
 
# Hat
turtle.penup()
turtle.goto(50, 150)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.right(10)
turtle.forward(100)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.end_fill()
 
# Text on Screen
turtle.penup()
turtle.goto(130, -230)
turtle.pendown()
turtle.color("blue")
turtle.write("data._.pirates", font=("Arial", 7, "bold"))
 
