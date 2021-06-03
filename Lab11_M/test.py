import sys
from math import sin, cos, radians

import pygame

from classes.Vector3d import Vector3d
from classes.Point import Point
from utils.graph import draw_cube, draw_lines
from utils.utils import init_cube

pygame.init()
FPS = 30

BLUE = (44, 174, 229)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
sc = pygame.display.set_mode((800, 800))


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


def orthogonal_projection(points):
  new_basis = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
  new_origin = [-100, 0, 0]
  projection = []
  for p in points:
    new_x = new_basis[0][0] * (p.x - new_origin[0]) + new_basis[1][0] * (p.y - new_origin[1]) + new_basis[2][0] * (
        p.z - new_origin[2])
    new_y = new_basis[0][1] * (p.x - new_origin[0]) + new_basis[1][1] * (p.y - new_origin[1]) + new_basis[2][1] * (
        p.z - new_origin[2])
    projection.append(Point(new_x, new_y))
  return projection


def center_projection(points, center):
  projection = []
  for p in points:
    x = p.x * (center.z / (center.z - p.z)) + center.x * (p.z / (center.z - p.z))
    y = p.y * (center.z / (center.z - p.z)) + center.y * (p.z / (center.z - p.z))
    projection.append(Point(x, y))
  return projection


def main():
  # угол поворота
  angle = 0.05

  cube = init_cube()

  # Единичный вектор
  angle_dir = 35
  dir_p1 = Point(0, 0, 0)
  dir_p2 = Point(cos(radians(angle_dir)), sin(radians(angle_dir)), 0)
  dir = Vector3d(dir_p1, dir_p2, 0)

  line = [Point(dir_p1.x + 100, dir_p1.y + 100), Point(dir_p2.x * 800, dir_p2.y * 800)]

  while True:
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
        sys.exit()
    sc.fill(BLUE)

    # projection_cube = orthogonal_projection(cube)
    # projection_line = orthogonal_projection(line)
    center = Point(0, 0, 600)
    projection_cube = center_projection(cube, center)
    projection_line = center_projection(line, center)

    draw_cube(sc, list(map(lambda point: [point.x, point.y], projection_cube)))
    draw_lines(sc, list(map(lambda point: [point.x, point.y], projection_line)), RED)

    for i in range(0, len(cube)):
      cube[i] = rotation(cube[i], dir, angle)

    pygame.display.update()
    clock.tick(FPS)


main()
