import pygame
import sys
import math

from classes.Vector2d import Vector3d

pygame.init()
FPS = 16
WIN_WIDTH = 600
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RUNNING = True

RADIUS = 3
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

FONT = pygame.font.Font(None, 20)


def dist_proj_a_to_b(a, b):
  # return (a[0] * b[0] + a[1] * b[1] + a[2] * b[2]) / (math.sqrt(b[0] * b[0] + b[1] * b[1] + b[2] * b[2]))
  return (a[0] * b.x + a[1] * b.y + a[2] * b.z) / (math.sqrt(b.x * b.x + b.y * b.y + b.z * b.z))


### Implemented in Vector3d class
# def scale(v: list, sc: int):
#   return [v[0] * sc, v[1] * sc, v[2] * sc]


### Implemented in Vector3d class
# def vect_multiply(a: list, b: list):
#   return [a[1] * b[2] - b[1] * a[2], a[2] * b[0] - b[2] * a[0], a[0] * b[1] - b[0] * a[1]]


def rotate(q: list, point: list, perp: list):
  # p = [point[0] - perp[0], point[1] - perp[1], point[2] - perp[2]]
  # q_dir = [q[1], q[2], q[3]]
  # vect_mult = vect_multiply(q_dir, p)
  p = Vector3d(point[0] - perp[0], point[1] - perp[1], point[2] - perp[2])
  q_dir = Vector3d(q[1], q[2], q[3])
  vect_mult = Vector3d.vect_product(q_dir, p)
  # return [perp[0] + p[0] * q[0] + vect_mult[0],
  #         perp[1] + p[1] * q[0] + vect_mult[1],
  #         perp[2] + p[2] * q[0] + vect_mult[2]]
  return [perp[0] + p.x * q[0] + vect_mult.x,
          perp[1] + p.y * q[0] + vect_mult.y,
          perp[2] + p.z * q[0] + vect_mult.z]


#  Draw functions
def render_text(sc, message, p) -> None:
  text = FONT.render(message, False, (0, 0, 0))
  sc.blit(text, (p[0] + 5, p[1] + 5))


def get_orth_projection(points: list):
  res = list()
  for p in points:
    point = [p[0], p[1]]
    res.append(point)
  return res


def get_center_projection(points: list):
  center = [0, 0, 800]
  res = list()
  for p in points:
    x = ((p[0] - center[0]) * center[2]) / (center[2] - p[2])
    y = ((p[1] - center[1]) * center[2]) / (center[2] - p[2])
    point = [x, y]
    res.append(point)
  return res


def draw_points(array: list):
  for point in array:
    pygame.draw.circle(sc, BLACK, point, RADIUS)


def draw_lines(array: list):
  for i in range(len(array) - 1):
    pygame.draw.line(sc, BLACK, array[i], array[i + 1])


def draw_cube(cube: list):
  draw_lines([cube[0], cube[1], cube[3], cube[2], cube[0]])
  draw_lines([cube[4], cube[5], cube[7], cube[6], cube[4]])
  draw_lines([cube[0], cube[4]])
  draw_lines([cube[1], cube[5]])
  draw_lines([cube[2], cube[6]])
  draw_lines([cube[3], cube[7]])


size = 50
ip = [300, 200, 100]  # init point
cube = [[ip[0], ip[1], ip[2]], [ip[0] + size, ip[1], ip[2]], [ip[0], ip[1] + size, ip[2]],
        [ip[0] + size, ip[1] + size, ip[2]],
        [ip[0], ip[1], ip[2] + size], [ip[0] + size, ip[1], ip[2] + size], [ip[0], ip[1] + size, ip[2] + size],
        [ip[0] + size, ip[1] + size, ip[2] + size]]

angle_dir = 45
# q_dir = [math.cos(math.radians(angle_dir)), math.sin(math.radians(angle_dir)), 0]
q_dir = Vector3d(math.cos(math.radians(angle_dir)), math.sin(math.radians(angle_dir)), 0)
delta = 0.1047
q = [math.cos(0.5 * delta),
     math.sin(0.5 * delta) * q_dir.x,
     math.sin(0.5 * delta) * q_dir.y,
     math.sin(0.5 * delta) * q_dir.z]

perpends_on_q = list()
for point in cube:
  # perpends_on_q.append(scale(q_dir, dist_proj_a_to_b(point, q_dir)))
  perpends_on_q.append(Vector3d.s_mult(q_dir, dist_proj_a_to_b(point, q_dir)))

while RUNNING:
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      sys.exit()
  sc.fill(WHITE)

  draw_cube(get_center_projection(cube))
  draw_lines(get_center_projection([[0, 0, 0], scale(q_dir, 500)]))

  for i in range(0, len(cube)):
    cube[i] = rotate(q, cube[i], perpends_on_q[i])

  pygame.display.update()
  clock.tick(FPS)
