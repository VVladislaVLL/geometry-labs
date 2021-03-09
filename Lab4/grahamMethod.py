from math import *
from Vector2d import *


def determinant(p1, p2, p0):
    a = p2.x - p1.x
    b = p2.y - p1.y
    c = p0.x - p1.x
    d = p0.y - p1.y
    return a * d - b * c


def check_point_pos(p1, p2, p0):
    det = determinant(p1, p2, p0)
    if det > 0:
        return 1
    elif det < 0:
        return -1
    else:
        return 0


def sorter(p1, p0):
    value1 = pi / 2 if p1.x == p0.x \
        else atan((p1.y - p0.y) / abs(p0.x - p1.x))
    if p1.x < p0.x:
        value1 = pi - value1
    return value1, Vector2d.get_length(p1, p0)


def get_min_index(points_set):
    min_index = 0
    min_value = {'y': points_set[0].y, 'x': points_set[0].x}
    # Find min value with y coordinate
    # (but if there are more then 1 point with such value of coord y compare Points by x coord)
    for i in range(0, len(points_set)):
        if min_value['y'] > points_set[i].y:
            min_value['y'] = points_set[i].y
            min_value['x'] = points_set[i].x
            min_index = i
        elif min_value['y'] == points_set[i].y:
            if min_value['x'] > points_set[i].x:
                min_value['y'] = points_set[i].y
                min_value['x'] = points_set[i].x
                min_index = i

    return min_index


def graham_method(points_set):
    set_copy = points_set[:]
    print('COPY SET:----------------------------------------------')
    for i in range(0, len(set_copy)):
        set_copy[i].print()
    print('COPY SET-----------------------------------------------')
    stack = []
    min_index = get_min_index(points_set)
    print('MIN POINT ---------------------------------------------')
    print(min_index)
    set_copy[min_index].print()
    print('MIN POINT ---------------------------------------------')
    stack.append(set_copy[min_index])
    del set_copy[min_index]


    set_copy.sort(key=lambda point: sorter(point, stack[0]))
    stack.append(set_copy[0])
    del set_copy[0]
    print('POINTS:------------------------------------------------ ')
    for i in range(0, len(set_copy)):
        set_copy[i].print()
    print('POINTS------------------------------------------------- ')

    print(str(stack[0]))
    k = 0
    j = 0
    while j < len(set_copy):
        if check_point_pos(stack[k], stack[k + 1], set_copy[j]) == -1:
            stack.pop()
            j += 1
        else:
            stack.append(set_copy)
            j += 1
            k += 1

    print('STACK:------------------------------------------------ ')
    for i in range(0, len(stack)):
        stack[i].print()
    print('STACK------------------------------------------------- ')
    return stack
