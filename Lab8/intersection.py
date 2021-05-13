from classes.Point import Point
from utils.utils import determinant, next_el, is_intersect, check_point_pos
from classes.Vector2d import Vector2d


def get_intersection(p1, p2, p3, p4):
  n = Vector2d(-(p2.y - p1.y), p2.x - p1.x)
  t = (Vector2d.scalar_product(n, Vector2d(p3, p1))) / (Vector2d.scalar_product(n, Vector2d(p3, p4)))
  p = Vector2d(p3, p4)
  return Point(p3.x + t * p.x, p3.y + t * p.y)


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
  for i in range(0, n):
    if check_point_pos(P[i], P[next_el(i, n)], Q[0]) == -1 or check_point_pos(Q[0], Q[1], P[next_el(i, n)]) == -1:
      p = i
      break

  next_p = next_el(p, n)
  next_q = next_el(q, m)

  for i in range(0, 2 * (m + n)):
    if aims_at(P[p], P[next_p], Q[q], Q[next_q]) and aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      if external(P[next_p], Q[next_q]):
        p = next_el(p, n)
        next_p = next_el(p, n)
      else:
        q = next_el(q, m)
        next_q = next_el(q, m)
    elif aims_at(P[p], P[next_p], Q[q], Q[next_q]) and not aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      if not external(P[next_p], Q[next_q]):
        Res.append(P[next_p])
      p = next_el(p, n)
      next_p = next_el(p, n)
    elif not aims_at(P[p], P[next_p], Q[q], Q[next_q]) and aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      if external(P[next_p], Q[next_q]):
        Res.append(Q[next_q])
      q = next_el(q, m)
      next_q = next_el(q, m)
    elif not aims_at(P[p], P[next_p], Q[q], Q[next_q]) and not aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      if is_intersect(P[p], P[next_p], Q[q], Q[next_q]):
        Res.append(get_intersection(P[p], P[next_p], Q[q], Q[next_q]))
      if external(P[next_p], Q[next_q]):
        p = next_el(p, n)
        next_p = next_el(p, n)
      else:
        q = next_el(q, m)
        next_q = next_el(q, m)
    if len(Res) and Res[0] == Res[len(Res) - 1]:
      break

  Res.remove(Res[len(Res) - 1])

  return Res
