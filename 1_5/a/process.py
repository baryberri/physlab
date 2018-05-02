from table_importer import TableImporter
from csv_writer import CSVWriter
from compute import *


def main():
    tables = TableImporter()
    writer = CSVWriter()

    table = tables.get_table()

    while table is not None:
        time = get_column(table, 0)
        moving_xs = get_column(table, 3)
        moving_ys = get_column(table, 4)

        past_degree = get_degree(moving_xs, moving_ys, 0)
        past_abs_dx = 0
        for i in range(1, len(table)):
            deg = get_degree(moving_xs, moving_ys, i)
            if deg is None:
                continue

            if abs(past_degree - deg) >= 10 and past_abs_dx > 1:
                print(i, time[i])
                break

            past_degree = deg
            past_abs_dx = get_abs_dx(moving_xs, i)

        table = tables.get_table()


if __name__ == '__main__':
    main()
