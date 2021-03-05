import random

import matplotlib.pyplot as plt
from lab1_1 import Point
from lab1_3 import draw_figure
from lab2 import is_inside


def test_inside(func,
                figure=[Point(-1, -1), Point(-5, 3), Point(0, 11), Point(6, 13), Point(10, 4.5), Point(4, -3)],
                range_number=100):
    draw_figure(figure)
    random.seed(1)
    mistakes_counter = 0
    for i in range(range_number):
        given_point = Point(random.randint(-5, 10), random.randint(-5, 10))  # -2,0
        func_value = func(figure, given_point)
        standard_value = is_inside(figure, given_point)
        if func_value != standard_value:
            print("ABORT", given_point, "Returned:", func_value, "Expected:", standard_value)
            plt.plot(given_point.x, given_point.y, 'ro', color=(0.5, 0.5, 0.5), markersize=5)
            continue
            mistakes_counter += 1
        if func_value == "on":
            plt.plot(given_point.x, given_point.y, 'ro', color=(0, 0, 0), markersize=4)
        elif func_value == "inside":
            plt.plot(given_point.x, given_point.y, 'ro', markersize=4)
        else:
            plt.plot(given_point.x, given_point.y, 'ro', color=(0, 0.5, 0.3), markersize=4)
    print("There is no incompatibilities" if mistakes_counter == 0 else str(mistakes_counter) + " incompatibilities")
    plt.show()
