from jarvis import jarvis_method
from utils.utils import *


def next_el(i, n):
    return i + 1 if i < n - 1 else 0


def diameter_of_set(stack):
    n = len(stack)
    start = 0
    maxs = 0
    # находим точку start
    for j in range(1, n - 2):
        square1 = abs(determinant(stack[n - 1], stack[0], stack[j]))
        # square2 = abs(determinant(stack[n - 1], stack[0], stack[j + 1]))
        if square1 >= maxs:
            start = j
            maxs = square1

    d = 0
    i = 0
    end = 0
    while end < n - 1:
        # находим точку end
        j = start
        square1 = abs(determinant(stack[i], stack[i + 1], stack[j]))
        square2 = abs(determinant(stack[i], stack[i + 1], stack[j + 1]))
        while square1 < square2:
            j += 1
            square1 = abs(determinant(stack[i], stack[i + 1], stack[j if j  < n else 0]))
            square2 = abs(determinant(stack[i], stack[i + 1], stack[j + 1 if j + 1 < n else 0]))

        end = j

        # находим максимальное расстояние между точками
        for t in range(start, end + 1):
            if Vector2d.get_length(stack[i], stack[t if t < n else 0]) > d:
                d = Vector2d.get_length(stack[i], stack[t])

        start = end
        i += 1

    return d