import math

from numpy import Infinity

def divide_and_rule(points, points_y):# points_y
    # points уже отсортированно по x
    arr_length = len(points)
    # Если есть 2 или 3 точки, то использует функцию get_distance
    if arr_length <= 3:
        return get_distance(points_y)

    # Находим среднюю точку
    middle = math.floor(arr_length / 2)

    # выделяем 2 подмассива (левый и правый)
    # left_clos_pair = divide_and_rule(points[0: middle])
    # right_clos_pair = divide_and_rule(points[middle:])
    left_clos_pair = points[0: middle]
    right_clos_pair = points[middle:]
    left_sorted_by_y = [point for point in points_y if point in left_clos_pair]
    right_sorted_by_y = [point for point in points_y if point in right_clos_pair]
    disL = divide_and_rule(left_clos_pair, left_sorted_by_y)
    disR = divide_and_rule(right_clos_pair, right_sorted_by_y)

    # Находим минимум
    # min_dist = get_min_pair(left_clos_pair, right_clos_pair)
    min_dist = get_min_pair(disL, disR)
    # print(min_dist)

    # Построит массив, который содержит точки ближе, чем min_dist к линии, проходящей через среднюю точку
    divide_pairs = list(filter(lambda coord: math.fabs(coord.x - points[middle].x) < min_dist[1], points_y))

    clos_divide_pair = [Infinity, Infinity]

    # Если точек больше чем 1, то использует функцию get_distance
    if len(divide_pairs) > 1:
        clos_divide_pair = get_distance(divide_pairs)

    # Находим самое короткое расстояние
    bestPair = get_min_pair(min_dist, clos_divide_pair)
    return bestPair


# Возвращает наименьшее расстояние между 2 точками в массиве
def get_distance(points):
    close_pair = []
    m_dist = Infinity
    arr_length = len(points)
    for i in range(0, arr_length - 1):
        for j in range(i + 1, arr_length):
        # for j in range(i + 1, i + 6):
            curr_dist = dist(points[i], points[j])
            if curr_dist < m_dist:
                m_dist = curr_dist
                close_pair = [points[i], points[j]]
    return [close_pair, m_dist]


def dist(point1, point2):
    x1 = point1.x
    x2 = point2.x
    y1 = point1.y
    y2 = point2.y
    dist = math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)
    return dist


def get_min_pair(pair1, pair2):
    return pair1 if pair1[1] < pair2[1] else pair2
