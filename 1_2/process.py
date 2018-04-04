from table_importer import TableImporter
from csv_writer import CSVWriter
from compute import *


def main():
    tables = TableImporter()
    writer = CSVWriter()

    result_times = []
    result_degrees = []
    table = tables.get_table()
    while table is not None:
        times = get_times(table)
        ratio = compute_ratio(table)
        atan = compute_atan(ratio)
        positive_atan = atan_to_positive(atan)
        accumulated_atan = accumulate_degree(positive_atan)
        resulting_degree = set_starting_point_to_zero(accumulated_atan)
        result_times.append(times)
        result_degrees.append(resulting_degree)

        table = tables.get_table()

    result_to_write = [result_times[0]]
    for i in range(len(result_times)):
        result_to_write.append(result_degrees[i])

    writer.write_2d(result_to_write)


if __name__ == '__main__':
    main()
