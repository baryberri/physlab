import math
import numpy as np


def get_times(table):
    num_items = len(table)
    times = [0 for _ in range(num_items)]
    for i in range(num_items):
        times[i] = table[i][0]
    return times


def compute_ratio(table):
    num_items = len(table)
    result = [0 for _ in range(num_items)]
    for i in range(len(table)):
        if table[i][1] == 0:
            result[i] = table[i][2] / (table[i][1] + 1e-4)
        else:
            result[i] = table[i][2] / table[i][1]

    return result


def set_starting_point_to_zero(data):
    data_to_substitute = data[0]
    result = [0 for _ in range(len(data))]
    for i in range(len(data)):
        result[i] = data[i] - data_to_substitute

    return result


def compute_atan(values):
    result = [0 for _ in range(len(values))]
    for i in range(len(values)):
        result[i] = math.atan(values[i])
    return result


def atan_to_positive(data):
    result = [0 for _ in range(len(data))]
    for i in range(len(data)):
        result[i] = data[i]
        if data[i] < 0:
            result[i] += math.pi / 2
    return result


def accumulate_degree(data):
    accumulation = 0
    result = [0 for _ in range(len(data))]
    result[0] = data[0]
    for i in range(1, len(data)):
        if data[i] < data[i - 1]:
            # accumulation
            accumulation += math.pi / 2
        result[i] = data[i] + accumulation
    return result


def regression(time, theta):
    p = np.polyfit(time, theta, deg=2)
    return p


def expect(data, func):
    return func[0] * (data ** 2) + func[1] * data + func[2]


def coefficient_of_determination(time, data, func):
    mean = np.mean(data)
    sst = 0
    sse = 0
    for i in range(len(time)):
        sst += (data[i] - mean) ** 2
        sse += (expect(time[i], func) - data[i]) ** 2
    return 1 - (sse / sst)


def momentum_of_inertial(func):
    m = 0.052
    g = 9.80665
    r = 0.03
    a = func[0]
    return ((m * g * r) / (2 * a)) - (m * r * r)