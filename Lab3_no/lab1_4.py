import matplotlib.pyplot as plt
import random

from lab1_1 import Point, det, draw_line, define_orientation
from lab1_2 import is_intersect
from lab1_3 import is_simple, draw_figure
from copy import deepcopy

def is_convex(original_points):
    flag = True
    if is_simple(original_points):
        points = deepcopy(original_points)
        points = points + [points[0]] + [points[1]]
        for i in range(0, len(points) - 2):
            temp = define_orientation(points[i], points[i + 1], points[i + 2])
            if temp != "on":
                try:
                    if temp != last:
                        return False
                except:
                    pass
                last = temp
        return True
    else:
        return False

if __name__ == "__main__":
    points = []
    for i in range(0, 4):  # random.randint(3,6)
        points.append(Point(random.randint(0, 20), random.randint(0, 20)))
    print("Convex", is_convex(points))
    draw_figure(points)
    plt.show()