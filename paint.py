from turtle import *

v = 100
step = 17

t = Turtle()
t.width(5)
t.color('black')
t.shape('circle')
t.pendown()
t.speed(v)

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def circler():
    t.circle(50)

def erase():
    t.clear()

def default():
    t.color('black')

def setRed():
    t.color('red')

def setGreen():
    t.color('green')

def setBlue():
    t.color('blue')

def setYellow():
    t.color('yellow')

def setOrange():
    t.color('orange')

def setPurple():
    t.color('purple')

def setLime():
    t.color('lime')

def setCyan():
    t.color('cyan')

def setSilver():
    t.color('silver')

def setWhite():
    t.color('white')

def stepUp():
    t.goto(t.xcor(), t.ycor() + step)

def stepDown():
    t.goto(t.xcor(), t.ycor() - step)

def stepLeft():
    t.goto(t.xcor() - step, t.ycor())

def stepRight():
    t.goto(t.xcor() + step, t.ycor())

def beginFill():
    t.begin_fill()

def endFill():
    t.end_fill()

def blackening():
    scr.bgcolor('black')
    
def whitening():
    scr.bgcolor('white')    

t.ondrag(draw)

scr = t.getscreen()
scr.onscreenclick(move)

scr.onkey(default, 'D')
scr.onkey(setRed, 'r')
scr.onkey(setBlue, 'b')
scr.onkey(setGreen, 'g')
scr.onkey(setYellow, 'y')
scr.onkey(setOrange, 'o')
scr.onkey(setPurple, 'p')
scr.onkey(setLime, 'l')
scr.onkey(setCyan, 'c')
scr.onkey(setSilver, 's')
scr.onkey(setWhite, 'w')

scr.onkeypress(beginFill, 'f')
scr.onkeyrelease(endFill, 'f')


scr.onkey(stepUp, 'Up')
scr.onkey(stepDown, 'Down')
scr.onkey(stepLeft, 'Left')
scr.onkey(stepRight, 'Right')

scr.onkey(circler, 'C')
scr.onkey(erase, 'Delete')
scr.onkeypress(blackening, 'space')
scr.onkeyrelease(whitening, 'space')
scr.onkeypress(NInk, 'Tab')
scr.onkeyrelease(Ink, 'Tab')

scr.listen()
done()
