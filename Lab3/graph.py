from tkinter import constants
from math import *
import random


def create_coordinate_system(canv):
    # Coordinate axes
    canv.create_line(500, 1000, 500, 0, width=2, arrow=constants.LAST)
    canv.create_line(0, 500, 1000, 500, width=2, arrow=constants.LAST)

    canv_width = 1000
    canv_height = 1000

    while canv_width > 0:
        canv.create_line(495, canv_height, 505, canv_height, width=2)
        canv.create_line(canv_width, 495, canv_width, 505, width=2)
        canv_width -= 50
        canv_height -= 50


def draw_point(canv, point, text, shift=-15):
    canv.create_oval(
        point.change_system().x - 2,
        point.change_system().y - 2,
        point.change_system().x + 2,
        point.change_system().y + 2,
        fill='black',
        outline='black'
    )

    canv.create_text(
        point.change_system().x + shift,
        point.change_system().y + shift,
        text=(text + ' (' + str(point.x) + ', ' + str(point.y) + ')'),
        justify=constants.CENTER
    )


def draw_line(canv, point1, point2):
    canv.create_line(
        point1.change_system().x,
        point1.change_system().y,
        point2.change_system().x,
        point2.change_system().y,
        width=2
    )


def clip(x, min, max):
    if min > max:
        return x
    elif x < min:
        return min
    elif x > max:
        return max
    else:
        return x
