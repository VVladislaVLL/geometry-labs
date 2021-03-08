#!/usr/bin/python
import copy
import random
from time import sleep

from Point import Point
from Vector2d import Vector2d, pi
from graph import draw_polygon
from matplotlib import pyplot as plt
from utils import binary_test, angle_test, is_intersect


def find_intersection(current, prev, polygon):
    i = 0
    length = len(polygon)
    print(length)
    point1_i = 0
    point2_i =0
    while i < length:
        # if is_intersect(current, prev, polygon[i], polygon[0 if i >= length else i + 1]):
        #     break
        # TODO: check this part of code
        if i + 1 >= length and i < length:
            if is_intersect(current, prev, polygon[i], polygon[0]):
                point1_i = i
                point2_i = 0
                break
        else:
            if is_intersect(current, prev, polygon[i], polygon[i + 1]):
                point1_i = i
                point2_i = i + 1
                break
        i += 1
    # TODO: invalid index
    return [polygon[point1_i], polygon[point2_i]]


def reflect(p, vector_coords):
    v = p.direction
    q = Vector2d(vector_coords[0], vector_coords[1])
    scal = Vector2d.scalar_product(v, q) / (q.get_module() ** 2)
    scal *= 2
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
            flag_angle = angle_test(Q, i)
            flag_binary = binary_test(P, i)
            if flag_angle or not flag_binary:
                prev = i.get_prev_state()
                # i.speed = 0
                plt.scatter(i.x, i.y)
                coords = []
                # if flag_angle == True and flag_binary == True:
                #     coords = find_intersection(i, prev, P)
                # elif flag_angle == False and flag_binary == False:
                #     coords = find_intersection(i, prev, Q)
                coords = find_intersection(i, prev, P)
                new_direction = reflect(i, coords)
                i.direction = new_direction
            else:
                i.move()
                plt.scatter(i.x, i.y)

        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(0.0001)

    plt.ioff()
    plt.show()


if __name__ == '__main__':

    # Polygons
    big_polygon = [Point(1, 1), Point(1, 2), Point(3, 7), Point(5, 8), Point(8, 9),
        Point(10, 8), Point(13, 4), Point(13, 3), Point(12, 1)]

    small_polygon = [Point(3, 3), Point(4, 4), Point(6, 4), Point(7, 6), Point(9, 6),
                     Point(7, 2), Point(6, 3)]

    # Our points
    # points_set = [Point(2, 2),Point(4, 2), Point(4, 5), Point(4, 6), Point(6, 6),
    #               Point(6, 8), Point(10, 2), Point(12, 2), Point(4, 5), Point(10, 6)]

    points_set = [Point(4, 2)]

    # Set points direction
    for point in points_set:
        point.set_direction(Vector2d.get_vector(random.uniform(0, 2 * pi), 0.1))

    # Get points coordinates
    points_coordinates = [[point.x for point in points_set], [point.y for point in points_set]]

    # Draw points and polygons
    # mat, = ax.plot(points_coordinates[0], points_coordinates[1], 'o', markersize=5)

    plot_task(big_polygon, small_polygon, points_set)
    # Animate points
    # anim = FuncAnimation(fig, animate_points)
    plt.show()
