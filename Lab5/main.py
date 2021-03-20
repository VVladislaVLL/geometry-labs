#!/usr/bin/python
import random
from time import sleep

from Point import Point
from Vector2d import Vector2d, pi
from graph import draw_polygon
from matplotlib import pyplot as plt
from utils import quick_hull, perimeter


def plot_task(points_set, S=45):
    plt.ion()
    s = 0
    for p in points_set:
        s += p.speed


    while s:
        plt.clf()

        s = 0
        for p in points_set:
            s += p.speed

        CH = quick_hull(points_set)
        draw_polygon(CH)
        CH_S = perimeter(CH)

        if CH_S > S:
            # TODO: ошибка в этот момент, бесконечный цикл
            for p in CH:
                # plt.scatter(p.x, p.y)
                p.reflect_direction()
                # print(p)
        else:
            for p in points_set:
                p.move()
                # plt.scatter(p.x, p.y)

        for p in points_set:
            plt.scatter(p.x, p.y)

        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(0.01)

    plt.ioff()
    plt.show()


if __name__ == '__main__':

    points_set = [Point(1, 1), Point(4, 3), Point(2, 2), Point(4, 5),
                  Point(9, 3), Point(6, 4), Point(3, 0), Point(8, 1),
                  Point(2, 4), Point(1.5, 3), Point(7, 3), Point(10, 7),
                  Point(4, 5)]

    # Set points direction
    for point in points_set:
        point.set_direction(Vector2d.get_vector(random.uniform(0, 2 * pi), 0.1))

    # CH = quick_hull(points_set)
    # draw_polygon(CH)
    # for p in points_set:
    #     plt.scatter(p.x, p.y)
    # plt.show()

    plot_task(points_set)
