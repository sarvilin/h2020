import turtle
import math
import turtle as t
t.setup(width=800, height=600, startx=0, starty=100)


def square1():
    side = 10
    for i in range(5):
        t.shape('turtle')
        for itr in range(4):
            t.forward(side)
            turtle.left(90)
        t.penup()
        t.right(135)
        t.forward(20)
        t.left(135)
        t.pendown()
        print(turtle.pos())
        side += 27
    t.clearscreen()


def spider(lng):
    turtle.shape('turtle')
    for i in range(12):
        turtle.forward(lng)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(lng)
        turtle.right(150)
    turtle.clearscreen()


def spir():
    s = 3
    rad = 7
    t.shape('turtle')
    for i in range(300):
        t.forward(s)
        t.left(rad)
        rad -= 0.02
        if rad <= 0:
            rad = 0
    t.clearscreen()


def square2():
    s = 15
    turtle.shape('turtle')
    for i in range(35):
        turtle.forward(s)
        turtle.left(90)
        s += 5
    turtle.clearscreen()


def mnogo():
    turtle.shape('turtle')
    r = 30
    for ugol in range(3, 12):
        turtle.left(90)
        turtle.left(180 / ugol)
        for i in range(ugol):
            turtle.forward(r * 2 * math.sin(math.radians(360 / (2 * ugol))))
            turtle.left(360 / ugol)
        turtle.right(90 + 180 / ugol)
        turtle.penup()
        turtle.forward(15)
        turtle.pendown()
        r += 15
    turtle.clearscreen()


def cvetok():
    turtle.shape('turtle')
    for cycle in range(3):
        for i in range(36):
            turtle.forward(4)
            turtle.left(10)
        for i in range(36):
            turtle.forward(4)
            turtle.right(10)
        turtle.left(60)
    turtle.clearscreen()


def byterfly():
    turtle.shape('turtle')
    lenght = 4
    turtle.left(90)
    for cycle in range(6):
        for i in range(36):
            turtle.forward(lenght)
            turtle.left(10)
        for i in range(36):
            turtle.forward(lenght)
            turtle.right(10)
        lenght += 1
    turtle.clearscreen()


def pruzina():
    turtle.shape('turtle')
    turtle.left(90)
    for vit in range(3):
        for i in range(72):
            turtle.forward(2)
            turtle.right(2.5)
        for i in range(72):
            turtle.forward(0.4)
            turtle.right(2.5)
    turtle.penup()
    turtle.setposition(00.00, 00.00)
    turtle.pendown()
    turtle.clearscreen()


def smile():
    def krug(diametr, color):
        turtle.shape('turtle')
        turtle.begin_fill()
        turtle.left(90)
        for i in range(72):
            turtle.forward(diametr)
            turtle.left(5)
        turtle.color(color)
        turtle.end_fill()
        turtle.color('black')

    def duga(diametr_duga):
        turtle.shape('turtle')
        turtle.right(90)
        for i in range(36):
            turtle.forward(diametr_duga)
            turtle.right(5)
    krug(6, 'yellow')
    turtle.penup()
    turtle.setposition(-100.00, 40.00)
    turtle.pendown()
    krug(1, 'blue')
    turtle.penup()
    turtle.setposition(-50.00, 29.00)
    turtle.pendown()
    krug(1, 'blue')
    turtle.penup()
    turtle.setposition(-70.00, 10.00)
    turtle.pendown()
    turtle.width(8)
    turtle.forward(20)
    turtle.penup()
    turtle.setposition(-35.00, -20.00)
    turtle.pendown()
    turtle.left(90)
    turtle.color('red')
    duga(3)


select = input('Select program')
if int(select) == 5:
   square1()
elif int(select) == 6:
   spider(75)
elif int(select) == 13:
   smile()
'''
spir()
square2()
mnogo()
cvetok()
byterfly()
pruzina()
smile()
'''
