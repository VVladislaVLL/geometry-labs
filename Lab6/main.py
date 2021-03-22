#!/usr/bin/python

import matplotlib.pyplot as plt
from time import sleep
from Point import Point
from grahamMethod import check_point_pos, sorter, get_min_index, diameter_of_set
from graph import draw_line_segment, draw_stack


def plot_task(points_set, D):
    plt.ion()

    # Coordinates for scatter function
    x_coords = list(map(lambda point: point.x, points_set))
    y_coords = list(map(lambda point: point.y, points_set))

    # Copy list
    set_copy = points_set[:]
    stack = []

    # Find Point with min y value
    min_index = get_min_index(points_set)

    # Push this Point in stack
    stack.append(set_copy[min_index])

    # Delete this Point from the list
    del set_copy[min_index]

    # Sort list by polar angle
    set_copy.sort(key=lambda point: sorter(point, stack[0]))

    # Push first Point in stack
    stack.append(set_copy[0])

    # Delete this Point from list
    del set_copy[0]

    # Bypass algorithm
    k = 0
    i = 0

    length = len(set_copy)

    # Algorithm
    while i < length:
        plt.clf()
        if check_point_pos(stack[k], stack[k + 1], set_copy[i]) > 0:
            stack.append(set_copy[i])
            i += 1
            k += 1
        else:
            stack.pop()
            k -= 1

        # Draw current state of stack
        draw_stack(stack)

        # Draw points set
        plt.scatter(x_coords, y_coords)
        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(0.1)

    draw_line_segment(stack[len(stack) - 1], stack[0])
    plt.ioff()
    plt.show()
    return stack


if __name__ == '__main__':
    points_set = [Point(1, 1), Point(4, 3),Point(2, 2), Point(4, 5),
                  Point(9, 3), Point(6, 4), Point(3, 0), Point(8, 1),
                  Point(2, 4), Point(1.5, 3), Point(7, 3), Point(10, 7),
                  Point(4, 5)]

    D = 5
    # stack = plot_task(points_set, D)
    stack = [Point(8,1), Point(11,6), Point(6,3), Point(3,5), Point(1,1), Point(3,2),]
    a = diameter_of_set(stack)
    print(a)
    plt.show()


