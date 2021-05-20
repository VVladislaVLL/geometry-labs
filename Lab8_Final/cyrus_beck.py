from classes.Vector2d import Vector2d
from utils.utils import check_point_pos, next_el, reverse_polygon, is_intersect, get_intersection
from classes.Point import Point


# def reverse_if_left_orientation(points):
#   n = len(points)
#   i = 0
#   while True:
#     orientation = check_point_pos(points[i], points[next_el(i, n)], points[next_el(next_el(i, n), n)])
#     i += 1
#     if orientation == 0:
#       continue
#     elif orientation < 0:
#       points.reverse()
#       break
#     else:
#       break
#   return points


def cyrus_beck(segment, points):
  A = segment[0]
  B = segment[1]
  # T = {t0 = 0, t1 = 1}
  tA = 0
  tB = 1
  n = len(points)
  for i in range(len(points)):
    side = Vector2d(points[i], points[next_el(i, n)])
    normal = Vector2d(side.y, -side.x)
    # A(1-t) + Bt = P
    t2 = B.y - A.y
    t1 = get_intersection(A, B, points[i], points[next_el(i, n)]).y - A.y
    t = t1 / t2
    scalar_product = Vector2d.scalar_product(Vector2d(A, B), normal)
    # если ПП
    if scalar_product > 0:
      tB = min(tB, t)
    else:
      # если ПВ
      tA = max(tA, t)
  if tA > tB:
    return 0, 0
  return tA, tB


def change_line_with_params(segment, t1, t2):
  return (Point(segment[0].x + (segment[1].x - segment[0].x) * t1, segment[0].y + (segment[1].y - segment[0].y) * t1),
          Point(segment[0].x + (segment[1].x - segment[0].x) * t2, segment[0].y + (segment[1].y - segment[0].y) * t2))
