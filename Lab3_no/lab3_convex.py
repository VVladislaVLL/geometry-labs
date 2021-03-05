from lab1_1 import Point, define_orientation
from lab1_3 import draw_figure
from lab2 import dimensional_test, is_on
from lab3_test import test_inside
import copy


def create_sections(sections):
    i = 0
    while True:
        orientation = define_orientation(sections[i], sections[i + 1], sections[i + 2])
        i += 1
        if orientation == "on":
            continue
        elif orientation == "right":
            sections.reverse()
            break
        else:
            break
    return sections


def determine_section(sections, given_point):
    start = 0
    end = len(sections) - 1
    while end - start > 1:
        sep = int((start + end) / 2)
        orientation = define_orientation(sections[0], sections[sep], given_point)
        if orientation == "left":
            start = sep
        else:
            end = sep
    return start, end


def is_inside(original_figure, given_point):
    if not dimensional_test(original_figure, given_point):
        return "outside"
    figure = copy.deepcopy(original_figure)
    figure += [figure[0]]
    if is_on(figure, given_point):
        return "on"
    sections = create_sections(figure)
    given_section = determine_section(sections, given_point)
    given_section = [sections[given_section[0]],
                     sections[given_section[1]]]
    orientation = define_orientation(given_section[0], given_section[1], given_point)
    if orientation == "left":
        return "inside"
    elif orientation == "right":
        return "outside"
    elif orientation == "on":
        return "on"


if __name__ == "__main__":
    convex_figure = [Point(-1, -1), Point(-5, 3), Point(0, 11), Point(6, 13), Point(10, 4.5), Point(4, -3)]
    test_inside(is_inside, range_number=300)
