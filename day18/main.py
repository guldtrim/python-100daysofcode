import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.speed(10)
tim.pensize(1)
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)


for i in range (101):
    tim.right(5)
    tim.color(random_color())
    tim.circle(100)











screen = Screen()
screen.exitonclick()
