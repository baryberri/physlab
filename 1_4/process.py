from table_importer import TableImporter
from csv_writer import CSVWriter
from compute import *


def main():
    tables = TableImporter()
    writer = CSVWriter()
    table = tables.get_table(delimiter=",", header=5, footer=7)

    error_rate_result = []
    step = 4

    while table is not None:
        consistent_table = extract_consistent_row(table, 3)
        w = rpm_to_rad_per_sec(consistent_table[0][3])

        theory_rotation = compute_theory_rotation(step_to_length(step), w)
        experiment_rotation = get_average_rotation(consistent_table)

        error_rate_result.append((experiment_rotation - theory_rotation) / theory_rotation * 100)

        table = tables.get_table(delimiter=",", header=5, footer=7)

    writer.write(error_rate_result)

if __name__ == '__main__':
    main()
