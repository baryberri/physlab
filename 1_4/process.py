from table_importer import TableImporter
from csv_writer import CSVWriter
from compute import *


def main():
    tables = TableImporter()
    writer = CSVWriter()
    table = tables.get_table(delimiter=",", header=5, footer=7)

    error_rate_result = []
    step = 3

    while table is not None:
        consistent_table = slice(table, 0, [15, 45])
        average_rpm = average(get_column(consistent_table, 3))
        w = rpm_to_rad_per_sec(average_rpm)

        theory_rotation = compute_theory_rotation(step_to_length(step), w)
        experiment_degree = linear_regression(get_column(consistent_table, 0), get_column(consistent_table, 1))
        experiment_rotation = degree_to_radian(experiment_degree)

        error_rate_result.append((experiment_rotation - theory_rotation) / theory_rotation * 100)

        table = tables.get_table(delimiter=",", header=5, footer=7)

    writer.write(error_rate_result)

if __name__ == '__main__':
    main()
