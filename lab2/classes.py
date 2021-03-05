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
