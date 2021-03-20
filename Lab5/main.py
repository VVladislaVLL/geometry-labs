#!/usr/bin/python
import random
from time import sleep

from Point import Point
from Vector2d import Vector2d, pi
from graph import draw_polygon
from matplotlib import pyplot as plt
from utils import quick_hull, perimeter


def plot_task(points_set, S=40):
    plt.ion()
    flag = True

    while flag:
        plt.clf()

        CH = quick_hull(points_set)
        draw_polygon(CH)
        CH_S = perimeter(CH)

        if CH_S > S:
            # Вроде ошибок явных не видно. Только я не знаю как обрабатывать момент, когда константа заведомо меньше
            # чем периметр. Тогда начинается просто дрочево
            # TODO: ошибка в этот момент, бесконечный цикл
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
