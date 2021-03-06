from generate_polygon import *
from utils import *
from graph import *
from classes import Point, Vector2d
from time import *
from math import *


def find_side(mng, p1, p2):
    i = 0
    length = len(mng)
    while i < length:
        if is_intersect(p1, p2, mng[i], mng[i + 1 if i != length else 0]):
            break
        i += 1
    return [i, i + 1 if i != length else 0]


def motion(canv, root, point, vector, mng):
    next_point_pos = Point(point.x + vector.x, point.y + vector.y)
    flag_next = binary_test(mng, next_point_pos)
    flag_current = binary_test(mng, point)
    print('next: inside' if flag_next else 'next: outside')
    print('current: inside' if flag_current else 'current: outside')
    if (not flag_next) and flag_current:
        print('столкновение ')
        draw_point(canv, next_point_pos, 'P')
        p = find_side(mng, point, next_point_pos)
        print(p)
        vec = Vector2d(mng[p[1]].x - mng[p[0]].x, mng[p[1]].y - mng[p[0]].y)
        normal = Vector2d.s_get_perpendicular(vec.x, vec.y)
        cos = Vector2d.scalar_product(vector, normal) / (vec.get_module() * normal.get_module())
        print(acos(cos))
        return
    else:
        canv.move(point.picture, vector.x, vector.y)
        point.x += vector.x
        point.y += vector.y
        root.after(30, lambda: motion(canv, root, point, vector, mng))


def task(canv, root):
    create_coordinate_system(canv)
    # main_polygon = generate_polygon(1, 1, 5)
    # draw_polygon(canv, main_polygon)
    # бинарный тест: передаём многоугольник в виде массива точек и точку p0
    # если точка на стороне - выдается не в многоугольнике
    # p0 = Point(3, 3)
    # draw_point(canv, p0, 'P0')
    # canv.create_text(150, 100, text=binary_test(main_polygon, p0), justify=constants.CENTER)

    # small_polygon = generate_polygon(1, 1, 2)
    # draw_polygon(canv, small_polygon)
    #
    # motion(canv, root, p0, Vector(Point(1, 1), Point(-1, 2)), small_polygon)

    main_polygon = generate_polygon(1, 1, 5)
    draw_polygon(canv, main_polygon)

    p0 = Point(3, 3)
    draw_point(canv, p0, 'P0')
    v = Vector2d.get_vector(pi / 3)
    motion(canv, root, p0, v.change_system(), main_polygon)