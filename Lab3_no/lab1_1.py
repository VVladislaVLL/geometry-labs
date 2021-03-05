import random

import matplotlib.pyplot as plt


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = (0, 0)

    def set_speed(self, speed):
        self.speed = speed

    def set_random_speed(self, value, seed=0):
        if seed != 0:
            random.seed(seed)
        r = random.uniform(-1, 1)
        self.speed = (value * r, value * (r - 1) if r > 0 else value * (r + 1))

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str(self.x) + "," + str(self.y)


def det(a, b, c, d):
    return a * d - b * c


def draw_line(p1, p2, color=False):
    if color:
        plt.plot([p1.x, p2.x], [p1.y, p2.y], color=color)
    else:
        plt.plot([p1.x, p2.x], [p1.y, p2.y])
    # print(sec_point, sec_point, zero_point)


def define_orientation(p1, p2, p0):
    D = det((p2.x - p1.x), (p2.y - p1.y), (p0.x - p1.x), (p0.y - p1.y))
    if D > 0:
        return "left"
    elif D < 0:
        return "right"
    else:
        return "on"


if __name__ == "__main__":
    p1 = Point(random.randint(0, 20), random.randint(0, 20))
    p2 = Point(random.randint(0, 20), random.randint(0, 20))
    p0 = Point(random.randint(0, 20), random.randint(0, 20))
    p1 = Point(3, 5)
    p2 = Point(3, 7)
    p0 = Point(3, 4)
    print(define_orientation(p1, p2, p0))
    draw_line(p1, p2)
    plt.plot(p0.x, p0.y, 'ro')
    plt.plot(p2.x, p2.y, 'ro')
    plt.show()
    # ctrl alt   o - import    l- style           ctrl p - funct params