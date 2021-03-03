from generate_polygon import *
from utils import *
from graph import *
from classes import Point


def task(canv):
    create_coordinate_system(canv)
    main_polygon = generate_polygon(1, 1, 5)
    draw_polygon(canv, main_polygon)
    # бинарный тест: передаём многоугольник в виде массива точек и точку p0
    # если точка на стороне - выдается не в многоугольнике
    p0 = Point(3, 3)
    draw_point(canv, p0, 'P0')

    canv.create_text(150, 100, text=binary_test(main_polygon, p0), justify=constants.CENTER)

    small_polygon = generate_polygon(1, 1, 2)
    draw_polygon(canv, small_polygon)


