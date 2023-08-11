import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")
timmy.color("blue4")
timmy.forward(100)
timmy.forward(-200)
print(timmy.heading())
print(timmy.position())

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()