#!/usr/bin/python

from time import sleep

import matplotlib.pyplot as plt

from Point import Point
from grahamMethod import graham_method



def plot_task(points):
    plt.ion()
    s = 0
    while s:
        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(0.0001)

    plt.ioff()
    plt.show()


def draw_polygon(polygon):
    cor_x = list(map(lambda p: p.x, polygon))
    cor_y = list(map(lambda p: p.y, polygon))
    cor_x.append(polygon[0].x)
    cor_y.append(polygon[0].y)
    plt.plot(cor_x, cor_y)


if __name__ == '__main__':
    points_set = [Point(1, 1), Point(4, 3),Point(2, 2), Point(4, 5), Point(9, 3), Point(6, 4), Point(3, 0), Point(8, 1), Point(2, 4), Point(1.5, 3), Point(3, 5)]

    x_coords = list(map(lambda point: point.x, points_set))
    y_coords = list(map(lambda point: point.y, points_set))
    plt.scatter(x_coords, y_coords)
    arr = graham_method(points_set)
    draw_polygon(arr)
    plt.show()

