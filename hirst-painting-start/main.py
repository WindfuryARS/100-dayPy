import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(list(color.rgb))

# print(rgb_colors)

new_color_list = []
for nl in rgb_colors:
    new_color_list.append(tuple(nl))
# print(new_color_list)


zhanma = Turtle()


# turtle.shape("turtle")
# turtle.penup()
# turtle.fd(50)
# turtle.pendown()
# turtle.pencolor(new_color_list[0])
# turtle.dot(20)
# turtle.penup(); turtle.fd(50)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(new_color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()