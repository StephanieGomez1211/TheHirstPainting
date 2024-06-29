import turtle as t
from turtle import Turtle, Screen
import random

#### GET COLOR OF AN IMAGE ####
# import colorgram
#
# rgb_color = []
# colors = colorgram.extract("image.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)
#################################


colorlist = [(253, 247, 249), (250, 228, 16), (236, 251, 244),
             (212, 13, 9), (199, 12, 36), (230, 228, 6), (196, 70, 20), (32, 90, 188),
             (235, 148, 38), (43, 212, 70), (33, 30, 152), (16, 22, 54), (67, 9, 48),
             (244, 39, 150), (14, 206, 223), (238, 244, 249), (66, 202, 229), (62, 21, 10),
             (225, 19, 111), (15, 155, 21), (228, 166, 9), (248, 11, 9), (245, 58, 16),
             (98, 75, 9), (223, 140, 203), (68, 240, 160), (10, 97, 62), (6, 39, 33),
             (68, 219, 157)]

hirst = Turtle()
hirst.hideturtle()
# hirst.screen.screensize(400,400)
STARTING_POSITION_X = -300
STARTING_POSITION_Y = -200
SIZE = 10
# X_SIZE = 10
# Y_SIZE = 10
hirst.teleport(STARTING_POSITION_X, STARTING_POSITION_Y)
hirst.penup()
t.colormode(255)
hirst.screen.bgcolor((253, 250, 247))
hirst.screen.setup (width=900, height=700, startx=-400, starty=-200)
hirst.speed("fastest")
def row_dot():
    for _ in range(SIZE):
        hirst.dot(30,random.choice(colorlist))
        hirst.forward(60)

row_pos = 0
for _ in range(SIZE):
    row_dot()
    row_pos += 50
    hirst.teleport(STARTING_POSITION_X, STARTING_POSITION_Y + row_pos)

screen = Screen()
screen.exitonclick()