from Vector2d import Vector2d
from graph import draw_polygon
from task import task
import numpy as np
from task import *
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation



if __name__ == '__main__':
    def animate(i):
        # global p0
        p0.move()
        print('Внутри анимате после move')
        p0.print()
        point.set_data(p0.x, p0.y)
        return point,

    fig = plt.figure()
    ax = plt.axes(xlim=(0, 15), ylim=(0, 10))
    plt.grid()
    big_polygon = [Point(1, 1), Point(1, 2), Point(3, 7), Point(5, 8), Point(8, 9),
        Point(10, 8), Point(13, 4), Point(13, 3), Point(12, 1)]
    small_polygon = [Point(3, 3), Point(4, 4), Point(6, 4), Point(7, 6), Point(9, 6),
                     Point(7, 2), Point(6, 3)]


    p0 = Point(4, 5)
    p0.direction = Vector2d(1, 1)
    p0.direction.print()
    # p0.draw(ax)
    point, = ax.plot(p0.x, p0.y, 'o', markersize=5)
    draw_polygon(big_polygon)
    draw_polygon(small_polygon)

    print('До')
    p0.print()
    anim = FuncAnimation(fig, animate)
    print('После')
    p0.print()

    plt.show()
