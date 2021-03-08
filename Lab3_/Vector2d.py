from math import *

from Point import Point


class Vector2d:
    def __init__(self, point1, point2):
        if type(point1) == Point:
            self.x = point2.x - point1.x
            self.y = point2.y - point1.y
        else:
            self.x = point1
            self.y = point2

    def __str__(self):
        return '[' + str(self.x) + ', ' + str(self.y) + ']'

    @staticmethod
    def get_length(point1, point2):
        return sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

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
        return Vector2d(speed * cos(alpha), speed * sin(alpha)), speed

    @staticmethod
    def s_get_perpendicular(x, y):
        return Vector2d(y, -x)

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
