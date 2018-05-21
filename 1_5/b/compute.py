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


def get_vector_size(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1])


def get_degree(v1, v2):
    v1_size = get_vector_size(v1)
    v2_size = get_vector_size(v2)
    inner_product = v1[0] * v2[0] + v1[1] * v2[1]
    return math.degrees(math.acos(inner_product / (v1_size * v2_size)))


def get_incidence_reflection_angle(xs, ys, turning_point):
    before_dx = xs[turning_point - 2] - xs[turning_point]
    before_dy = ys[turning_point - 2] - ys[turning_point]
    before = (before_dx, before_dy)

    after_dx = xs[turning_point + 2] - xs[turning_point]
    after_dy = ys[turning_point + 2] - ys[turning_point]
    after = (after_dx, after_dy)

    unit = (0, -1)

    incidence_angle = get_degree(unit, before)
    reflection_angle = get_degree(unit, after)
    return incidence_angle, reflection_angle
