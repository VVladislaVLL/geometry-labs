import matplotlib.pyplot as plt

def draw_polygon(polygon):
    cor_x = list(map(lambda p: p.x, polygon))
    cor_y = list(map(lambda p: p.y, polygon))
    cor_x.append(polygon[0].x)
    cor_y.append(polygon[0].y)
    plt.plot(cor_x, cor_y)


def draw_line_segment(p1, p2):
    cor_x = list(map(lambda p: p.x, [p1, p2]))
    cor_y = list(map(lambda p: p.y, [p1, p2]))
    plt.plot(cor_x, cor_y, linewidth=2)


def draw_stack(stack):
    length = len(stack)
    if length < 2 :
        return
    else:
        i = 0
        while i < length - 1:
            draw_line_segment(stack[i], stack[i + 1])
            i += 1