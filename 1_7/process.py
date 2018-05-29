from table_importer import TableImporter
from csv_writer import CSVWriter
from compute import *


def main():
    r = 0.038 / 2
    d = 0.024
    mark = 30

    tables = TableImporter()
    writer = CSVWriter()

    table = tables.get_table()

    writer.string_write(["theory", "exp", "error"])

    while table is not None:
        times = get_1d_data(table, 0)
        ys = get_1d_data(table, 2)
        h = get_h(mark)
        valid_ys = filter_descending_movement(ys)
        valid_ys_in_meter = change_to_meter(valid_ys)

        start_point = (times[1], valid_ys_in_meter[1])
        end_point = (times[len(valid_ys) - 2], valid_ys_in_meter[len(valid_ys_in_meter) - 2])

        exp_time = end_point[0] - start_point[0]
        theory_time = theoretical_time(start_point, end_point, h, r, d)
        error = (exp_time - theory_time) / theory_time * 100

        writer.write([theory_time, exp_time, error])

        table = tables.get_table()



if __name__ == '__main__':
    main()
