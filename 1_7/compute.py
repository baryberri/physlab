import math


def get_1d_data(table, index):
    result = []
    for row in table:
        result.append(row[index])
    return result


def filter_descending_movement(data):
    result = []
    for i in range(len(data)):
        if data[i] > data[i + 1]:
            result.append(data[i])
        else:
            break
    return result


def change_to_meter(data):
    result = []
    for h in data:
        h_in_meter = 0.01 * (h + 9.577) + 0.68242641
        result.append(h_in_meter)
    return result


def theoretical_time(start_point, end_point, h, r, d):
    reff_squared = (r ** 2) - ((d / 2) ** 2)
    k = (r ** 2) / reff_squared
    g = 9.80665
    start_h = start_point[1]
    end_h = end_point[1]
    return math.sqrt((2 + 0.8 * k) / g) * (2 / math.sqrt(2)) * (((h - end_h) ** 0.5) - ((h - start_h) ** 0.5))


def get_h(mark):
    return 0.64 + 0.01 * (10 - mark) * (math.sqrt(2) / 2)