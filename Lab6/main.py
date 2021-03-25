#!/usr/bin/python

import matplotlib.pyplot as plt
from classes.Point import Point
from jarvis import *
from utils.graph import draw_polygon

if __name__ == '__main__':
    points_set = [Point(1, 1), Point(4, 3),Point(2, 2), Point(4, 5),
                  Point(9, 3), Point(6, 4), Point(3, 0), Point(8, 1),
                  Point(2, 4), Point(1.5, 3), Point(7, 3), Point(10, 7),
                  Point(4, 5)]

    p_x = list(map(lambda p: p.x, points_set))
    p_y = list(map(lambda p: p.y, points_set))
    plt.scatter(p_x, p_y)

    ch = jarvis_method(points_set)
    draw_polygon(ch)
    plt.show()


