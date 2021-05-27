import copy

from utils import draw_line


def recursive_draw(point):
    bounded_points_copy = copy.copy(point.bound_points)
    while len(point.bound_points):
        draw_line(point.bound_points[0], point)
        point.bound_points[0].unbind(point)
    for point in bounded_points_copy:
        recursive_draw(point)


def draw_graph(original_points):
    points = copy.deepcopy(original_points)
    recursive_draw(points[0])
    # draw_line()