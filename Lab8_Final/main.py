from time import sleep

import matplotlib.pyplot as plt
from celluloid import Camera

from classes.Point import Point
from classes.Vector2d import Vector2d
from utils.utils import reverse_polygon
from utils.graph import draw_polygon, draw_line
from intersection import polygon_intersection
from cyrus_beck import cyrus_beck, change_line_with_params

fig, ax = plt.subplots()
camera = Camera(fig)


def plot_task(P, Q):
  plt.ion()

  # Количество итераций движения фигур
  CNT = 40
  for k in range(0, CNT):
    # Рисуем многоугольники
    draw_polygon(P)
    draw_polygon(Q)

    # Получаем массив точек пересечения многоугольников
    res = polygon_intersection(P, Q)
    # Зарисовываем пересечение многоугольников
    ax.fill(list(map(lambda p: p.x, res)), list(map(lambda p: p.y, res)), "gray")

    # Алгоритм Цируса-бека и отрисовка
    t1, t2 = cyrus_beck([P[0], P[2]], Q)
    draw_line(change_line_with_params([P[0], P[2]], t1, t2), "black")

    # Делаем шаг анимации
    camera.snap()
    # Двигаем многоугольники
    for p1 in P:
      p1.move()
    for p2 in Q:
      p2.move()

    plt.draw()
    plt.gcf().canvas.flush_events()
    sleep(0.0001)

  # Сохраняем анимацию
  animation = camera.animate()
  plt.ioff()
  plt.show()


def main():
  # Координаты точек вершин первого многоугольника
  P = [Point(-5.0, 0.6), Point(-2, 2.1), Point(-7, 3.6), Point(-8, 2.1)]
  # P = [Point(5, -1), Point(8, 1), Point(8, 4), Point(6, 6), Point(3, 6), Point(1, 3), Point(2, 1)]
  # Координаты точек вершин второго многоугольника
  Q = [Point(1, 2), Point(3, 0), Point(8, 0), Point(10, 2), Point(8, 4), Point(3, 4)]
  # Q = [Point(16, 2), Point(21, 4), Point(20, 6), Point(16, 9), Point(13, 7), Point(13, 4)]

  reverse_polygon(P)
  reverse_polygon(Q)

  # Задаем направление точкам
  speed = 0.25
  for point in P:
    point.set_direction([Vector2d(speed * 1, 0), speed])
  for point in Q:
    point.set_direction([Vector2d(speed * -1, 0), speed])

  plot_task(P, Q)


if __name__ == "__main__":
  main()
