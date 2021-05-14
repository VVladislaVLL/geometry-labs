import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera
from matplotlib import rcParams

from classes.Point import Point
from utils.graph import draw_polygon
from utils.utils import get_length, get_point_position, my_det2, my_det, get_next, check_position

rcParams['animation.convert_path'] = r'C:\Program Files\ImageMagick-7.0.10-Q16\convert.exe'
rcParams['animation.ffmpeg_path'] = r'C:\Program Files\ImageMagick-7.0.10-Q16\ffmpeg.exe'

# Количество итераций движения фигур
CNT = 20

fig, ax = plt.subplots()
camera = Camera(fig)


# Функция проверяющая нацелен ли отрезок первый отрезок на второй
# Передаем координаты начала и конца первого и воторого отрезков
def is_aimed(p1_start, p1_end, p2_start, p2_end):
    x1_v = p1_end.x - p1_start.x
    y1_v = p1_end.y - p1_start.y
    x2_v = p2_end.x - p2_start.x
    y2_v = p2_end.y - p2_start.y
    x12_v = p1_end.x - p2_start.x
    y12_v = p1_end.y - p2_start.y
    if ((my_det(x2_v, y2_v, x12_v, y12_v) > 0)
            and (my_det(x2_v, y2_v, x1_v, y1_v) < 0)):
        return True
    if ((my_det(x2_v, y2_v, x12_v, y12_v) < 0)
            and (my_det(x2_v, y2_v, x1_v, y1_v) > 0)):
        return True
    # Случай если отрезки лежат на одной прямой
    if ((get_point_position(p1_start, p1_end, p2_start) == 0)
            and (get_point_position(p1_start, p1_end, p2_end) == 0)
            and (((-x1_v) * (p2_end.x - p1_end.x)) + ((-y1_v) * (p2_end.y - p1_end.y))) < 0):
        return True
    return False


# Функция возвращающая точку пересечения отрезков
def get_point_intersection(p1, p2, p3, p4):
    d1 = p1.x - p2.x
    d2 = p3.x - p4.x
    d3 = p1.y - p2.y
    d4 = p3.y - p4.y
    tmp = my_det(d1, d2, d3, d4)
    dd1 = my_det(p1.x, p1.y, p2.x, p2.y)
    dd2 = my_det(p3.x, p3.y, p4.x, p4.y)
    x = my_det(dd1, dd2, d1, d2) / tmp
    y = my_det(dd1, dd2, d3, d4) / tmp
    return Point(x, y)


# Функция определяющая является ли первый отрезок внешним
def is_first_external(p1, p2, p3, p4):
    if (get_point_position(p3, p4, p2) == -1):
        return True
    if ((get_point_position(p3, p4, p2) == 0) and (get_point_position(p3, p4, p1) == -1)):
        return True
    return False


