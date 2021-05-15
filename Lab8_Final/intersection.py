from utils.utils import is_intersect, next_el, get_intersection, check_point_pos, determinant, my_det


# a1, a2, b1, b2
# p1_start, p1_end, p2_start, p2_end
def is_aimed(a1, a2, b1, b2):
  # x1_v = p1_end.x - p1_start.x
  # y1_v = p1_end.y - p1_start.y
  # x2_v = p2_end.x - p2_start.x
  # y2_v = p2_end.y - p2_start.y
  # x12_v = p1_end.x - p2_start.x
  # y12_v = p1_end.y - p2_start.y
  # if ((my_det(x2_v, y2_v, x12_v, y12_v) > 0)
  #     and (my_det(x2_v, y2_v, x1_v, y1_v) < 0)):
  #   return True
  # if ((my_det(x2_v, y2_v, x12_v, y12_v) < 0)
  #     and (my_det(x2_v, y2_v, x1_v, y1_v) > 0)):
  #   return True
  # # Случай если отрезки лежат на одной прямой
  # if ((check_point_pos(p1_start, p1_end, p2_start) == 0)
  #     and (check_point_pos(p1_start, p1_end, p2_end) == 0)
  #     and (((-x1_v) * (p2_end.x - p1_end.x)) + ((-y1_v) * (p2_end.y - p1_end.y))) < 0):
  #   return True
  # return False
  is_col = check_point_pos(b1, b2, a1) == 0 and check_point_pos(b1, b2, a2) == 0

  if is_col:
    if (a2.x - b2.x) * (b2.x - b1.x) + (a2.y - b2.y) * (b2.y - b1.y) > 0:
      return True
  else:
    if determinant(b1, b2, a1, a2) <= 0 and determinant(b1, b2, b1, a2) >= 0:
      return True
    elif determinant(b1, b2, a1, a2) > 0 and determinant(b1, b2, b1, a2) < 0:
      return True
  return False


def is_external(a1, a2, b1, b2):
  if check_point_pos(b1, b2, a2) < 0:
    return True
  if check_point_pos(b1, b2, a2) == 0 and check_point_pos(b1, b2, a1) < 0:
    return True
  return False


# Функция возвращающая массив точек пересечения многоугольников
def polygon_intersection(P, Q):
  # Получаем количества вершин многоугольников
  n = len(P)
  m = len(Q)
  # Массив вершин пересечения
  Res = []
  # "Окно" для движения по первому многоугольнику
  p = 0
  # "Окно" для движения по второму многоугольнику
  q = 0
  # Фиксируем окно q из второго многоугольника и для него подбираем окно p из первого многоугольника
  for i in range(0, n):
    if check_point_pos(P[i], P[next_el(i, n)], Q[0]) < 0 or check_point_pos(Q[0], Q[1], P[next_el(i, n)]) < 0:
      p = i
      break
  # следующие точки
  p_next = next_el(p, n)
  q_next = next_el(q, m)
  # Идем циклом по точкам многоугольника
  for i in range(0, 2 * (n + m)):
    # Случай если окна нацелены друг на друга
    if is_aimed(P[p], P[p_next], Q[q], Q[q_next]) and is_aimed(Q[q], Q[q_next], P[p], P[p_next]):
      # Двигаем внешнее окно
      if is_external(P[p], P[p_next], Q[q], Q[q_next]):
        p = p_next
        p_next = next_el(p, n)
      else:
        q = q_next
        q_next = next_el(q, m)
    # Случай когда p нацелен на q, а q на p не нацелен
    elif is_aimed(P[p], P[p_next], Q[q], Q[q_next]) and not is_aimed(Q[q], Q[q_next], P[p], P[p_next]):
      # Если p - внешнее окно, то добавляем конечную вершину в ответ
      if not is_external(P[p], P[p_next], Q[q], Q[q_next]):
        Res.append(P[p_next])
      # Двигаем окно p
      p = p_next
      p_next = next_el(p, n)
    # Случай когда q нацелен на p, а p на q не нацелен
    elif not is_aimed(P[p], P[p_next], Q[q], Q[q_next]) and is_aimed(Q[q], Q[q_next], P[p], P[p_next]):
      # Если q - внешнее окно, то добавляем конечную вершину в ответ
      if not is_external(Q[q], Q[q_next], P[p], P[p_next]):
        Res.append(Q[q_next])
      # Двигаем окно q
      q = q_next
      q_next = next_el(q, m)
    # Случай если окна не нацелены друг на друга
    elif not is_aimed(P[p], P[p_next], Q[q], Q[q_next]) and not is_aimed(Q[q], Q[q_next], P[p], P[p_next]):
      # Если окна пересекаются, то добавляем точку пересечения в ответ
      if is_intersect(P[p], P[p_next], Q[q], Q[q_next]):
        Res.append(get_intersection(P[p], P[p_next], Q[q], Q[q_next]))
      # Двигаем внешнее окно
      if is_external(P[p], P[p_next], Q[q], Q[q_next]):
        p = p_next
        p_next = next_el(p, n)
      else:
        q = q_next
        q_next = next_el(q, m)
    # Если первая добавленная точка совпала с последней
    if len(Res) > 1 and Res[0] == Res[-1]:
      del Res[-1]
      break

  return Res
