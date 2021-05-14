from classes.Point import Point
from utils.utils import determinant, next_el, is_intersect, check_point_pos
from classes.Vector2d import Vector2d


def get_intersection(p1, p2, p3, p4):
  # p = p3 + t(p4 - p3)
  n = Vector2d(-(p2.y - p1.y), p2.x - p1.x)
  t = (Vector2d.scalar_product(n, Vector2d(p3, p1))) / (Vector2d.scalar_product(n, Vector2d(p3, p4)))
  p = Vector2d(p3, p4)
  return Point(p3.x + t * p.x, p3.y + t * p.y)


def external(a1, a2, b1, b2):
  if check_point_pos(b1, b2, a2) < 0:
    return True
  if check_point_pos(b1, b2, a2) == 0 and check_point_pos(b1, b2, a1) < 0:
    return True
  return False
  # if a2.x > b2.x:
  #   return True
  # else:
  #   return False


def aims_at(a1, a2, b1, b2):
  is_col = check_point_pos(a1, a2, b1) == 0 and check_point_pos(a1, a2, b2) == 0

  if is_col:
    #
    if (a1.x - a2.x) * (b2.x - b1.x) + (a1.y - a2.y) * (b2.y - b1.y) < 0:
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
    if check_point_pos(P[i], P[next_el(i, n)], Q[0]) < 0 or check_point_pos(Q[0], Q[1], P[next_el(i, n)]) < 0:
      p = i
      break

  next_p = next_el(p, n)
  next_q = next_el(q, m)

  for i in range(0, 2 * (m + n)):
    if aims_at(P[p], P[next_p], Q[q], Q[next_q]) and aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      if external(P[p], P[next_p], Q[q], Q[next_q]):
        p = next_p
        next_p = next_el(p, n)
      else:
        q = next_q
        next_q = next_el(q, m)
    elif aims_at(P[p], P[next_p], Q[q], Q[next_q]) and not aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      if not external(P[p], P[next_p], Q[q], Q[next_q]):
        Res.append(P[next_p])
      p = next_p
      next_p = next_el(p, n)
    elif not aims_at(P[p], P[next_p], Q[q], Q[next_q]) and aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      if not external(Q[q], Q[next_q], P[p], P[next_p]):
        Res.append(Q[next_q])
      q = next_q
      next_q = next_el(q, m)
    elif not aims_at(P[p], P[next_p], Q[q], Q[next_q]) and not aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      if is_intersect(P[p], P[next_p], Q[q], Q[next_q]):
        Res.append(get_intersection(P[p], P[next_p], Q[q], Q[next_q]))
      if external(P[p], P[next_p], Q[q], Q[next_q]):
        p = next_p
        next_p = next_el(p, n)
      else:
        q = next_q
        next_q = next_el(q, m)
    if len(Res) > 1 and Res[0] == Res[-1]:
      Res.remove(Res[len(Res) - 1])
      break

  # if len(Res) > 0:
  #   Res.remove(Res[len(Res) - 1])

  return Res