# Функция возвращающая массив точек пересечения многоугольников
def get_intersection(P, Q):
    # Получаем количества вершин многоугольников
    n1 = len(P)
    n2 = len(Q)
    # Создаем пустые массивы для хранения результата
    Res = []
    # "Окно" для движения по первому многоугольнику
    p = 0
    # "Окно" для движения по второму многоугольнику
    q = 0
    # Количество операций
    k = 0
    # Фиксируем окно q из второго многоугольника и для него подбираем окно p из первого многоугольника
    for i in range(0, n1):
        if (get_point_position(P[i], P[get_next(i, n1)], Q[0]) == -1) or (
                get_point_position(Q[0], Q[1], P[get_next(i, n1)]) == -1):
            p = i
            break
    # следующие точки
    p_next = get_next(p, n1)
    q_next = get_next(q, n2)
    # Идем циклом по точкам многоугольника
    while k != (2 * (n1 + n2)):
        # Случай если окна нацелены друг на друга
        if (is_aimed(P[p], P[p_next], Q[q], Q[q_next]) and is_aimed(Q[q], Q[q_next], P[p], P[p_next])):
            # Двигаем внешнее окно
            if is_first_external(P[p], P[p_next], Q[q], Q[q_next]):
                p = p_next
                p_next = get_next(p, n1)
            else:
                q = q_next
                q_next = get_next(q, n2)
        # Случай когда p нацелен на q, а q на p не нацелен
        elif (is_aimed(P[p], P[p_next], Q[q], Q[q_next]) and is_aimed(Q[q], Q[q_next], P[p], P[p_next]) == False):
            # Если p - внешнее окно, то добавляем конечную вершину в ответ
            if is_first_external(P[p], P[p_next], Q[q], Q[q_next]) == False:
                Res.append(P[p_next])
            # Двигаем окно p
            p = p_next
            p_next = get_next(p, n1)
        # Случай когда q нацелен на p, а p на q не нацелен
        elif (is_aimed(P[p], P[p_next], Q[q], Q[q_next]) == False and is_aimed(Q[q], Q[q_next], P[p], P[p_next])):
            # Если q - внешнее окно, то добавляем конечную вершину в ответ
            if is_first_external(Q[q], Q[q_next], P[p], P[p_next]) == False:
                Res.append(Q[q_next])
            # Двигаем окно q
            q = q_next
            q_next = get_next(q, n2)
        # Случай если окна не нацелены друг на друга
        elif (is_aimed(P[p], P[p_next], Q[q], Q[q_next]) == False and is_aimed(Q[q], Q[q_next], P[p],
                                                                               P[p_next])) == False:
            # Если окна пересекаются, то добавляем точку пересечения в ответ
            if (check_position(P[p], P[p_next], Q[q], Q[q_next])):
                point = get_point_intersection(P[p], P[p_next], Q[q], Q[q_next])
                Res.append(point)
            # Двигаем внешнее окно
            if is_first_external(P[p], P[p_next], Q[q], Q[q_next]):
                p = p_next
                p_next = get_next(p, n1)
            else:
                q = q_next
                q_next = get_next(q, n2)
        # Если первая добавленная точка совпала с последней
        if ((len(Res) > 1) and (Res[0] == Res[-1])):
            break
        k += 1
    # Удаляем совпашую точку
    if (len(Res) > 0):
        del Res[-1]
    return Res


def main():
    # Количество вершин в первом многоугольнике
    n1 = 5
    # Координаты точек вершин первого многоугольника
    P = [Point(-5.0, 0.6), Point(-2, 2.1), Point(-3, 3.6), Point(-7, 3.6), Point(-8, 2.1)]
    # Вектор движения точек первого многоугольника
    x1_vector = 0.5
    y1_vector = 0.0
    # Количество вершин во втором многоугольнике
    n2 = 6
    # Координаты точек вершин второго многоугольника
    Q = [Point(1, 2), Point(3, 0), Point(8, 0), Point(10, 2), Point(8, 4), Point(3, 4)]
    # Вектор движения точек второго многоугольника
    x2_vector = -0.5
    y2_vector = 0.0
    # Запускам цикл на нужное количество итераций движения
    for k in np.arange(CNT):
        # Рисуем многоугольники
        draw_polygon(P)
        draw_polygon(Q)

        # Получаем массив точек пересечения многоугольников
        res = get_intersection(P, Q)
        # Зарисовываем пересечение многоугольников
        ax.fill(list(map(lambda p: p.x, res)), list(map(lambda p: p.y, res)), "gray")
        # Делаем шаг анимации
        camera.snap()
        # Двигаем многоугольники
        for i in np.arange(n1):
            P[i].x += x1_vector
            P[i].y += y1_vector
        for i in np.arange(n2):
            Q[i].x += x2_vector
            Q[i].y += y2_vector
    # Сохраняем анимацию
    animation = camera.animate()
    animation.save('animation.gif', writer='pillow')


if __name__ == "__main__":
    main()
