import random
from Point import Point
from Vector2d import Vector2d, pi
from graph import draw_polygon
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from utils import binary_test


# def animate_points(i):
#     global points_set
#     # next_points = points_set.copy()
#     #
#     # for i in range(0, len(points_set)):
#     #     next_points[i].move()
#     #     if (not binary_test(big_polygon, next_points[i])) and binary_test(big_polygon, points_set[i]):
#     #         points_set[i].direction
#
#     for point in points_set:
#         # if binary_test(big_polygon, point)
#         point.move()
#     mat.set_data([point.x for point in points_set], [point.y for point in points_set])
#     return mat,


if __name__ == '__main__':
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 15), ylim=(0, 10))

    # Polygons
    big_polygon = [Point(1, 1), Point(1, 2), Point(3, 7), Point(5, 8), Point(8, 9),
        Point(10, 8), Point(13, 4), Point(13, 3), Point(12, 1)]

    small_polygon = [Point(3, 3), Point(4, 4), Point(6, 4), Point(7, 6), Point(9, 6),
                     Point(7, 2), Point(6, 3)]

    # Our points
    points_set = [Point(2, 2),Point(4, 2), Point(4, 5), Point(4, 6), Point(6, 6),
                  Point(6, 8), Point(10, 2), Point(12, 2), Point(4, 5), Point(10, 6)]

    # Set points direction
    for point in points_set:
        point.set_direction(Vector2d.get_vector(random.uniform(0, 2 * pi)))

    # Get points coordinates
    points_coordinates = [[point.x for point in points_set], [point.y for point in points_set]]

    # Draw points and polygons
    mat, = ax.plot(points_coordinates[0], points_coordinates[1], 'o', markersize=5)
    draw_polygon(big_polygon)
    draw_polygon(small_polygon)

    # Animate points
    # anim = FuncAnimation(fig, animate_points)
    plt.show()
