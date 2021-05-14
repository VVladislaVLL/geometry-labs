from classes.Vector2d import Vector2d


def is_intersect(p1, p2, p3, p4):
    d1 = determinant(p3, p4, p3, p1)
    d2 = determinant(p3, p4, p3, p2)
    d3 = determinant(p1, p2, p1, p3)
    d4 = determinant(p1, p2, p1, p4)
    if d1 == d2 == d3 == d4 == 0:
        c1 = Vector2d.scalar_product(Vector2d(p1, p3), Vector2d(p1, p4))
        c2 = Vector2d.scalar_product(Vector2d(p2, p3), Vector2d(p2, p4))
        c3 = Vector2d.scalar_product(Vector2d(p3, p1), Vector2d(p3, p2))
        c4 = Vector2d.scalar_product(Vector2d(p4, p1), Vector2d(p4, p2))
        if c1 < 0 or c2 < 0 or c3 < 0 or c4 < 0:
            return True
        else:
            return False
    elif d1 * d2 <= 0 and d3 * d4 <= 0:
        return True
    else:
        return False


def next_el(i, n):
    return (i + 1) % n


def determinant(p1, p2, p3, p4):
    a = p2.x - p1.x
    b = p2.y - p1.y
    c = p4.x - p3.x
    d = p4.y - p3.y
    return a * d - b * c


def check_point_pos(p1, p2, p0):
    det = determinant(p1, p2, p1, p0)
    if det > 0: # left
        return 1
    elif det < 0:
        return -1 # right
    else:
        return 0 # on


def check_triangle(p1, p2, p3):
    if p1 == p2 == p3:
        return p1
    elif not p1 == p2 and not p1 == p3 and not p2 == p3:
        pos = check_point_pos(p1, p2, p3)
        if pos > 0:
            return [p1, p2, p3]
        elif pos < 0:
            return [p1, p3, p2]
        elif pos == 0:
            if Vector2d.scalar_product(Vector2d(p3, p1), Vector2d(p3, p2)) < 0:
                return [p1, p2]
            elif Vector2d.scalar_product(Vector2d(p1, p2), Vector2d(p1, p3)) < 0:
                return [p2, p3]
            elif Vector2d.scalar_product(Vector2d(p2, p1), Vector2d(p2, p3)) < 0:
                return [p1, p3]
    else:
        if p1 == p2:
            return [p1, p3]
        elif p1 == p3:
            return [p1, p2]
        elif p2 == p3:
            return [p1, p2]


def get_scalar_product(v1, v2):
    return v1.x * v2.x + v1.y * v2.y