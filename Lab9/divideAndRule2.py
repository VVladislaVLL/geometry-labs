import math

from numpy import Infinity

# рекурсивная функция для нахождения ближайщей пары точек
def divide_and_rule(points):
    arr_length = len(points)
    # Если есть 2 или 3 точки, то использует функцию brute
    if arr_length <= 3:
        return brute(points)

    # Находим среднюю точку
    middle = math.floor(arr_length / 2)

    # выделяем 2 подмассива (левый и правый)
    left_clos_pair = divide_and_rule(points[0: middle])
    right_clos_pair = divide_and_rule(points[middle:])

    # Находим минимум
    min_dist = get_min_pair(left_clos_pair, right_clos_pair)

    # Построит массив, который содержит точки ближе, чем min_dist к линии, проходящей через среднюю точку
    divide_pairs = list(filter(lambda coord: coord.x - points[middle].x < min_dist[1], points))

    # Просто объявление, не знаю, как это можно заменить
    clos_divide_pair = [Infinity, Infinity]

    # Если точек больше чем 1, то использует функцию brute
    if len(divide_pairs) > 1:
        clos_divide_pair = brute(divide_pairs)

    # Находим самое короткое расстояние
    bestPair = get_min_pair(min_dist, clos_divide_pair)
    return bestPair


# Возвращает наименьшее расстояние между 2 точками в массиве
def brute(coordMas):
    close_pair = []
    m_dist = Infinity
    arr_length = len(coordMas)
    for i in range(0, arr_length - 1):
        for j in range(i + 1, arr_length):
            curr_dist = dist(coordMas[i], coordMas[j])
            if curr_dist < m_dist:
                m_dist = curr_dist
                close_pair = [coordMas[i], coordMas[j]]
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
