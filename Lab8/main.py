#!/usr/bin/python

import pylab
import matplotlib.patches
import matplotlib.lines
import matplotlib.path
import matplotlib.pyplot as plt
from time import sleep
from classes.Point import Point
from classes.Vector2d import Vector2d


def draw_polygons(axes, first_polygon, second_polygon):
    polygon_1 = matplotlib.patches.Polygon([(first_polygon[0].x, first_polygon[0].y),
                                             (first_polygon[1].x, first_polygon[1].y),
                                             (first_polygon[2].x, first_polygon[2].y),
                                             (first_polygon[3].x, first_polygon[3].y),
                                             (first_polygon[4].x, first_polygon[4].y),
                                             (first_polygon[5].x, first_polygon[5].y),
                                             (first_polygon[6].x, first_polygon[6].y)],
                                            color="g")
    axes.add_patch(polygon_1)

    polygon_2 = matplotlib.patches.Polygon([(second_polygon[0].x, second_polygon[0].y),
                                             (second_polygon[1].x, second_polygon[1].y),
                                             (second_polygon[2].x, second_polygon[2].y),
                                             (second_polygon[3].x, second_polygon[3].y),
                                             (second_polygon[4].x, second_polygon[4].y),
                                             (second_polygon[5].x, second_polygon[5].y)],
                                            fill='b')
    axes.add_patch(polygon_2)


def plot_task(axes, first_polygon, second_polygon):
    plt.ion()
    i = 10
    while not i == 0:
        plt.clf()
        # for point in first_polygon:
        #     point.move()
        #
        # for point in second_polygon:
        #     point.move()

        draw_polygons(axes, first_polygon, second_polygon)
        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(0.2)
        i -= 1

    plt.ioff()
    plt.show()


if __name__ == '__main__':
    pylab.xlim(-1, 24)
    pylab.ylim(-2, 10)

    first_polygon = [Point(5, -1), Point(2, 1), Point(1, 3), Point(3, 6), Point(6, 6), Point(8, 4), Point(8, 1)]
    # Set Direction
    speed = 0.25
    for point in first_polygon:
        point.set_direction([Vector2d(speed * 1, 0), speed])

    second_polygon = [Point(16, 2), Point(13, 4), Point(13, 7), Point(16, 9), Point(20, 6), Point(21, 4)]
    for point in second_polygon:
        point.set_direction([Vector2d(speed * -1, 0), speed])

    # Получим текущие оси
    axes = pylab.gca()
    axes.set_aspect("equal")
    draw_polygons(axes, first_polygon, second_polygon)

    # plot_task(axes, first_polygon, second_polygon)
    plt.show()  # if you need...
