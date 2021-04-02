from classes.Vector2d import Vector2d


def next_el(i, n):
    return i + 1 if i < n - 1 else 0


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
