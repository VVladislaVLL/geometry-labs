import matplotlib.pyplot as plt

from utils.graph import draw_figure_ca
from utils.utils import get_scalar_product, check_point_pos
from classes.Point import Point


def reverse_if_left_orientation(points):
    i = 0
    while True:
        orientation = check_point_pos(points[i], points[i + 1], points[i + 2])
        i += 1
        if orientation == 0:
            continue
        elif orientation == 1:
            points.reverse()
            break
        else:
            break
    return points


def alg_Cyrus_Beck(segment, points):
    reverse_if_left_orientation(points)
    A = segment[0]
    B = segment[1]
    # инициализируем пределы значений параметра, предполагая что отрезок полностью видимый
    # T = {t0 = 0, t1 = 1}
    tA = 0
    tB = 1
    for i in range(len(points)):
        # зациклинность массива
        # edge = PiPi+1
        try:
            edge = points[i], points[i + 1]
        except:
            edge = points[i], points[0]
        # ---
        # находи нормаль
        normal = Point(edge[1].y - edge[0].y, edge[0].x - edge[1].x)
        t1 = (normal.x * (edge[1].x - A.x) + normal.y * (edge[1].y - A.y))
        t2 = (normal.x * (B.x - A.x) + normal.y * (B.y - A.y))
        if t2 != 0:
            t = t1 / t2
        else:
            continue
        scalar_product = get_scalar_product(Point(B.x - A.x, B.y - A.y), normal)
        # Если тип точки потенциально вход. то:
        if scalar_product > 0:
            tA = max(tA, t)
        else:
            tB = min(tB, t)
    if tA > tB:
        return 0, 0
    return tA, tB


def change_line_with_params(segment, t1, t2) -> [Point, Point]:
    return (Point(segment[0].x + (segment[1].x - segment[0].x) * t1, segment[0].y + (segment[1].y - segment[0].y) * t1),
            Point(segment[0].x + (segment[1].x - segment[0].x) * t2, segment[0].y + (segment[1].y - segment[0].y) * t2))


if __name__ == "__main__":
    # Отрезки
    segment_list = [
        [Point(2, 5), Point(4, 6)],
        [Point(-2, 2), Point(0, 4)],
        [Point(-4, 4), Point(4, 4)],
        [Point(-4, 2), Point(0.1, 4.4)],
        [Point(0, 6), Point(4, 6)],
        [Point(2, 2), Point(4, 5)],
        [Point(0, 5), Point(0, -5)]
    ]

    # Выпуклые многоугольники
    point_list = [
        [Point(-3, 0), Point(-5, 6), Point(4, 3), Point(1, 0)],
        [Point(-3, 0), Point(0, 4), Point(1, 6), Point(-2, 4.5)]
    ]
    for j in range(len(point_list)):
        for i in range(len(segment_list)):
            print("Case {0}:".format(i))
            draw_figure_ca(segment_list[i])
            draw_figure_ca(point_list[j])
            t1, t2 = alg_Cyrus_Beck(segment_list[i], point_list[j])
            print(t1, t2)
            draw_figure_ca(change_line_with_params(segment_list[i], t1, t2))
            plt.show()
