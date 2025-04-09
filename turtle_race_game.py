import turtle
import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
answer = screen.textinput(prompt="Who will win?", title="Make your bet")


colours = ["red", "blue", "green", "pink", "brown", "grey"]
y_position = [-80, -40, 0, 40, 80, 120]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

if answer:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
          is_race_on = False
          winning_colour = turtle.pencolor()
          if winning_colour == answer:
            print("You won!")
          else:
            print("You lost!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()