from math import sin, cos

from classes.Point import Point


def multiply_matrix(m1, m2):
  return [[sum(a * b for a, b in zip(m1_row, m2_col))
           for m2_col in zip(*m2)]
          for m1_row in m1]


def init_cube():
  start_point = Point(300, 200, 100)
  side_length = 50
  # Куб
  cube = [start_point,
          Point(start_point.x + side_length, start_point.y, start_point.z),
          Point(start_point.x, start_point.y + side_length, start_point.z),
          Point(start_point.x + side_length, start_point.y + side_length, start_point.z),
          Point(start_point.x, start_point.y, start_point.z + side_length),
          Point(start_point.x + side_length, start_point.y, start_point.z + side_length),
          Point(start_point.x, start_point.y + side_length, start_point.z + side_length),
          Point(start_point.x + side_length, start_point.y + side_length, start_point.z + side_length)
          ]
  return cube


def get_quaternion(p0, point):
  return [p0, point]


def get_conj_quaternion(q):
  return get_quaternion(q[0], q[1].reverse())


def quaternions_multiplication(q1, q2):
  p0 = q1[0] * q2[0] - q1[1].x * q2[1].x - q1[1].y * q2[1].y - q1[1].z * q2[1].z
  p1 = q1[0] * q2[1].x + q1[1].x * q2[0] + q1[1].y * q2[1].z - q1[1].z * q2[1].y
  p2 = q1[0] * q2[1].y + q1[1].y * q2[0] + q1[1].z * q2[1].x - q1[1].x * q2[1].z
  p3 = q1[0] * q2[1].z + q1[1].z * q2[0] + q1[1].x * q2[1].y - q1[1].y * q2[1].x
  return get_quaternion(p0, Point(p1, p2, p3))


def rotation(point, n, angle):
  s = sin(angle / 2)
  n_q = get_quaternion(cos(angle / 2), Point(n.x * s, n.y * s, n.z * s))
  n_q_conj = get_conj_quaternion(n_q)
  p_q = get_quaternion(0, point)
  return quaternions_multiplication(quaternions_multiplication(n_q, p_q), n_q_conj)[1]


def orth_proj(points, new_basis, new_origin):
  projection = []
  for p in points:
    matrix = multiply_matrix(new_basis, [[p.x - new_origin[0]], [p.y - new_origin[1]], [p.z - new_origin[2]]])
    new_x = matrix[0][0]
    new_y = matrix[1][0]
    new_z = matrix[2][0]
    projection.append(Point(new_x, new_y, new_z))
  return projection


def center_proj(points, center, new_basis, new_origin):
  new_points = orth_proj(points, new_basis, new_origin)
  new_center = orth_proj([center], new_basis, new_origin)[0]
  projection = []
  for p in new_points:
    x = p.x * (new_center.z / (new_center.z - p.z)) + new_center.x * (p.z / (new_center.z - p.z))
    y = p.y * (new_center.z / (new_center.z - p.z)) + new_center.y * (p.z / (new_center.z - p.z))
    projection.append(Point(x, y))
  return projection
