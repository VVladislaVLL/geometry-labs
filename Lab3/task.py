from generate_polygon import *
from utils import *
from classes import Point
from graph import *


def task(canv):
    create_coordinate_system(canv)
    main_polygon = generate_polygon(1, 1, 5)
    draw_polygon(canv, main_polygon)

    small_polygon = generate_polygon(1, 1, 2)
    draw_polygon(canv, small_polygon)


