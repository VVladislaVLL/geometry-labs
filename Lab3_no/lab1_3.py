import random

import matplotlib.pyplot as plt

from lab1_1 import draw_line, Point
from lab1_2 import is_intersect
from copy import deepcopy

def is_simple(original_points):
    points = deepcopy(original_points)
    points = points + [points[0]]
    # print(points)
    for i in range(0,len(points)):
        total = 0
        for j in range(0,len(points)):
            try:
                total += is_intersect(points[i],points[i+1],points[j],points[j+1])
            except:
                pass
            if total > 3:
                return False
        if total != 3 and total != 0:
            return False
    return True

def draw_figure(points, color=False):
    for ind in range(0,len(points)):
        try:
            draw_line(points[ind], points[ind + 1],color)
        except:
            draw_line(points[ind], points[0],color)


if __name__=="__main__":
    points = []
    for i in range(0,4):
        points.append(Point(random.randint(0, 20), random.randint(0, 20)))
    print("Simple", is_simple(points))
    draw_figure(points)
    plt.show()