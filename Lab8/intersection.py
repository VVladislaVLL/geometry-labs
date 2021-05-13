from classes.Point import Point
from utils.utils import determinant, next_el, is_intersect, check_point_pos
from classes.Vector2d import Vector2d
import numpy as np


def get_intersection(p1, p2, p3, p4):
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
  v1 = Vector2d(a1, a2)
  v2 = Vector2d(b1, b2)
  # is_col = (v1.x * v2.y) == (v1.y * v2.x)
  is_col = check_point_pos(a1, a2, b1) == 0 and check_point_pos(a1, a2, b2)

  if is_col:
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
        # next_p = next_el(next_p, n)
      else:
        q = next_q
        next_q = next_el(q, m)
        # next_q = next_el(next_q, m)
    elif aims_at(P[p], P[next_p], Q[q], Q[next_q]) and not aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      if not external(P[p], P[next_p], Q[q], Q[next_q]):
        Res.append(P[next_p])
      p = next_p
      next_p = next_el(p, n)
      # next_p = next_el(next_p, n)
    elif not aims_at(P[p], P[next_p], Q[q], Q[next_q]) and aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      if not external(Q[q], Q[next_q], P[p], P[next_p]):
        Res.append(Q[next_q])
      q = next_q
      next_q = next_el(q, m)
      # next_q = next_el(next_q, m)
    elif not aims_at(P[p], P[next_p], Q[q], Q[next_q]) and not aims_at(Q[q], Q[next_q], P[p], P[next_p]):
      # check this
      if is_intersect(P[p], P[next_p], Q[q], Q[next_q]):
        Res.append(get_intersection(P[p], P[next_p], Q[q], Q[next_q]))
      if external(P[p], P[next_p], Q[q], Q[next_q]):
        p = next_p
        next_p = next_el(p, n)
        # next_p = next_el(next_p, n)
      else:
        q = next_q
        next_q = next_el(q, m)
        # next_q = next_el(next_q, m)
    if len(Res) > 1 and Res[0] == Res[-1]:
      break

  if len(Res) > 0:
    Res.remove(Res[len(Res) - 1])

  return Res

# def intersection(x1, y1, x2, y2):
#   # Получаем количества вершин многоугольников
#   n1 = np.size(x1)
#   n2 = np.size(x2)
#   # Создаем пустые массивы для хранения результата
#   x = np.array([])
#   y = np.array([])
#   # "Окно" для движения по первому многоугольнику
#   p = 0
#   # "Окно" для движения по второму многоугольнику
#   q = 0
#   # Количество операций
#   k = 0
#   # Фиксируем окно q из второго многоугольника и для него подбираем окно p из первого многоугольника
#   for i in np.arange(n1):
#     if (check_point_pos(x1[i], y1[i], x1[get_next(i, n1)], y1[get_next(i, n1)], x2[0], y2[0]) == -1) or (
#         check_point_pos(x2[0], y2[0], x2[1], y2[1], x1[get_next(i, n1)], y1[get_next(i, n1)]) == -1):
#       p = i
#       break
#   # следующие точки
#   p_next = next_el(p, n1)
#   q_next = next_el(q, n2)
#   # Идем циклом по точкам многоугольника
#   while k != (2 * (n1 + n2)):
#     # Случай если окна нацелены друг на друга
#     if (is_aimed(x1[p], y1[p], x1[p_next], y1[p_next], x2[q], y2[q], x2[q_next], y2[q_next]) and is_aimed(x2[q],
#                                                                                                           y2[q], x2[
#                                                                                                             q_next],
#                                                                                                           y2[
#                                                                                                             q_next],
#                                                                                                           x1[p],
#                                                                                                           y1[p], x1[
#                                                                                                             p_next],
#                                                                                                           y1[
#                                                                                                             p_next])):
#       # Двигаем внешнее окно
#       if is_first_external(x1[p], y1[p], x1[p_next], y1[p_next], x2[q], y2[q], x2[q_next], y2[q_next]):
#         p = p_next
#         p_next = next_el(p, n1)
#       else:
#         q = q_next
#         q_next = next_el(q, n2)
#     # Случай когда p нацелен на q, а q на p не нацелен
#     elif (is_aimed(x1[p], y1[p], x1[p_next], y1[p_next], x2[q], y2[q], x2[q_next], y2[q_next]) and is_aimed(x2[q],
#                                                                                                             y2[q],
#                                                                                                             x2[
#                                                                                                               q_next],
#                                                                                                             y2[
#                                                                                                               q_next],
#                                                                                                             x1[p],
#                                                                                                             y1[p],
#                                                                                                             x1[
#                                                                                                               p_next],
#                                                                                                             y1[
#                                                                                                               p_next]) == False):
#       # Если p - внешнее окно, то добавляем конечную вершину в ответ
#       if is_first_external(x1[p], y1[p], x1[p_next], y1[p_next], x2[q], y2[q], x2[q_next], y2[q_next]) == False:
#         x = np.append(x, x1[p_next])
#         y = np.append(y, y1[p_next])
#       # Двугаем окно p
#       p = p_next
#       p_next = next_el(p, n1)
#     # Случай когда q нацелен на p, а p на q не нацелен
#     elif (is_aimed(x1[p], y1[p], x1[p_next], y1[p_next], x2[q], y2[q], x2[q_next],
#                    y2[q_next]) == False and is_aimed(x2[q], y2[q], x2[q_next], y2[q_next], x1[p], y1[p], x1[p_next],
#                                                      y1[p_next])):
#       # Если q - внешнее окно, то добавляем конечную вершину в ответ
#       if is_first_external(x2[q], y2[q], x2[q_next], y2[q_next], x1[p], y1[p], x1[p_next], y1[p_next]) == False:
#         x = np.append(x, x2[q_next])
#         y = np.append(y, y2[q_next])
#       # Двугаем окно q
#       q = q_next
#       q_next = next_el(q, n2)
#     # Случай если окна не нацелены друг на друга
#     elif (is_aimed(x1[p], y1[p], x1[p_next], y1[p_next], x2[q], y2[q], x2[q_next],
#                    y2[q_next]) == False and is_aimed(x2[q], y2[q], x2[q_next], y2[q_next], x1[p], y1[p], x1[p_next],
#                                                      y1[p_next])) == False:
#       # Если окна пересекаются, то добавляем точку пересечения в ответ
#       if (check_position(x1[p], y1[p], x1[p_next], y1[p_next], x2[q], y2[q], x2[q_next], y2[q_next])):
#         point = get_point_intersection(x1[p], y1[p], x1[p_next], y1[p_next], x2[q], y2[q], x2[q_next],
#                                        y2[q_next])
#         x = np.append(x, point[0])
#         y = np.append(y, point[1])
#       # Двигаем внешнее окно
#       if is_first_external(x1[p], y1[p], x1[p_next], y1[p_next], x2[q], y2[q], x2[q_next], y2[q_next]):
#         p = p_next
#         p_next = next_el(p, n1)
#       else:
#         q = q_next
#         q_next = next_el(q, n2)
#     # Если первая добавленная точка совпала с последней
#     if ((np.size(x) > 1) and ((x[0] == x[-1]) and (y[0] == y[-1]))):
#       break
#     k += 1
#   # Удаляем совпашую точку
#   if (np.size(x) > 0):
#     x = np.delete(x, np.size(x) - 1)
#     y = np.delete(y, np.size(y) - 1)
#   return np.array([x, y])
