import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

from lab1_1 import Point
from lab1_3 import draw_figure
from lab3_collision import collision
from lab3_convex import is_inside as convex_is_inside
from lab3_octane import is_inside as octane_is_inside


def animate_points(i):
    new_points = []
    global points
    for point in points:
        collision(point, convex_figure, "outside")
        if octane_is_inside(simple_figure, point) == "outside":
            new_points.append(point)
        point.move()
    points = new_points
    mat.set_data([point.x for point in points], [point.y for point in points])
    return mat,


if __name__ == "__main__":
    fig = plt.figure()
    ax = plt.axes(xlim=(-50, 150), ylim=(-50, 150))
    # random.seed(15)
    # random.seed(392)
    # random.seed(2)
    random.seed(205)
    points = [Point(random.randint(-50, 100), random.randint(-50, 100)) for i in range(0, 100)]
    convex_figure = [Point(-10, -10), Point(-50, 30), Point(0, 110), Point(60, 130), Point(100, 45), Point(40, -30)]
    simple_figure = [Point(10, 10), Point(40, 50), Point(10, 80), Point(50, 70), Point(70, 90), Point(60, 30), Point(90, 40),
                     Point(60, 20), Point(40, 35)]

    new_points = []
    for point in points:
        if convex_is_inside(convex_figure,point) == "inside":
            new_points.append(point)
            point.set_random_speed(1,seed=100)
    points = new_points

    mat, = ax.plot([point.x for point in points], [point.y for point in points], 'o', markersize=4)
    anim = FuncAnimation(fig, animate_points, frames=100, interval=1,
                         blit=True)  # blit=True means only re-draw the parts that have changed.

    draw_figure(simple_figure)
    draw_figure(convex_figure)
    plt.show()