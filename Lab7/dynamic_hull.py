from utils.utils import check_triangle, check_point_pos, next_el


def dynamic_hull(point, CH):
    n = len(CH)
    # точка
    if n == 0:
        CH.append(point)
    # две точки
    elif n == 1:
        # если совпадают, добавляем одну, иначе две
        if not CH[0] == point:
            CH.append(point)
    # три точки
    elif n == 2:
        CH = check_triangle(CH[0], CH[1], point)

    if n >= 3:
        S = []
        for i in range(0, n):
            # следующая точка оболочки для текущей
            next_point = next_el(i, n)
            # если сторона оболочки "видна" из добавленной точки добавляем индексы вершин стороны
            if check_point_pos(CH[i], CH[next_point], point) < 0:
                if S.count(i) == 0:
                    S.append(i)
                if S.count(next_point) == 0 or S[0] == next_point:
                    S.append(next_point)
        s = len(S)
        if not s == 0:
            # если конечные эл-ты множ-ва вершин сторон, "видимых из точки", равны
            # то надо удалить эту вершину в оболочке и на её место вставить точку
            if S[0] == S[s - 1]:
                start_index = 0
                s = 2
                insert_index = S[0]
            # иначе удаляем все элементы между первым и последним и вставляем между ними точку
            else:
                insert_index = S[0] + 1
                start_index = 1
            # меняем оболочку
            for i in range(start_index, s - 1):
                CH.remove(CH[S[i]])
            CH.insert(insert_index, point)

    return CH
