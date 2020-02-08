import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

iniLineLen  = 500;

myWin.setworldcoordinates(0, 0, iniLineLen, iniLineLen);

myTurtle.speed('fast')
myTurtle.penup()
myTurtle.goto(0, iniLineLen)
myTurtle.pendown()



def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,iniLineLen)
myWin.exitonclick()


