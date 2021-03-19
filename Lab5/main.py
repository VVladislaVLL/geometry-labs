#!/usr/bin/python
import random
from time import sleep

from Point import Point
from Vector2d import Vector2d, pi
from graph import draw_polygon
from matplotlib import pyplot as plt
from utils import quick_hull


def reflect(p, vector_coords):
    # Implementation of a formula
    # new_V = 2 * scalar_prod(V, Q) / scalar_prod(Q, Q) * Q - V

    # Previous direction
    v = p.direction
    # Polygon side
    q = Vector2d(vector_coords[0], vector_coords[1])

    scal = 2 * (Vector2d.scalar_product(v, q) / Vector2d.scalar_product(q, q))
    prod = Vector2d.s_mult(q, scal)
    new_direction = Vector2d.s_minus(prod, v)
    return new_direction


def plot_task(P, Q, points):
    plt.ion()
    s = 0
    for p in points:
        s += p.speed

    while s:
        plt.clf()

        s = 0
        for p in points:
            s += p.speed

        draw_polygon(P)
        draw_polygon(Q)

        for i in points:
            flag_angle = angle_test(Q, i.get_next_state())
            flag_binary = binary_test(P, i.get_next_state())['flag']
            if not flag_binary:
                plt.scatter(i.x, i.y)
                coords_binary = binary_test(P, i.get_next_state())['points']
                new_direction = reflect(i, coords_binary)
                i.direction = new_direction
            elif flag_angle:
                i.speed = 0
            else:
                i.move()
                plt.scatter(i.x, i.y)

        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(0.000001)

    plt.ioff()
    plt.show()


if __name__ == '__main__':

    points_set = [Point(1, 1), Point(4, 3), Point(2, 2), Point(4, 5),
                  Point(9, 3), Point(6, 4), Point(3, 0), Point(8, 1),
                  Point(2, 4), Point(1.5, 3), Point(7, 3), Point(10, 7),
                  Point(4, 5)]
    quick_hull(points_set)

    # Set points direction
    # for point in points_set:
    #     point.set_direction(Vector2d.get_vector(random.uniform(0, 2 * pi), 0.1))
    #
    # plot_task(points_set)
