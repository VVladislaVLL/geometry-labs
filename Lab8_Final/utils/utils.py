from classes.Point import Point
from classes.Vector2d import Vector2d

import math


def get_intersection(p1, p2, p3, p4):
  # p = p3 + t(p4 - p3)
  n = Vector2d(-(p2.y - p1.y), p2.x - p1.x)
  t = (Vector2d.scalar_product(n, Vector2d(p3, p1))) / (Vector2d.scalar_product(n, Vector2d(p3, p4)))
  p = Vector2d(p3, p4)
  return Point(p3.x + t * p.x, p3.y + t * p.y)


# Функция возвращающая длинну отрезка
def get_length(point1, point2):
  return math.sqrt(((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2))


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
  if det > 0:  # left
    return 1
  elif det < 0:
    return -1  # right
  else:
    return 0  # on


def get_scalar_product(v1, v2):
  return v1.x * v2.x + v1.y * v2.y


# Функция возвращащая определитель матрицы 2x2
# a b
# c d
def my_det(a, b, c, d):
  return (a * d) - (b * c)


# Функция возвращающая определитель матрицы
def my_det2(p1, p2, p3):
  return ((p2.x - p1.x) * (p3.y - p1.y)) - ((p2.y - p1.y) * (p3.x - p1.x))
