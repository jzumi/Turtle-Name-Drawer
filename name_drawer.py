"""
Module: name_drawer

A program to draw a name using one (or more) turtles.

Authors:
9/16/2022
1) JT - jtumlos@sandiego.edu
2) Aiden - aidenhill@sandiego.edu
"""
import turtle
window = turtle.Screen()

#We made the turtle blue and named the variable the name we are going to write
#We also included a user input to determine what color the text will be
jt = turtle.Turtle()
turtle_color = (input("What color would you like the text to be? "))

#This changes the pen color to the user's desired color and the shape to a turtle
jt.color(str(turtle_color))
jt.shape("turtle")
jt.pensize(5)

#These lines of code writes the first letter J
jt.forward(50)
jt.right(90)
jt.forward(100)
jt.right(90)
jt.forward(75)
jt.right(90)
jt.forward(25)
jt.penup()

#These lines of code moves the pen for the next letter
jt.forward(75)
jt.right(90)
jt.forward(125)
jt.pendown()

#These lines of code writes the final letter T
jt.forward(50)
jt.forward(-25)
jt.right(90)
jt.forward(100)

yay = input("Are you satisfied? y or n: ")

#Because my name is short, I drew a smiley face!
if yay == "y": 

    jt.penup()
    jt.forward(50)
    jt.right(90)
    jt.forward(100)
    jt.pendown()
    jt.left(90)
    jt.forward(20)
    jt.penup()

    jt.left(90)
    jt.forward(50)
    jt.left(90)
    jt.pendown()
    jt.forward(20)
    jt.penup()

    #This makes the mouth of the smiley face
    jt.forward(-40)
    jt.right(180)
    jt.pendown()
    jt.forward(40)
    jt.right(90)
    jt.forward(50)
    jt.right(90)
    jt.forward(40)


#This allows the screen to close after a user click
turtle.exitonclick()


