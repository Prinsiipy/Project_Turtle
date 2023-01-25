import time
from turtle import *

pen = Turtle()
pen.color('red')
bgcolor('black')

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def draw_heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def draw_txt():
    pen.up()
    pen.setpos(-60, 90)
    pen.down()
    pen.color('white')
    pen.write("Люблю тебя", font=("Montserrat", 16, "bold"))

draw_heart()
draw_txt()
pen.ht()
done()