from lab1_1 import Point, det
from lab2 import dimensional_test
from lab3_test import test_inside
import copy


def count_octanes(figure, given_point):
    octanes = []
    for point in figure:
        x, y = point.x - given_point.x, point.y - given_point.y
        if 0 <= y < x:
            octanes.append(1)
        elif 0 < x <= y:
            octanes.append(2)
        elif 0 <= -x < y:
            octanes.append(3)
        elif 0 < y <= -x:
            octanes.append(4)
        elif 0 <= -y < -x:
            octanes.append(5)
        elif 0 < -x <= -y:
            octanes.append(6)
        elif 0 <= x < -y:
            octanes.append(7)
        elif 0 < - y <= x:
            octanes.append(8)
    return octanes


def is_inside(original_figure, given_point):
    if not dimensional_test(original_figure, given_point):
        return "outside"
    figure = copy.deepcopy(original_figure)
    figure += [figure[0]]
    octanes = count_octanes(figure, given_point)
    if given_point in figure:
        return "on"  # somehow returns -1
    s = 0
    for ind in range(0, len(octanes) - 1):
        delta = octanes[ind + 1] - octanes[ind]
        if delta > 4:
            delta -= 8
        if delta < -4:
            delta += 8
        if delta == 4 or delta == -4:
            D = det(figure[ind].x - given_point.x, figure[ind].y - given_point.y,
                    figure[ind + 1].x - given_point.x, figure[ind + 1].y - given_point.y)
            if D > 0:
                delta = 4
            if D < 0:
                delta = -4
            if D == 0:
                return "on"
        s += delta
    if s == 8 or s == -8:
        return "inside"
    if s == 0:
        return "outside"


if __name__ == "__main__":
    given_point = Point(1, 1)  # -2,0
    simple_figure = [Point(1, 1), Point(4, 5), Point(1, 8), Point(5, 7), Point(7, 9), Point(6, 3), Point(9, 4),
                     Point(6, 2), Point(4, 3.5)]
    test_inside(is_inside, simple_figure)
