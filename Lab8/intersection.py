from utils.utils import determinant, next_el, is_intersect
from classes.Vector2d import Vector2d


def external(a2, b2):
    if a2.x > b2.x:
        return True
    else:
        return False


def aims_at(a1, a2, b1, b2):
    v1 = Vector2d(a1, a2)
    v2 = Vector2d(b1, b2)
    is_col = (v1.x / v2.x) == (v1.y / v2.y)

    if is_col:
        if a2.x >= b2.x:
            return True
    else:
        if determinant(b1, b2, a1, a2) <= 0 and determinant(b1, b2, b1, a2) >= 0:
            return True
        elif determinant(b1, b2, a1, a2) > 0 and determinant(b1, b2, b1, a2) < 0:
            return True
    return False


def polygons_intersection(P, Q):
    n = len(P)
    m = len(Q)

    Res = []

    p = 0
    q = 0
    next_p = next_el(p, n)
    next_q = next_el(q, m)

    # TODO: находим 2 окна, принадлжещаих одному серпу (или пересекающимся) (не полным перебором всех ребер)
    for i in range(0, 2 * (m + n)):
        if P.count(p) or Q.count(q):
            break

        if aims_at(p, next_p, q, next_q) and aims_at(q, next_q, p, next_p):
            if external(next_p, next_q):
                p = next_el(p, n)
                next_p = next_el(p, n)
            else:
                q = next_el(q, m)
                next_q = next_el(q, m)
        elif aims_at(p, next_p, q, next_q) and not aims_at(q, next_q, p, next_p):
            p = next_el(p, n)
            next_p = next_el(p, n)
            if not external(next_p, next_q):
                Res.append(next_p)
        elif not aims_at(p, next_p, q, next_q) and aims_at(q, next_q, p, next_p):
            q = next_el(q, m)
            next_q = next_el(q, m)
            if external(next_p, next_q):
                Res.append(next_q)
        elif not aims_at(p, next_p, q, next_q) and not aims_at(q, next_q, p, next_p):
            if external(next_p, next_q):
                p = next_el(p, n)
                next_p = next_el(p, n)
            else:
                q = next_el(q, m)
                next_q = next_el(q, m)
                if is_intersect(p, next_p, q, next_q):
                    # TODO: найти точку пересечения
                    Res.append("точка пересечения")

    return Res
