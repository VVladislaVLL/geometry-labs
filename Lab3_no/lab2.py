import matplotlib.pyplot as plt
import random
from lab1_1 import Point,draw_line, define_orientation
from lab1_2 import is_intersect
from lab1_3 import is_simple, draw_figure
from lab2_test import test_inside
import copy

def find_min_max(points):
    points_x = []
    points_y = []
    for i in points:
        points_x.append(i.x)
        points_y.append(i.y)
    return Point(min(points_x),min(points_y)),Point(max(points_x),max(points_y))

def dimensional_test(points,given_point):
    min_point, max_point = find_min_max(points)
    if given_point.x < min_point.x or given_point.x > max_point.x or given_point.y < min_point.y or given_point.y > max_point.y:
        return False
    else:
        return True

def is_intersect_in_nodes(points,given_point,outside_point):
    for i in points:
        if define_orientation(i, given_point, outside_point) == "on":
            return True
    return False

def is_on(points,given_point):
    for ind in range(len(points)-1):
        p_max = Point(max(points[ind].x, points[ind+1].x), max(points[ind].y, points[ind+1].y))
        p_min = Point(min(points[ind].x, points[ind+1].x), min(points[ind].y, points[ind+1].y))
        if define_orientation(points[ind],points[ind+1],given_point) == "on" \
                and p_min.x <= given_point.x <= p_max.x and p_min.y <= given_point.y <= p_max.y:
            return True

def is_inside(original_points,given_point):
    points = copy.deepcopy(original_points)
    points += [points[0]]
    if is_on(points,given_point):
        return "on"
    outside_point = find_min_max(points)[0]  # Point(-1,-1)
    # outside_point = Point(-1, -1)
    outside_point.x -= 1
    outside_point.y -= 1
    if dimensional_test(points, given_point):
        while is_intersect_in_nodes(points, given_point, outside_point):
            # print("outside point moved")
            outside_point.y -= 0.1
        counter = 0
        for i in range(0, len(points)-1):
            try:
                counter += is_intersect(given_point, outside_point, points[i], points[i + 1])
            except:
                counter += is_intersect(given_point, outside_point, points[i], points[0])
        if counter % 2 == 0:
            return "outside"
        else:
            return "inside"
    else:
        return "outside"


if __name__ == "__main__":
    given_point = Point(5,3) #4,4 -1,-1
    points = [Point(1,1),Point(4,5),Point(1,8),Point(5,7),Point(7,9),Point(6,3),Point(9,4),Point(6,2),Point(4,3.5)]
    test_inside(is_inside,range_number=100)