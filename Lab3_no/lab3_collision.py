import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from lab1_1 import Point
from lab1_2 import is_intersect
from lab1_3 import draw_figure
from lab2 import is_on
from lab3_convex import is_inside
from numpy import argmin
from math import sqrt


# crashes if inside the corner


class Vector():
    def __init__(self, point1, point2):
        if type(point1) == Point:
            self.vx = point2.x - point1.x
            self.vy = point2.y - point1.y
        else:
            self.vx = point1
            self.vy = point2

    def __mul__(self, other):
        if type(self) == type(other):
            return self.vx * other.vx + self.vy * other.vy
        else:
            self.vx *= other
            self.vy *= other
            return self

    def __add__(self, other):
        self.vx += other.vx
        self.vy += other.vy
        return self

    def __sub__(self, other):
        self.vx -= other.vx
        self.vy -= other.vy
        return self

    def __len__(self):
        return self.vx * self.vx + self.vy * self.vy

    def __str__(self):
        return str(self.vx) + "," + str(self.vy)


def distance(p1, p2):
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def animate(i):
    collision(given_point, points, "outside")
    given_point.move()
    point.set_data(given_point.x, given_point.y)
    return point,


def collision(given_point, points, position):
    # position can be inside or outside
    next_position_point = Point(given_point.x + given_point.speed[0], given_point.y + given_point.speed[1])
    flag = is_inside(points, next_position_point)
    if flag == position or flag == "on":
        for ind in range(len(points) - 1):
            if (is_intersect(points[ind], points[ind + 1], next_position_point, given_point)):
                b = Vector(points[ind], points[ind + 1])
        if (is_intersect(points[-1], points[0], next_position_point, given_point)):
            b = Vector(points[-1], points[0])
        a = Vector(given_point, next_position_point)
        try:
            arr = []
            for point in points:
                arr.append(distance(point, given_point))
            new_a = b * ((a * b) / (b * b) * 2) - a
            given_point.set_speed((new_a.vx, new_a.vy))
        except:
            given_point.x, given_point.y = (48, 54)   #тут иногда возникает исключение, когда точка попадает прямо в угол. тогда формула неправильная
            # и надо считать по другому. тут же она выносится за пределы полигона и, следственно, удаляется.
            # print("ex")
            # arr = []
            # for point in points:
            #     arr.append(distance(point, given_point))
            # i = argmin(arr)
            # try:
            #     b1 = Vector(points[i], points[i+1])
            # except:
            #     b1 = Vector(points[i], points[0])
            # try:
            #     b2 = Vector(points[i], points[i-1])
            # except:
            #     b2 = Vector(points[i], points[-1])
            # b1 = b1 * (1 / len(b1))
            # b2 = b2 * (1 / len(b2))
            # orthogonal = Vector(b1.vx + b2.vx, b1.vy + b2.vy)
            # b = Vector(-orthogonal.vy, orthogonal.vx)
            # new_a = b * ((a * b) / (b * b) * 2) - a
            # given_point.set_speed((new_a.vx, new_a.vy))


if __name__ == "__main__":
    given_point = Point(0, -3)
    given_point.set_speed((0,-1))
    points = [Point(-30, 30), Point(30, 30), Point(0, -50)]

    fig = plt.figure()
    ax = plt.axes(xlim=(-50, 150), ylim=(-60, 150))
    point, = ax.plot(0, -30, 'o', markersize=4)
    anim = FuncAnimation(fig, animate, frames=1, interval=200, blit=True)

    draw_figure(points)
    plt.show()