#!/usr/bin/python

import matplotlib.pyplot as plt
from time import sleep
from classes.Point import Point
from dynamic_hull import *
from classes.Vector2d import Vector2d, pi
from utils.graph import draw_polygon, draw_points


def plot_task(points_set):
    plt.ion()

    length = len(points_set)
    Points = []
    CH = []

    for i in range(0, length):
        plt.clf()
        Points.append(points_set[i])
        draw_points(Points)
        CH = dynamic_hull(points_set[i], CH)
        print("Hull")
        for p in CH:
            print(p)
        draw_polygon(CH)

        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(1)

    plt.ioff()
    plt.show()


if __name__ == '__main__':
    points_set = [Point(1, 1), Point(4, 3), Point(2, 2), Point(4, 5),
                  Point(9, 3), Point(6, 4), Point(3, 0), Point(8, 1),
                  Point(2, 4), Point(1.5, 3), Point(7, 3), Point(10, 7),
                  Point(4, 5)]

    plot_task(points_set)

    plt.show()
