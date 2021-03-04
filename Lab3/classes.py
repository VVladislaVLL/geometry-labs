from math import sqrt, sin, cos
from graph import draw_line


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picture = 0

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

    @staticmethod
    def count_vector(p1, p2):
        return Vector(p2.x - p1.x, p2.y - p1.y)

    # @staticmethod
    # def static_sum(v1, v2):
    #     return Vector(Point(v1.x + v2.x), Point(v1.y + v2.y))

    @staticmethod
    def static_rotate_vector(vector, angle, flag):
        if flag:
            x_ = vector.x * cos(angle) - vector.y * sin(angle)
            y_ = vector.x * sin(angle) + vector.y * cos(angle)
        else:
            x_ = vector.x * cos(angle) + vector.y * sin(angle)
            y_ = -vector.x * sin(angle) + vector.y * cos(angle)

        r_x = round(x_, 3)
        r_y = round(y_, 3)
        r_p2 = Point((vector.x + vector.p1.x), (vector.y + vector.p1.y))
        return Vector(vector.p1, Point(r_x, r_y))




class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def scalar_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y

    @staticmethod
    def check_perpendicularity(v1, v2):
        return Vector2d.scalar_product(v1, v2) == 0

    @staticmethod
    def s_normalize(v):
        module = v.get_module()
        v.x /= module
        v.y /= module

    @staticmethod
    def get_vector(alpha, speed=1):
        return Vector2d(speed * cos(alpha), speed * sin(alpha))

    @staticmethod
    def s_get_perpendicular(x, y):
        return Vector2d(y, -x)

    @staticmethod
    def s_change_system(v):
        coef = 50
        new_point = Point(v.x * coef, v.y * coef)
        return Vector2d(new_point.x + 500, -new_point.y + 500)

    def change_system(self):
        return Vector2d(self.x, -self.y)

    def sum(self, vector):
        self.x += vector.x
        self.y += vector.y

    def minus(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def get_perpendicular(self):
        return Vector2d(self.y, -self.x)

    def rotate(self, angle, flag=True):
        if flag:
            x_ = self.x * cos(angle) - self.y * sin(angle)
            y_ = self.x * sin(angle) + self.y * cos(angle)
        else:
            x_ = self.x * cos(angle) + self.y * sin(angle)
            y_ = -self.x * sin(angle) + self.y * cos(angle)

        self.x = round(x_, 3)
        self.y = round(y_, 3)

    def get_module(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        module = self.get_module()
        self.x /= module
        self.y /= module

    def print(self):
        print('[' + str(self.x) + ', ' + str(self.y) + ']')


