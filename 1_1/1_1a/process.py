from table_importer import TableImporter
from csv_writer import CSVWriter
from compute import compute


def main():
    tables = TableImporter()
    writer = CSVWriter()

    table = tables.get_table()

    while table is not None:
        writer.write(compute(table))
        table = tables.get_table()


if __name__ == '__main__':
    main()
