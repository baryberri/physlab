import math


def get_column(table, column):
    result = []
    for row in table:
        result.append(row[column])
    return result


def get_min_max(table, column):
    result = [table[0]]
    for i in range(1, len(table) - 1):
        previous_row = table[i - 1][column]
        current_row = table[i][column]
        next_row = table[i + 1][column]
        if current_row <= previous_row and current_row <= next_row and current_row != result[-1][column]:
            result.append(table[i])
        elif current_row >= previous_row and current_row >= next_row and current_row != result[-1][column]:
            result.append(table[i])
    return result[1:]


def get_period(min_max_table):
    result = []
    for i in range(len(min_max_table) - 2):
        result.append(min_max_table[i + 2][0] - min_max_table[i][0])
    return result


def get_amplitude(min_max_table, column):
    result = []
    for i in range(len(min_max_table) - 1):
        result.append(abs(min_max_table[i + 1][column] - min_max_table[i][column]) / 100)
    return result
