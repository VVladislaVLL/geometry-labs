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




if __name__ == '__main__':
    points_set = [Point(1, 1), Point(2, 2), Point(3, 0), Point(2, 4), Point(1, 2), Point(3, 5)]

    x_coords = list(map(lambda point: point.x, points_set))
    y_coords = list(map(lambda point: point.y, points_set))
    plt.scatter(x_coords, y_coords)
    plt.show()

    arr = graham_method(points_set)