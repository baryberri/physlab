from table_importer import TableImporter
from compute import *


def main():
    tables = TableImporter()

    table = tables.get_table()

    while table is not None:
        time = get_column(table, 0)
        xs = get_column(table, 1)
        ys = get_column(table, 2)
        turning_point = None
        for i in range(1, len(table) - 2):
            if ys[i] > ys[i - 1] and ys[i] > ys[i + 1]:
                turning_point = i
                break

        before_speed = get_speed(xs, ys, time, turning_point - 1, -3)
        after_speed = get_speed(xs, ys, time, turning_point + 1, 3)
        print(before_speed, after_speed)
        print(get_incidence_reflection_angle(xs, ys, turning_point)[1])

        table = tables.get_table()


if __name__ == '__main__':
    main()
