import turtle
import time

box = turtle.Turtle()
star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

box.forward(100)
time.sleep(5)

box.right(90)
box.forward(100)
time.sleep(5)

box.right(90)
box.forward(200)
time.sleep(5)

box.right(90)
box.forward(100)
time.sleep(5)

box.right(90)
box.forward(100)

turtle.done()
