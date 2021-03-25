from utils.utils import get_min_index, check_point_pos


def find_max_right(base_point, points_set):
    # Let the max point has the index 0
    max = points_set[0]

    if (max == base_point):
        # Change max point (first point from the end of points_set)
        max = points_set[-1]
        # The loop by points (excluding the last point)
        for point in points_set[:-1]:
            if check_point_pos(base_point, max, point) == -1 and point != base_point:
                max = point
    else:
        # The loop by points (excluding the first point)
        for point in points_set[1:]:
            if check_point_pos(base_point, max, point) == -1 and point != base_point:
                max = point
    return max


def jarvis_method(points_set):
    stack = []
    points_copy = points_set[:]

    # Find point with min Y coordinate
    stack.append(points_copy[get_min_index(points_set)])
    base_point = stack[0]

    # Jarvis Method
    while True:
        right_point = find_max_right(base_point, points_copy)
        base_point = right_point
        points_copy.remove(base_point)

        # If the shell is closed, then exit the loop
        if right_point == stack[0]:
            break

        stack.append(right_point)
    return stack
