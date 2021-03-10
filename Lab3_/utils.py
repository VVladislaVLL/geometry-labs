from math import floor
from Point import Point


def determinant(p1, p2, p0):
    a = p2.x - p1.x
    b = p2.y - p1.y
    c = p0.x - p1.x
    d = p0.y - p1.y
    return a * d - b * c


def gabarit_test(p0, p_min, p_max):
    if p0.x < p_min.x or p0.x > p_max.x or p0.y < p_min.y or p0.y > p_max.y:
        return True
    return False


def get_min_point(polygon):
    min_x = polygon[0].x
    min_y = polygon[0].y
    for i in range(0, len(polygon)):
        if polygon[i].x < min_x:
            min_x = polygon[i].x
        if polygon[i].y < min_y:
            min_y = polygon[i].y
    return Point(min_x, min_y)


def get_max_point(polygon):
    max_x = polygon[0].x
    max_y = polygon[0].y
    for i in range(0, len(polygon)):
        if polygon[i].x > max_x:
            max_x = polygon[i].x
        if polygon[i].y > max_y:
            max_y = polygon[i].y
    return Point(max_x, max_y)


def check_point_pos(p1, p2, p0):
    det = determinant(p1, p2, p0)
    if det > 0:
        return 1
    elif det < 0:
        return -1
    else:
        return 0


def angle_test(polygon, p0):
    if gabarit_test(p0, get_min_point(polygon), get_max_point(polygon)):
        return False

    n = len(polygon)
    s = 0
    for i in range(0, n):
        d1 = octan(p0, polygon[i])
        d2 = octan(p0, polygon[next_el(i, n)])
        d = correction(d2 - d1, polygon[i], polygon[next_el(i, n)], p0)
        if d == 'на стороне':
            return False
        s += d
    if s == 0:
        return False
    elif s == 8 or s == -8:
        return True
    else:
        print('ошибка в реализации')


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
        det = check_point_pos(p0, p1, p2)
        if det > 0:
            return 4
        elif det < 0:
            return -4
        else:
            return 'на стороне'
    else:
        return d


def binary_test(polygon, p0):
    n = len(polygon)
    position_p0 = check_point_pos(polygon[0], polygon[1], p0)
    position_pn = check_point_pos(polygon[0], polygon[1], polygon[n - 1])
    position_p0n = check_point_pos(polygon[0], polygon[n - 1], p0)
    position_p2 = check_point_pos(polygon[0], polygon[n - 1], polygon[1])
    # если P0, Pn по разные стороны P1P2
    if position_p0 * position_pn < 0:
        return {'flag': False, 'points': [polygon[0], polygon[1]]}
    # P0, P2 по разные стороны P1Pn
    elif position_p0n * position_p2 < 0:
        return {'flag': False, 'points': [polygon[0], polygon[n - 1]]}

    start = 1
    end = n - 1
    while end - start > 1:
        sep = floor((start + end) / 2)
        if check_point_pos(polygon[0], polygon[sep], p0) * check_point_pos(polygon[0], polygon[sep],
                                                                           polygon[start]) < 0:
            start = sep
        else:
            end = sep
    if check_point_pos(polygon[start], polygon[end], p0) * check_point_pos(polygon[start], polygon[end],
                                                                           polygon[0]) < 0:
        return {'flag': False, 'points': [polygon[start], polygon[end]]}
    else:
        return {'flag': True}


def next_el(i, n):
    return i + 1 if i < n - 1 else 0
