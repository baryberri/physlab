import math


def get_column(table, index):
    result = []
    for row in table:
        result.append(row[index])
    return result


def get_distance(xs, ys, time):
    dx = xs[time + 1] - xs[time]
    dy = ys[time + 1] - ys[time]
    return math.sqrt(dx * dx + dy * dy)


def get_vector(xs, ys, time):
    dx = xs[time + 4] - xs[time + 1]
    dy = ys[time + 4] - ys[time + 1]
    return dx, dy


def get_speed(xs, ys, time, index, step):
    next_index = index + step
    if next_index < 0:
        next_index = 0
    elif next_index >= len(time):
        next_index = len(time) - 1
    dx = (xs[next_index] - xs[index]) / 100
    dy = (ys[next_index] - ys[index]) / 100
    dt = abs(time[next_index] - time[index])
    distance = math.sqrt(dx * dx + dy * dy)
    return distance / dt


def get_vector_size(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1])


def get_degree(v1, v2):
    v1_size = get_vector_size(v1)
    v2_size = get_vector_size(v2)
    inner_product = v1[0] * v2[0] + v1[1] * v2[1]
    return math.degrees(math.acos(inner_product / (v1_size * v2_size)))


def get_mass(v, v1, v2, b):
    m = 0.045
    a = v2 * v2
    b = m * v1 * v2 * math.cos(math.radians(b))
    c = m * m * (v1 * v1 - v * v)
    result = (-1 * b + math.sqrt(b * b - a * c)) / a
    return (result - 0.045) * 1000
