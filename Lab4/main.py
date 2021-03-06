import matplotlib.pyplot as plt

from Point import Point
from grahamMethod import graham_method

if __name__ == '__main__':
    points_set = [Point(1, 1), Point(2, 2), Point(3, 0), Point(2, 4), Point(1, 2), Point(3, 5)]
    arr = graham_method(points_set)