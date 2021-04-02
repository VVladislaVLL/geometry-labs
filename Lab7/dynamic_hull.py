from utils.utils import check_triangle, check_point_pos, next_el


def dynamic_hull(point_set, CH=[]):
    n = len(point_set)
    # точка
    if n == 1:
        CH.append(point_set[0])
    # две точки
    elif n == 2:
        # если совпадают, добавляем одну, иначе две
        if point_set[0] == point_set[1]:
            CH.append(point_set[0])
        else:
            CH.append(point_set[0])
            CH.append(point_set[1])
    # три точки
    elif n == 3:
        points = check_triangle(point_set)
        # если 1 точка - все 3 совпадают - добавляем её
        if len(points) == 1:
            CH.append(points)
        # если 2 точки - 2 совпадают и 1 отличная - добавляем 2 точки
        # или 3 различные точки на одной прямой
        elif len(points) == 2:
            CH.append(points[0])
            CH.append(points[1])
        # все 3 точки различные и не одной прямой
        else:
            CH.append(points[0])
            CH.append(points[1])
            CH.append(points[2])

    if len(CH) >= 3:
        S = []
        for i in range(0, len(CH)):
            # следующая точка оболочки для текущей
            next_point = next_el(i, len(CH))
            # если сторона оболочки "видна" из добавленной точки добавляем сторону
            if check_point_pos(CH[i], CH[next_point], point_set[n - 1]) < 0:
                if S.count(CH[i]) == 0:
                    S.append(CH[i])
                if S.count(CH[next_point]) == 0:
                    S.append(CH[next_point])
        # если множество видимых сторон не пусто, оставляем первую и последнюю
        # вершины из мн-ва и между ними добавляем добавленную точку
        if not S == []:
            S = [S[0], point_set[n - 1], S[len(S) - 1]]

        # меняем оболочку
        i = CH.index(S[0])
        j = CH.index(S[2])

        for k in range(i + 1, j):
            CH.remove(CH[k])
        CH.insert(i + 1, S[1])

    return CH