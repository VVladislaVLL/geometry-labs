from generate_polygon import *
from utils import *
from graph import *
from classes import Point, Vector2d
from time import *


def motion(canv, root, point, vector, mng):
    next_point_pos = Point(point.x + vector.x, point.y + vector.y)
    # canv.move(point.picture, vector.x, vector.y)
    if not binary_test(mng, next_point_pos) and binary_test(mng, point):
        print('столкновение ')
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