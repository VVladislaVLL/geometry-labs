import random

import matplotlib.pyplot as plt
from lab1_1 import Point
from lab1_3 import draw_figure


def test_inside(func,
                figure = [Point(-1,-1),Point(-5,3),Point(0,11),Point(6,13),Point(10,4.5),Point(4,-3)], range_number = 100):
    draw_figure(figure)
    random.seed(1)
    for i in range(range_number):
        given_point = Point(random.randint(-5,10),random.randint(-5,10))   #-2,0
        func_value = func(figure, given_point)
        if func_value == "on":
            plt.plot(given_point.x, given_point.y, 'ro', color=(0,0,0), markersize=4)
        elif func_value == "inside":
            plt.plot(given_point.x, given_point.y, 'ro', markersize=4)
        else:
            plt.plot(given_point.x, given_point.y, 'ro', color = (0,0.5,0.3), markersize=4)
    plt.show()