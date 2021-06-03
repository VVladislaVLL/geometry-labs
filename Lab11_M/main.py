import sys
from math import sin, cos, radians

import pygame

from classes.Vector3d import Vector3d
from classes.Point import Point
from utils.graph import draw_cube, draw_lines
from utils.utils import init_cube, center_projection, rotation, orthogonal_projection

pygame.init()
FPS = 30

BLUE = (44, 174, 229)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
sc = pygame.display.set_mode((800, 800))


def plot_task(cube, dir_p1, dir_p2, angle):
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


def main():
  # угол поворота
  angle = 0.05

  cube = init_cube()

  # Единичный вектор
  angle_dir = 35
  dir_p1 = Point(0, 0, 0)
  dir_p2 = Point(cos(radians(angle_dir)), sin(radians(angle_dir)), 0)

  plot_task(cube, dir_p1, dir_p2, angle)


if __name__ == "__main__":
  main()
