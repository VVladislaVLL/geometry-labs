import matplotlib.pyplot as plt


def draw_polygon(polygon):
    cor_x = list(map(lambda p: p.x, polygon))
    cor_y = list(map(lambda p: p.y, polygon))
    cor_x.append(polygon[0].x)
    cor_y.append(polygon[0].y)
    plt.plot(cor_x, cor_y)