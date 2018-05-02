import math


def get_column(table, index):
    result = []
    for row in table:
        result.append(row[index])
    return result


def get_speed(xs, ys, time, index, step):
    next_index = index + step
    if next_index < 0:
        next_index = 0
    if next_index >= len(time):
        next_index = len(time) - 1
    dx = (xs[next_index] - xs[index]) / 100
    dy = (ys[next_index] - ys[index]) / 100
    dt = abs(time[next_index] - time[index])
    distance = math.sqrt(dx * dx + dy * dy)
    return distance / dt
