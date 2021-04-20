#!/usr/bin/python
import random
from time import sleep

from matplotlib import pyplot as plt

from classes.Point import Point
from classes.Vector2d import Vector2d, pi
from divideAndRule2 import divide_and_rule, divide_and_rule
from utils.graph import draw_polygon


def reflect(p, vector_coords):
    # Previous direction
    v = p.direction
    # Polygon side
    q = Vector2d(vector_coords[0], vector_coords[1])

    scal = 2 * (Vector2d.scalar_product(v, q) / Vector2d.scalar_product(q, q))
    prod = Vector2d.s_mult(q, scal)
    new_direction = Vector2d.s_minus(prod, v)
    return new_direction


def plot_task(rectangle, points):
    # TODO: Алгоритм рабочий, надеюсь, что это вообще тот, который нам нужен))
    #  Но я не сделал только отражение от границ прямоугольника
    #  И чтобы точки отображались как круги(но воообще это не должно быть проблемой)
    #  Самая тупая часть - это сделать отражние от стен, хз, как это делать, единсвенный вариант,
    #  который я вижу - это взять алгоритм из 3 лабы
    MIN_DISTANSE = 0.2
    plt.ion()
    s = 1
    while s:
        plt.clf()
        draw_polygon(rectangle)
        clash_flag = divide_and_rule(points)

        if clash_flag[1] <= MIN_DISTANSE:
            clash_flag[0][0].reflect_direction()
            clash_flag[0][1].reflect_direction()

        for i in points:
                i.move()
                plt.scatter(i.x, i.y)

        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(0.002)
        plt.show()

    plt.ioff()
    plt.show()


if __name__ == '__main__':
    # Rectangle
    rectangle = [Point(1, 1), Point(1, 10), Point(15, 10), Point(15, 1)]

    # Our points
    points_set = [Point(2, 2), Point(2, 2.5), Point(4, 2),
                  Point(4, 5), Point(4, 8), Point(6, 2),
                  Point(6,9), Point(8, 5), Point(10,3),
                  Point(11,9), Point(12, 5), Point(12,8)]


    # Test example
    # draw_polygon(rectangle)
    # plt.scatter(list(map(lambda p: p.x, points_set)), list(map(lambda p: p.y, points_set)))
    # Тут как раз создние массива координат
    # points_set_coords = list(map(lambda p: [p.x, p.y], points_set))
    # Если подключишь divideAndRule, то он работает не с точками а с массивом коорднат
    # minPair = divide_and_rule(points_set_coords)
    # Если подключишь divideAndRule2, то он работает не с точками
    # minPair = divide_and_rule(points_set)
    # print(minPair)

    # Set points direction
    for point in points_set:
        point.set_direction(Vector2d.get_vector(random.uniform(0, 2 * pi), 0.1))

    plot_task(rectangle, points_set)



