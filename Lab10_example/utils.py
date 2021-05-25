import matplotlib.pyplot as plt
import random


def draw_line(p1, p2, color=False):
    if color:
        plt.plot([p1.x, p2.x], [p1.y, p2.y], color=color)
    else:
        plt.plot([p1.x, p2.x], [p1.y, p2.y])
    # print(sec_point, sec_point, zero_point)


def det(a, b, c, d):
    return a * d - b * c


def define_orientation(p1, p2, p0):
    D = det((p2.x - p1.x), (p2.y - p1.y), (p0.x - p1.x), (p0.y - p1.y))
    if D > 0:
        return "left"
    elif D < 0:
        return "right"
    else:
        return "on"


def is_intersect(p1, p2, p3, p4):
    det1 = det((p2.x - p1.x), (p2.y - p1.y), (p3.x - p1.x), (p3.y - p1.y))
    det2 = det((p2.x - p1.x), (p2.y - p1.y), (p4.x - p1.x), (p4.y - p1.y))
    det3 = det((p4.x - p3.x), (p4.y - p3.y), (p1.x - p3.x), (p1.y - p3.y))
    det4 = det((p4.x - p3.x), (p4.y - p3.y), (p2.x - p3.x), (p2.y - p3.y))
    if det1 * det2 <= 0 and det3 * det4 <= 0:
        return True
    else:
        return False


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


def point_on_line(point, p1, p2):
    p_max = Point(max(p1.x, p2.x), max(p1.y, p2.y))
    p_min = Point(min(p1.x, p2.x), min(p1.y, p2.y))
    if define_orientation(p1, p2, point) == "on" \
            and p_min.x <= point.x <= p_max.x and p_min.y <= point.y <= p_max.y:
        return True
    else:
        return False


def append_point(convex_hull, point):
    if point in convex_hull:
        return convex_hull
    if len(convex_hull) == 0 or len(convex_hull) == 1:
        print(convex_hull)
        convex_hull.append(point)
        return convex_hull
    if len(convex_hull) == 2:
        p1, p2 = convex_hull[0], convex_hull[1]
        if define_orientation(p1, p2, point) == "on":
            if (point_on_line(point, p1, p2)):
                print(point)
            elif (point_on_line(p1, point, p2)):
                print(p1)
                convex_hull = [p2, point]
            else:
                print(p2)
                convex_hull = [p1, point]
        else:
            if define_orientation(p1, p2, point) == "left":
                convex_hull = [p1, point, p2]
            else:
                convex_hull = [p1, p2, point]
        return convex_hull
    if len(convex_hull) > 2:
        right_sides = []
        for i in range(len(convex_hull)):
            if define_orientation(convex_hull[i], convex_hull[(i + 1) % len(convex_hull)], point) == "right":
                right_sides.append((convex_hull[i], convex_hull[(i + 1) % len(convex_hull)]))
            elif 0 not in right_sides:
                right_sides.append(0)
        if len(right_sides) == 1:
            return convex_hull
        convex_hull = []
        for side in right_sides:
            if side == 0:
                convex_hull.append(point)
            else:
                if side[0] not in convex_hull:
                    convex_hull.append(side[0])
                if side[1] not in convex_hull:
                    convex_hull.append(side[1])
        return convex_hull


def draw_figure(points, color=False):
    for ind in range(0, len(points)):
        try:
            draw_line(points[ind], points[ind + 1], color)
        except:
            draw_line(points[ind], points[0], color)
