from math import sqrt, sin, cos

from classes.Vector2d import Vector3d
from classes.Point import Point


# def dist_proj_a_to_b(a, b):
#   return (a.x * b.x + a.y * b.y + a.z * b.z) / sqrt(Vector3d.scalar_product(b, b))


def get_quaternion(p0, point):
  return [p0, point]


def get_conj_quaternion(q):
  return [q[0], q[1].reverse()]


def quaternions_mult(q1, q2):
  p0 = q1[0] * q2[0] - q1[1].x * q2[1].x - q1[1].y * q2[1].y - q1[1].z * q2[1].z
  p1 = q1[0] * q2[1].x + q1[1].x * q2[0] + q1[1].y * q2[1].z - q1[1].z * q2[1].y
  p2 = q1[0] * q2[1].y + q1[1].y * q2[0] + q1[1].z * q2[1].x - q1[1].x * q2[1].z
  p3 = q1[0] * q2[1].z + q1[1].z * q2[0] + q1[1].x * q2[1].y - q1[1].y * q2[1].x
  return get_quaternion(p0, Point(p1, p2, p3))


def rotate(point, n, angle):
  s = sin(angle / 2)
  p_q = get_quaternion(0, point)
  n_q = get_quaternion(cos(angle / 2), Point(n.x * s, n.y * s, n.z * s))
  n_q_conj = get_conj_quaternion(n_q)
  return quaternions_mult(quaternions_mult(n_q, p_q), n_q_conj)[1]


# def render_text(sc, message, p):
#   text = FONT.render(message, False, (0, 0, 0))
#   sc.blit(text, (p.x + 5, p.y + 5))


def get_orthogonal_proj(point):
  None


def get_center_proj(point):
  None


def main():
  # угол поворота
  angle = 0
  # Куб
  cube = []
  # Единичный вектор
  dir = Vector3d(1, 1, 1)

  while True:
    for i in range(0, len(cube)):
      rotated = rotate(cube[i], dir, angle)
      if i % 2 == 0:
        # нахожу центральную проекцию
        None
      else:
        # нахожу ортогональную проекцию
        None

    # нужно отрисовать всё
