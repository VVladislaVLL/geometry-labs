import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print('(' + str(self.x) + ', ' + str(self.y) + ')')

    def draw(self, ax):
        self.figure = ax.plot(self.x, self.y, 'go')

    def set_direction(self, vector):
        self.direction = vector

    def move(self):
        self.x += self.direction.x
        self.y += self.direction.y