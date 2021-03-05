from utils import *
from classes import Point
from graph import *


def task(num, canvas):
    # строим систему координат
    create_coordinate_system(canvas)

    # массив вершин многоугольника
    points = []
    # массив x-координат вершин для последующей сортировки и выявления max/min точек
    points_x = []
    # массив y-координат вершин для последующей сортировки и выявления max/min точек
    points_y = []
    # ввод точки
    [x, y] = input_point("Введите точку")
    p0 = Point(x, y)
    draw_point(canvas, p0, 'P0', 20)
    # ввод вершин многоугольника
    n = 1
    while n <= num:
        [x, y] = input_point("Введите вершину многоугольника")
        p = Point(x, y)
        points.append(p)
        points_x.append(x)
        points_y.append(y)
        draw_point(canvas, p, 'P' + str(n))
        n += 1

    # отрисовка многоугольника
    changed_points = []
    for i in range(0, num):
        changed_points.append(points[i].change_system().x)
        changed_points.append(points[i].change_system().y)
    canvas.create_polygon(changed_points, fill="", outline="black")

    # габаритный тест
    points_x.sort()
    points_y.sort()
    p_max = Point(points_x[num-1], points_y[num-1])
    p_min = Point(points_x[0], points_y[0])
    if gabarit_test(p0, p_min, p_max):
        return 'Точка вне многоугольника'

    q1 = Point(p_min.x - 1, p0.y)
    s = 0
    i = 0
    while i < num:
        j = next_el(i, num)
        if ptest(points[i], points[j], p0):
            return 'Точка на многоугольнике'
        if is_intersect(p0, q1, points[i], points[j]):
            if ptest(p0, q1, points[i]):
                while determinant(p0, q1, points[j]) == 0:
                    j = next_el(j, num)
                k = prev_el(i, num)
                while determinant(p0, q1, points[k]) == 0:
                    k = prev_el(k, num)
                if determinant(p0, q1, points[j]) * determinant(p0, q1, points[k]) < 0:
                    s += 1
                if j < i:
                    break
                i = j
                continue
            if ptest(p0, q1, points[j]):
                i += 1
                continue
            s += 1
        i += 1

    if s % 2 == 0:
        return 'Точка вне многоугольника'
    else:
        return 'Точка внутри многоугольника'
