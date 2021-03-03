from math import sqrt, sin, cos
from graph import draw_line


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('(' + str(self.x) + ', ' + str(self.y) + ')')

    def change_system(self):
        coef = 50
        new_point = Point(self.x * coef, self.y * coef)
        return Point(new_point.x + 500, -new_point.y + 500)


class Vector:
    def __init__(self, point1, point2):
        self.x = 0
        self.y = 0
        self.p1 = point1
        self.p2 = point2
        self.count_coordinates()

    def count_coordinates(self):
        self.x = self.p2.x - self.p1.x
        self.y = self.p2.y - self.p1.y

    def print_vector(self):
        print('[' + str(self.x) + ', ' + str(self.y) + ']')

    def get_length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def rotate(self, angle, flag=True):
        if flag:
            x_ = self.x * cos(angle) - self.y * sin(angle)
            y_ = self.x * sin(angle) + self.y * cos(angle)
        else:
            x_ = self.x * cos(angle) + self.y * sin(angle)
            y_ = -self.x * sin(angle) + self.y * cos(angle)

        self.x = round(x_, 3)
        self.y = round(y_, 3)
        self.p2 = Point((self.x + self.p1.x), (self.y + self.p1.y))

    def draw(self, canv):
        draw_line(canv, self.p1, self.p2)
