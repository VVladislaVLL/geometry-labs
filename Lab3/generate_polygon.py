import random
from math import *

from classes import Vector, Point
from graph import draw_line, draw_point


def get_random_position(radius, err_radius, cord_center):
    return round(random.random(), 1) * err_radius + radius + cord_center


def generate_polygon(cord_center_x, cord_center_y, radius):
    # Array of polygon points
    arr = []

    # Number of polygon vertexes
    number_of_vertex = random.randrange(3, 10, 1)
    print('Number of vertexes')
    print(number_of_vertex)
    # Average rotation alfa
    alfa = 2 * pi / number_of_vertex

    # Rotation error alfa
    err_alfa = alfa / 100 * 10

    # Radius error
    err_radius = radius / 100 * 10

    # Rotation center
    center_point = Point(cord_center_x, cord_center_y)

    # First polygon point
    start_point = Point(get_random_position(radius, err_radius, cord_center_x), cord_center_y)
    main_vector = Vector(center_point, start_point)
    # arr.append(Point(round(main_vector.p2.x, 2), round(main_vector.p2.y, 2)))
    i = 0
    while i < number_of_vertex:
        main_vector.rotate(alfa + err_alfa * random.randrange(-1, 1, 1))
        round_x = round(main_vector.p2.x, 2)
        round_y = round(main_vector.p2.y, 2)
        point = Point(round_x, round_y)
        arr.append(point)
        print('Appended point: ' + str(1+i))
        point.print_point()
        i += 1
    return arr


def draw_polygon(canv, arr):
    i = 0
    j = 1
    while i < len(arr) - 1:
        draw_line(canv, arr[i], arr[j])
        i = j
        j += 1

    draw_line(canv, arr[-1], arr[0])

    for k in range(0, len(arr)):
        text = 'P' + str(k + 1)
        draw_point(canv, arr[k], text)
