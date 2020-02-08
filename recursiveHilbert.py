
import sys
from turtle import Turtle, Screen

def hilbert_curve(n, turtle, angle=90):
    if n <= 0:
        return

    turtle.left(angle)
    hilbert_curve(n - 1, turtle, -angle)
    turtle.forward(1)
    turtle.right(angle)
    hilbert_curve(n - 1, turtle, angle)
    turtle.forward(1)
    hilbert_curve(n - 1, turtle, angle)
    turtle.right(angle)
    turtle.forward(1)
    hilbert_curve(n - 1, turtle, -angle)
    turtle.left(angle)

depth = 5 #int(sys.argv[1])
size = 2 ** depth

screen = Screen()
screen.setworldcoordinates(0, 0, size, size)

yertle = Turtle('turtle')
yertle.speed('fastest')
yertle.penup()
yertle.goto(0.5, 0.5)
yertle.pendown()

hilbert_curve(depth, yertle)

yertle.hideturtle()
screen.exitonclick()




