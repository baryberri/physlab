import math
import numpy as np


def get_column(table, index):
    result = []
    for row in table:
        result.append(row[index])
    return result


def extract_consistent_row(table, base_index):
    result = [table[0]]
    index = 1
    value = table[0][base_index]
    while value == table[index][base_index]:
        result.append(table[index])
        index += 1
    return result


def get_average_rotation(table):
    start_time, start_angle = table[0][0], table[0][1]
    end_time, end_angle = table[-1][0], table[-1][1]
    # print(degree_to_radian(end_angle - start_angle))
    return degree_to_radian(end_angle - start_angle) / (end_time - start_time)


def compute_theory_rotation(r, w):
    I = 0.0118807
    g = 9.80665
    m = 0.1
    return (m * g * r) / (I * w)


def step_to_length(step):
    return 0.15 + 0.02 * (step - 1)


def degree_to_radian(degree):
    return math.pi / 180 * degree


def rpm_to_rad_per_sec(rpm):
    rps = rpm / 60
    return rps * math.pi * 2


def slice(table, index, value):
    result = []
    for row in table:
        if row[index] <= value:
            result.append(row)
        else:
            break
    return result


def average(values):
    result = 0
    for value in values:
        result += value
    return result / len(values)


def linear_regression(x, y):
    result = np.polyfit(x, y, 1)
    return result[0]
