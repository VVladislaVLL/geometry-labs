import matplotlib.pyplot as plt

from classes.Point import Point


def draw_points(points):
    plt.scatter(list(map(lambda p: p.x, points)), list(map(lambda p: p.y, points)))


def draw_polygon(polygon, color=""):
    cor_x = list(map(lambda p: p.x, polygon))
    cor_y = list(map(lambda p: p.y, polygon))
    cor_x.append(polygon[0].x)
    cor_y.append(polygon[0].y)
    plt.plot(cor_x, cor_y)
    if not color == "":
        plt.fill(color)
    # n = len(polygon)
    # for i in range(0, n):
    #   # plt.scatter(x[i], y[i])
    #   plt.plot([polygon[i].x, polygon[i + 1].x], [polygon[i].y, polygon[i + 1].y])
    # # plt.scatter(x[n - 1], y[n - 1])
    # plt.plot([polygon[n - 1].x, polygon[0].x], [polygon[n - 1].y, polygon[0].y])


def draw_line_segment(p1, p2):
    cor_x = list(map(lambda p: p.x, [p1, p2]))
    cor_y = list(map(lambda p: p.y, [p1, p2]))
    plt.plot(cor_x, cor_y, linewidth=2)


def draw_stack(stack):
    length = len(stack)
    if length < 2:
        return
    else:
        i = 0
        while i < length - 1:
            draw_line_segment(stack[i], stack[i + 1])
            i += 1


def draw_figure(points: [Point], color):
    for ind, point in enumerate(points):
        plt.plot([point.x, points[(ind + 1) % len(points)].x], [point.y, points[(ind + 1) % len(points)].y], color)


def draw_line(p1, p2, color=False):
    if color:
        plt.plot([p1.x, p2.x], [p1.y, p2.y], color=color)
    else:
        plt.plot([p1.x, p2.x], [p1.y, p2.y])
    # print(sec_point, sec_point, zero_point)


def draw_figure_ca(points, color=False):
    for ind in range(0, len(points)):
        try:
            draw_line(points[ind], points[ind + 1], color)
        except:
            draw_line(points[ind], points[0], color)
