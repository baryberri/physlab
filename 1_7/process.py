from table_importer import TableImporter
from csv_writer import CSVWriter
from compute import *


def main():
    tables = TableImporter()
    writer = CSVWriter()

    table = tables.get_table()

    while table is not None:
        min_max_table = get_min_max(table, 2)

        period = get_period(min_max_table)
        amplitude = get_amplitude(min_max_table, 2)

        writer.string_write(["period"], end=",")
        writer.write(period)

        writer.string_write(["amplitude"], end=",")
        writer.write(amplitude)
        writer.write([])

        table = tables.get_table()


if __name__ == '__main__':
    main()
