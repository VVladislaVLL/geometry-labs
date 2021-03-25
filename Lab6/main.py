#!/usr/bin/python
import random
import matplotlib.pyplot as plt
from classes.Point import Point
from classes.Vector2d import Vector2d, pi
from diameter import diameter_of_set
from jarvis import *
from utils.graph import draw_polygon
from time import sleep


def plot_task(points_set, S=12):
    plt.ion()
    flag = True

    while flag:
        plt.clf()

        CH = jarvis_method(points_set)
        draw_polygon(CH)
        D = diameter_of_set(CH)

        print(D)
        if D > S:
            for p in CH:
                p.reflect_direction()
        for p in points_set:
            p.move()
            plt.scatter(p.x, p.y)

        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(0.0001)

    plt.ioff()
    plt.show()


if __name__ == '__main__':
    points_set = [Point(1, 1), Point(4, 3),Point(2, 2), Point(4, 5),
                  Point(9, 3), Point(6, 4), Point(3, 0), Point(8, 1),
                  Point(2, 4), Point(1.5, 3), Point(7, 3), Point(10, 7),
                  Point(4, 5)]

    # Set points direction
    for point in points_set:
        point.set_direction(Vector2d.get_vector(random.uniform(0, 2 * pi), 0.1))

    # p_x = list(map(lambda p: p.x, points_set))
    # p_y = list(map(lambda p: p.y, points_set))
    # plt.scatter(p_x, p_y)

    # ch = jarvis_method(points_set)
    # draw_polygon(ch)
    plot_task(points_set)
    # print(diameter_of_set(ch))
    plt.show()


