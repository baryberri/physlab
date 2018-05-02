from table_importer import TableImporter
from csv_writer import CSVWriter
from compute import *


def main():
    tables = TableImporter()

    table = tables.get_table()

    while table is not None:
        time = get_column(table, 0)
        static_xs = get_column(table, 1)
        static_ys = get_column(table, 2)
        moving_xs = get_column(table, 3)
        moving_ys = get_column(table, 4)

        start_index = None
        for i in range(len(table) - 1):
            if get_distance(static_xs, static_ys, i) > 0.65:
                start_index = i + 1
                break

        moving_vector = get_vector(moving_xs, moving_ys, start_index)
        static_vector = get_vector(static_xs, static_ys, start_index)
        observed_beta = get_degree(moving_vector, static_vector)

        past_speed = get_speed(moving_xs, moving_ys, time, start_index - 2, -3)
        moving_speed = get_speed(moving_xs, moving_ys, time, start_index + 2, 3)
        static_speed = get_speed(static_xs, static_ys, time, start_index + 2, 3)

        print(get_mass(past_speed, moving_speed, static_speed, observed_beta))

        table = tables.get_table()


if __name__ == '__main__':
    main()
