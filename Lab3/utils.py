from classes import Vector, Point
from math import floor
import random


def determinant(p1, p2, p0):
    a = p2.x - p1.x
    b = p2.y - p1.y
    c = p0.x - p1.x
    d = p0.y - p1.y
    return a*d - b*c


def scalar(p1, p2, p3, p4):
    line1 = Vector(p1, p2)
    line2 = Vector(p3, p4)
    return line1.x * line2.x + line1.y * line2.y


def input_point(msg):
    print(msg)
    x = float(input('x: '))
    y = float(input('y: '))
    return [x, y]


def gabarit_test(p0, p_min, p_max):
    if p0.x < p_min.x or p0.x > p_max.x or p0.y < p_min.y or p0.y > p_max.y:
        return True
    return False


def check_point_pos(p1, p2, p0):
    det = determinant(p1, p2, p0)
    if det > 0:
        return 1
    elif det < 0:
        return -1
    else:
        return 0


def octan(p1, p2):
    x = p2.x - p1.x
    y = p2.y - p1.y
    if 0 <= y < x:
        return 1
    elif 0 < x <= y:
        return 2
    elif 0 <= -x < y:
        return 3
    elif 0 < y <= -x:
        return 4
    elif 0 <= -y < -x:
        return 5
    elif 0 < -x <= -y:
        return 6
    elif 0 <= x < -y:
        return 7
    elif 0 < -y <= x:
        return 8


def correction(d, p1, p2, p0):
    if d > 4:
        return d - 8
    elif d < -4:
        return d + 8
    elif d == 4 or d == -4:
        det = determinant(p0, p1, p2)
        if det > 0:
            return 4
        elif det < 0:
            return -4
        else:
            # Точка на многоугольнике
            return 'Точка на многоугольнике'
    else:
        return d


def binary_test(polygon, p0):
    n = len(polygon)
    position_p0 = check_point_pos(polygon[0], polygon[1], p0)
    position_pn = check_point_pos(polygon[0], polygon[1], polygon[n-1])
    position_p0n = check_point_pos(polygon[0], polygon[n - 1], p0)
    position_p2 = check_point_pos(polygon[0], polygon[n - 1], polygon[1])
    # если P0, Pn по разные стороны P1P2 или P0, P2 по разные стороны P1P2
    if position_p0 * position_pn < 0 or position_p0n * position_p2 < 0:
        print('Не в многоугольнике')
        return False
    start = 1
    end = n - 1
    while end - start > 1:
        sep = floor((start + end) / 2)
        if check_point_pos(polygon[0], polygon[sep], p0) * check_point_pos(polygon[0], polygon[sep], polygon[start]) < 0:
            start = sep
        else:
            end = sep
    if check_point_pos(polygon[start], polygon[end], p0) * check_point_pos(polygon[start], polygon[end], polygon[0]) < 0:
        # return 'Не в многоугольнике'
        print('Не в многоугольнике')
        return False
    else:
        # return 'В многоугольнике'
        print('В многоугольнике')
        return True


def next_el(i, n):
    return i + 1 if i < n - 1 else 0


def prev_el(i, n):
    return i - 1 if i > 0 else n - 1


def is_intersect(p1, p2, p3, p4):
    d1 = determinant(p3, p4, p1)
    d2 = determinant(p3, p4, p2)
    d3 = determinant(p1, p2, p3)
    d4 = determinant(p1, p2, p4)
    if d1 == d2 == d3 == d4 == 0:
        c1 = scalar(p1, p3, p1, p4)
        c2 = scalar(p2, p3, p2, p4)
        c3 = scalar(p3, p1, p3, p2)
        c4 = scalar(p4, p1, p4, p2)
        if c1 < 0 or c2 < 0 or c3 < 0 or c4 < 0:
            return True
        else:
            return False
    elif d1 * d2 <= 0 and d3 * d4 <= 0:
        return True
    else:
        return False


def ptest(p1, p2, p0):
    if check_point_pos(p1, p2, p0) == 0 and scalar(p0, p1, p0, p2) <= 0:
        return True
    return False


def generate():
    number_of_vertex = random.randrange(3, 10, 1)
    points_array = []
    i = 0
    while i < number_of_vertex:
        point = Point(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        points_array.append(point)
        i += 1
    return points_array