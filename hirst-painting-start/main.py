# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# list_of_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     list_of_colors.append(color_tuple)
#
#
# print(list_of_colors)
import turtle
from turtle import Turtle, Screen
import random

color_list = [(208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162),
              (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121),
              (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7),
              (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]
tim = Turtle()
tim.hideturtle()
turtle.colormode(255)
tim.speed('fastest')
tim.penup()
position = tim.ycor()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for dot in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()