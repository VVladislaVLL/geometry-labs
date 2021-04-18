class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bound_points = []

    def bind(self, point):
        if point not in self.bound_points:
            point.bound_points.append(self)
            self.bound_points.append(point)

    def unbind(self, point):
        point.bound_points.remove(self)
        self.bound_points.remove(point)

    def __eq__(self, other):
        try:
            return self.x == other.x and self.y == other.y
        except:
            return False

    def __repr__(self):
        return f"Point [{str(self.x)}, {str(self.y)}]"

    def __hash__(self):
        return hash((self.x, self.y))

    def __getitem__(self, ind):
        if ind == 0:
            return self.x
        if ind == 1:
            return self.y

    def __setitem__(self, ind, value):
        if ind == 0:
            self.x = value
        if ind == 1:
            self.y = value

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** (1 / 2)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)