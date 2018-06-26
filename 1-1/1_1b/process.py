from table_importer import TableImporter
from csv_writer import CSVWriter
from compute import *


def main():
    degree = 60

    tables = TableImporter()
    writer = CSVWriter()

    data_to_write = []
    table = tables.get_table()
    while table is not None:
        x_velocity = compute_x_velocity(table)
        initial_velocity = compute_initial_velocity(x_velocity, degree)
        times = get_times(table)
        ys = get_ys(table)
        theory_ys = compute_y_at_times(initial_velocity, degree, times)
        data_to_write.append(rms(ys, theory_ys))

        table = tables.get_table()

    writer.write(data_to_write)


if __name__ == '__main__':
    main()
