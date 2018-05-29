import os


class TableImporter:
    def __init__(self, directory="./input"):
        file_names = list(filter(lambda filename: filename.endswith(".txt"), os.listdir(directory)))
        file_urls = [os.path.join(directory, filename) for filename in file_names]
        self.files = file_urls

    def get_table(self, delimiter="\t", header=0, footer=0):
        if len(self.files) == 0:
            return None

        file_url = self.files.pop()
        print("Processing {}...".format(file_url))
        with open(file_url, "r", encoding='cp949') as file:
            table = file.readlines()

            for _ in range(header):
                del table[0]

            for _ in range(footer):
                del table[-1]

            split_table = [table_row.strip().split(delimiter) for table_row in table]
            float_table = [[float(data.strip()) for data in table_row] for table_row in split_table]

        return float_table
