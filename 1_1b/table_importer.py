import os


class TableImporter:
    def __init__(self, directory="./input"):
        file_names = list(filter(lambda filename: filename.endswith(".txt"), os.listdir(directory)))
        file_urls = [os.path.join(directory, filename) for filename in file_names]
        self.files = file_urls

    def get_table(self, delimiter="\t", header=True):
        if len(self.files) == 0:
            return None

        file_url = self.files.pop()
        print("Processing {}...".format(file_url))
        with open(file_url, "r") as file:
            table = file.readlines()

            if header:
                del table[0]

            split_table = [table_row.strip().split(delimiter) for table_row in table]
            float_table = [[float(data) for data in table_row] for table_row in split_table]

        return float_table
