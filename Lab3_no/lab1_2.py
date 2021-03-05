import random

import matplotlib.pyplot as plt

from lab1_1 import Point, det, draw_line


def is_intersect(p1, p2, p3, p4):
    det1 = det((p2.x - p1.x), (p2.y - p1.y), (p3.x - p1.x), (p3.y - p1.y))
    det2 = det((p2.x - p1.x), (p2.y - p1.y), (p4.x - p1.x), (p4.y - p1.y))
    det3 = det((p4.x - p3.x), (p4.y - p3.y), (p1.x - p3.x), (p1.y - p3.y))
    det4 = det((p4.x - p3.x), (p4.y - p3.y), (p2.x - p3.x), (p2.y - p3.y))
    if det1 * det2 <= 0 and det3 * det4 <= 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # p1 = Point(3,5)
    # p2 = Point(3, 7)
    # p3 = Point(3, 6)
    # p4 = Point(8, 6)
    p1 = Point(random.randint(0, 20), random.randint(0, 20))
    p2 = Point(random.randint(0, 20), random.randint(0, 20))
    p3 = Point(random.randint(0, 20), random.randint(0, 20))
    p4 = Point(random.randint(0, 20), random.randint(0, 20))
    draw_line(p1, p2)
    draw_line(p3, p4)
    plt.show()
    print("intersect:", is_intersect(p1, p2, p3, p4))