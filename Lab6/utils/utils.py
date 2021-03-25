from classes.Vector2d import *


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
