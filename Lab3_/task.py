# import matplotlib.pyplot as plt
# from Point import Point
# import numpy as np
# from matplotlib.animation import FuncAnimation
#
# def animate_points(i):
#     new_points = []
#     global points
#     for point in points:
#         collision(point, convex_figure, "outside")
#         if octane_is_inside(simple_figure, point) == "outside":
#             new_points.append(point)
#         point.move()
#     points = new_points
#     mat.set_data([point.x for point in points], [point.y for point in points])
#     return mat,
#
#
# def task():
#     plt.title("Lab 3")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.grid()
#     big_polygon = [
#         Point(4, 0.5),
#         Point(2, 1),
#         Point(1, 2),
#         Point(2, 4),
#         Point(4, 5),
#         Point(7, 4),
#         Point(8, 2),
#         Point(6, 1),
#         Point(4, 0.5)
#     ]
#     small_polygon = [
#         Point(2, 2),
#         Point(3, 3),
#         Point(4, 3.5),
#         Point(5, 3),
#         Point(6, 3),
#         Point(6, 2),
#         Point(5, 2),
#         Point(4, 1.5),
#         Point(3, 2),
#         Point(2, 2)
#     ]
#     big_cor_x = list(map(lambda p: p.x, big_polygon))
#     big_cor_y = list(map(lambda p: p.y, big_polygon))
#     plt.plot(big_cor_x, big_cor_y)
#
#     small_cor_x = list(map(lambda p: p.x, small_polygon))
#     small_cor_y = list(map(lambda p: p.y, small_polygon))
#     plt.plot(small_cor_x, small_cor_y)
#
#     p0 = Point(4, 4)
#     p0.draw()
#
    # plt.show()