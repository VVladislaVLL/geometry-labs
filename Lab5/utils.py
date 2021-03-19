from math import floor
from Point import Point


def determinant(p1, p2, p0):
    a = p2.x - p1.x
    b = p2.y - p1.y
    c = p0.x - p1.x
    d = p0.y - p1.y
    return a * d - b * c


def get_min_point(points_set):
    min = points_set[0]
    for i in range(1, len(points_set)):
        if points_set[i].x < min.x:
            min = points_set[i]
    return Point(min.x, min.y)


def get_max_point(points_set):
    max = points_set[0]
    for i in range(1, len(points_set)):
        if points_set[i].x > max.x:
            max = points_set[i]
    return Point(max.x, max.y)


def check_point_pos(p1, p2, p0):
    det = determinant(p1, p2, p0)
    if det > 0:
        return 1
    elif det < 0:
        return -1
    else:
        return 0


def next_el(i, n):
    return i + 1 if i < n - 1 else 0


def f(P, pl, pr):
    if P == []:
        return
    # Находим точку с max площадью PlPrPi
    max_s = 0
    pm = P[0]
    for p in P:
        square = abs(check_point_pos(pl, pr, p))
        if square > max_s:
            max_s = square
            pm = p
    # Разбиваем множество на два. Точки правее PrPm
    P1 = [p for p in P if check_point_pos(pr, pm, p) < 0]
    # Точки правее PmPl
    P2 = [p for p in P if check_point_pos(pm, pl, p) < 0]


def quick_hull(points_set):
    CH = []
    # находим левую и правую точку множества
    pr = get_max_point(points_set)
    pl = get_min_point(points_set)
    # строим множества точек находящихся правее и левее прямой PrPl
    L = [p for p in points_set if check_point_pos(pl, pr, p) > 0]
    R = [p for p in points_set if check_point_pos(pl, pr, p) < 0]
    # оболочка для L
    # f(L, pl, pr)
    # CH.append()
    # оболочка для R
    # f(R, pl, pr)
    # CH.append()
    # CH - итоговая оболочка
    # return CH
