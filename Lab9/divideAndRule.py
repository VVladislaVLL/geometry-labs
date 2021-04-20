import math

from numpy import Infinity

# рекурсивная функция для нахождения ближайщей пары точек
def divide_and_rule(points):
    arr_length = len(points)
    if arr_length <= 3:
        return brute(points)

    middle = math.floor(arr_length / 2)
    left_clos_pair = divide_and_rule(points[0: middle])
    right_clos_pair = divide_and_rule(points[middle:])
    min_dist = get_min_pair(left_clos_pair, right_clos_pair)
    divide_pairs = list(filter(lambda coord: coord[0] - points[middle][0] < min_dist[1], points))
    clos_divide_pair = [Infinity, Infinity]

    if len(divide_pairs) > 1:
        clos_divide_pair = brute(divide_pairs)

    bestPair = get_min_pair(min_dist, clos_divide_pair)
    return bestPair

def brute(coordMas):
    close_pair = []
    m_dist = Infinity
    # curr_dist = 0
    arr_length = len(coordMas)
    for i in range(0, arr_length - 1):
        for j in range(i + 1, arr_length):
            curr_dist = dist(coordMas[i], coordMas[j])
            if curr_dist < m_dist:
                m_dist = curr_dist
                close_pair = [coordMas[i], coordMas[j]]
    print('m_dist')
    print(m_dist)
    print(close_pair)
    return [close_pair, m_dist]


def dist(point1, point2):
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    dist = math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)
    # if dist == 0:
    #     print('dist == 0 : ')
    #     print(point1)
    #     print(point2)
    #     print(x1)
    #     print(y1)
    #     print(x2)
    #     print(y2)
    return dist


def get_min_pair(pair1, pair2):
    print('pair')
    print(pair1)
    return pair1 if pair1[1] < pair2[1] else pair2
