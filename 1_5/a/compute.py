import math


def get_column(table, index):
    result = []
    for row in table:
        result.append(row[index])
    return result


def get_abs_dx(xs, time):
    return abs(xs[time] - xs[time + 1])


def get_degree(xs, ys, time):
    dx = xs[time + 1] - xs[time]
    if dx == 0:
        return None

    dy = ys[time + 1] - ys[time]

    degree_in_rad = math.atan(dy / dx)
    return math.degrees(degree_in_rad)
