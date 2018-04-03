from table_importer import TableImporter
from csv_writer import CSVWriter
from compute import *


def main():
    tables = TableImporter()
    writer = CSVWriter()

    data_to_write = []
    table = tables.get_table()
    while table is not None:
        times = get_times(table)
        ratio = compute_ratio(table)
        atan = compute_atan(ratio)
        positive_atan = atan_to_positive(atan)
        accumulated_atan = accumulate_degree(positive_atan)
        resulting_degree = set_starting_point_to_zero(accumulated_atan)
        regression_result = regression(times, resulting_degree)
        r2 = coefficient_of_determination(times, resulting_degree, regression_result)
        i = momentum_of_inertial(regression_result)
        writer.write([regression_result[0], regression_result[1], regression_result[2], r2, i])

        table = tables.get_table()

    writer.write(data_to_write)


if __name__ == '__main__':
    main()
