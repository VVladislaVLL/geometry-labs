import matplotlib.pyplot as plt
import random

from classes.Point import Point
from classes.Vector2d import Vector2d


def draw_line(p1, p2, color=False):
  if color:
    plt.plot([p1.x, p2.x], [p1.y, p2.y], color=color)
  else:
    plt.plot([p1.x, p2.x], [p1.y, p2.y])
  # print(sec_point, sec_point, zero_point)


def det(a, b, c, d):
  return a * d - b * c


def define_orientation(p1, p2, p0):
  D = det((p2.x - p1.x), (p2.y - p1.y), (p0.x - p1.x), (p0.y - p1.y))
  if D > 0:
    return "left"
  elif D < 0:
    return "right"
  else:
    return "on"


def is_intersect(p1, p2, p3, p4):
  det1 = det((p2.x - p1.x), (p2.y - p1.y), (p3.x - p1.x), (p3.y - p1.y))
  det2 = det((p2.x - p1.x), (p2.y - p1.y), (p4.x - p1.x), (p4.y - p1.y))
  det3 = det((p4.x - p3.x), (p4.y - p3.y), (p1.x - p3.x), (p1.y - p3.y))
  det4 = det((p4.x - p3.x), (p4.y - p3.y), (p2.x - p3.x), (p2.y - p3.y))
  if det1 * det2 <= 0 and det3 * det4 <= 0:
    return True
  else:
    return False


def point_on_line(point, p1, p2):
  p_max = Point(max(p1.x, p2.x), max(p1.y, p2.y))
  p_min = Point(min(p1.x, p2.x), min(p1.y, p2.y))
  if define_orientation(p1, p2, point) == "on" and p_min.x <= point.x <= p_max.x and p_min.y <= point.y <= p_max.y:
    return True
  else:
    return False


# Создание динамической оболочки
def append_point(convex_hull, point):
  # n = len(CH)
  # # точка
  # if n == 0:
  #   CH.append(point)
  # # две точки
  # elif n == 1:
  #   # если совпадают, добавляем одну, иначе две
  #   if not CH[0] == point:
  #     CH.append(point)
  # # три точки
  # elif n == 2:
  #   CH = check_triangle(CH[0], CH[1], point)
  #
  # if n >= 3:
  #   S = []
  #   for i in range(0, n):
  #     # следующая точка оболочки для текущей
  #     next_point = next_el(i, n)
  #     # если сторона оболочки "видна" из добавленной точки добавляем индексы вершин стороны
  #     if define_orientation(CH[i], CH[next_point], point) == "right":
  #       if S.count(i) == 0:
  #         S.append(i)
  #       if S.count(next_point) == 0 or S[0] == next_point:
  #         S.append(next_point)
  #   s = len(S)
  #   if not s == 0:
  #     # если конечные эл-ты множ-ва вершин сторон, "видимых из точки", равны
  #     # то надо удалить эту вершину в оболочке и на её место вставить точку
  #     if S[0] == S[s - 1]:
  #       start_index = 0
  #       s = 2
  #       insert_index = S[0]
  #     # иначе удаляем все элементы между первым и последним и вставляем между ними точку
  #     else:
  #       insert_index = S[0] + 1
  #       start_index = 1
  #     # меняем оболочку
  #     for i in range(start_index, s - 1):
  #       CH.remove(CH[S[i]])
  #     CH.insert(insert_index, point)
  #
  # return CH
  if point in convex_hull:
    return convex_hull

  if len(convex_hull) <= 1:
    convex_hull.append(point)
    return convex_hull

  if len(convex_hull) == 2:
    p1, p2 = convex_hull[0], convex_hull[1]
    if define_orientation(p1, p2, point) == "on":
      if (point_on_line(point, p1, p2)):
        print(point)
      elif (point_on_line(p1, point, p2)):
        print(p1)
        convex_hull = [p2, point]
      else:
        print(p2)
        convex_hull = [p1, point]
    else:
      if define_orientation(p1, p2, point) == "left":
        convex_hull = [p1, point, p2]
      else:
        convex_hull = [p1, p2, point]
    return convex_hull
  if len(convex_hull) > 2:
    right_sides = []
    for i in range(len(convex_hull)):
      if define_orientation(convex_hull[i], convex_hull[(i + 1) % len(convex_hull)], point) == "right":
        right_sides.append((convex_hull[i], convex_hull[(i + 1) % len(convex_hull)]))
      elif 0 not in right_sides:
        right_sides.append(0)
    if len(right_sides) == 1:
      return convex_hull
    convex_hull = []
    for side in right_sides:
      if side == 0:
        convex_hull.append(point)
      else:
        if side[0] not in convex_hull:
          convex_hull.append(side[0])
        if side[1] not in convex_hull:
          convex_hull.append(side[1])
    return convex_hull


def draw_figure(points, color=False):
  for ind in range(0, len(points)):
    try:
      draw_line(points[ind], points[ind + 1], color)
    except:
      draw_line(points[ind], points[0], color)


def check_triangle(p1, p2, p3):
  if p1 == p2 == p3:
    return p1
  elif not p1 == p2 and not p1 == p3 and not p2 == p3:
    pos = define_orientation(p1, p2, p3)
    if pos == "left":
      return [p1, p2, p3]
    elif pos == "right":
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


def next_el(i, n):
  return (i + 1) % n
