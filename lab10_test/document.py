from classes.Vector2d import Vector2d
from grahamMethod import *


def cos_angle(v1, v2):
	cos_a = (v1.x * v2.x + v1.y * v2.y) /(v1.get_legth() * v2.get_length())
	return cos_a

def delaunay_triangulation(points):
    gr = graham_method(points)
    P = gr[0]
    CH = gr[1]
    l_s = line_segments(CH)

    # E = 3V - out_V - 3
    edge_limit = 3 * len(points) - len(CH) - 3

    triangulation = []
    triangulation += l_s

    new_edge = []

    for side in l_s:

        base = side

        # p_m = min(P, key=lambda p: cos_angle(vector(p, base[0]), vector(p, base[1])))
        p_m = min(P, key=lambda p: cos_angle(Vector2d(p, base[0]), Vector2d(p, base[1])))

        if [p_m, base[0]] in triangulation or [base[0], p_m] in triangulation:
            pass
        else:
            triangulation.append([p_m, base[0]])
            new_edge.append([p_m, base[0]])

        if [base[1], p_m] in triangulation or [p_m, base[1]] in triangulation:
            pass
        else:
            triangulation.append([base[1], p_m])
            new_edge.append([base[1], p_m])

    if len(triangulation) == edge_limit:
        return triangulation

    new_edge_loop = []
    for i in new_edge:
        new_edge_loop.append(i)

    while True:
        for side in new_edge:

            base = side

            p_m = min(P, key=lambda p: cos_angle(Vector2d(p, base[0]), Vector2d(p, base[1])))

            if [p_m, base[0]] in triangulation or [base[0], p_m] in triangulation:
                pass
            else:
                triangulation.append([p_m, base[0]])
                new_edge.append([p_m, base[0]])

            if [base[1], p_m] in triangulation or [p_m, base[1]] in triangulation:
                pass
            else:
                triangulation.append([base[1], p_m])
                new_edge.append([base[1], p_m])

        if len(triangulation) == edge_limit:
            return triangulation
